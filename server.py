"""

This is a copy of server.py that has been changed slightly (changes reverted) to make the program work

"""


# initially generated by chatGPT to help me learn the what is going on with this module. 
# Extensive modifications have been made my me on top of the skeleton ChatGPT created.

import socket
import threading

HOST = ""  
PORT = 80

BLANK_CHARACTER = 0

def handle_client(
        client_connection:socket.socket
        , client_address
        , game_board
        , player_index
        , turn_counter
        # , is_player1_turn
        , game_over
        ):
    
    
    print(f"\nClient Address: {client_address}")
    player_has_won = False
    global is_player1_turn
    

    # if not first_time
    
    try:
        while not player_has_won:
                if game_over:
                    player_has_won = True
                    continue
                
                #get data
                data = client_connection.recv(1024)

                #check if data is truthy (client has not closed connection)
                if data:

                    #decode to string, remove and store op code
                    decoded_data = data.decode()
                    print(f"From: {client_address}\n\tincoming transmission: {decoded_data}\n")
                    operation_code  = decoded_data[0]
                    decoded_data = decoded_data[1:]

                    player_number = int(f"{client_address}"[18:23])

                    #check if op code is PING SERVER
                    if operation_code == "P":

                        if is_player1_turn:

                            message = f"{player_index}Player 1 Turn".encode("utf-8")
                            client_connection.sendall(message)
                            print(is_player1_turn)
                            continue

                        else:
                            message = f"{player_index}Player 2 Turn".encode("utf-8")
                            client_connection.sendall(message)
                            print(is_player1_turn)
                            continue


                    #check if operation code (first index) is TERMINATE
                    if operation_code == "T":
                        client_connection.close()

                    #check if op code is REQUEST BOARD.
                    elif operation_code == "R":
                        message = f"{game_board}".encode("utf-8")
                        client_connection.sendall(message)

                    #check if op code is SENDING MOVE
                    elif operation_code == "M":
                        # row = int(decoded_data[0])
                        column = int(decoded_data[0])
                        value = player_number
                        
                        # fill in the correct row based on game state and given column
                        for i in range (6):
                            column_number_from_bottom_up = 5 - i
                            if game_board[column_number_from_bottom_up][column] == BLANK_CHARACTER:#"     ":
                                game_board[column_number_from_bottom_up][column] = value
                                break

                        # game_board[row][column] = value
                        show_game_board(game_board)
                        player_has_won = check_4_in_row(game_board)
                        if player_has_won:
                            print(player_has_won)
                        message = f"{game_board}{player_has_won}".encode("utf-8")
                        client_connection.sendall(message)
                        is_player1_turn = not is_player1_turn
                        print(f"I am {player_number}. I just ended my turn")
    
                        

    finally:
        client_connection.close()
        print(f"connection with {client_address} closed because win")
            
    
def show_game_board(game_board):
    print(f"The game board is: ")
    for row in game_board:
        print("\t" + f"{row}")
    print("\n")

def check_4_in_row(game_board):
    for row in range(len(game_board)):
        
        #check for diagonal top-L to bottom-R
        if row + 3 <= 5:
            if game_board[row][0] != 0:
                if game_board[row][0] == game_board[row + 3][3]:
                    if game_board[row][0] == game_board[row + 1][1]:
                        if game_board[row][0] == game_board[row + 2][2]:
                            return True
                        
            if game_board[row][1] != 0:
                if game_board[row][1] == game_board[row + 3][4]:
                    if game_board[row][1] == game_board[row + 1][2]:
                        if game_board[row][1] == game_board[row + 2][3]:
                            return True
                        
            if game_board[row][2] != 0:   
                if game_board[row][2] == game_board[row + 3][5]:
                    if game_board[row][2] == game_board[row + 2][4]:
                        if game_board[row][2] == game_board[row + 1][3]:
                            return True
                            
            if game_board[row][3] != 0:      
                if game_board[row][3] == game_board[row + 3][6]:
                    if game_board[row][3] == game_board[row + 2][5]:
                        if game_board[row][3] == game_board[row + 1][4]:
                            return True
        for i in range(0,3):
            #check for diagonal bottom-L to top-R   
            row_inverted = 5-row
            if row_inverted -3 >= 0:
                if game_board[row_inverted-i][0] != 0:
                    if game_board[row_inverted-i][0] == game_board[row_inverted - 3-i][3]:
                        if game_board[row_inverted-i][0] == game_board[row_inverted - 2-i][2]:
                            if game_board[row_inverted-i][0] == game_board[row_inverted - 1-i][1]:
                                return True

                if game_board[row_inverted-i][1] != 0:
                    if game_board[row_inverted-i][1] == game_board[row_inverted - 3-i][4]:
                        if game_board[row_inverted-i][1] == game_board[row_inverted - 2-i][3]:
                            if game_board[row_inverted-i][1] == game_board[row_inverted - 1-i][2]:
                                return True
                        
                if game_board[row_inverted-i][2] != 0:
                    if game_board[row_inverted-i][2] == game_board[row_inverted - 3-i][5]:
                        if game_board[row_inverted-i][2] == game_board[row_inverted - 2-i][4]:
                            if game_board[row_inverted-i][2] == game_board[row_inverted - 1-i][3]:
                                return True
                        
                if game_board[row_inverted-i][3] != 0:
                    if game_board[row_inverted-i][3] == game_board[row_inverted - 3-i][6]:
                        if game_board[row_inverted-i][3] == game_board[row_inverted - 2-i][5]:
                            if game_board[row_inverted-i][3] == game_board[row_inverted - 1-i][4]:
                                return True

        # check for horizontal 4inrow
        if game_board[row][0] != 0:
                if game_board[row][0] == game_board[row][3]:
                    if game_board[row][0] == game_board[row] [2]:
                        if game_board[row][0] == game_board[row][1]:
                            return True

        if game_board[row][1] != 0:
            if game_board[row][1] == game_board[row][4]:
                if game_board[row][1] == game_board[row][3]:
                    if game_board[row][1] == game_board[row][2]:
                        return True
                
        if game_board[row][2] != 0:
            if game_board[row][2] == game_board[row][5]:
                if game_board[row][2] == game_board[row][4]:
                    if game_board[row][2] == game_board[row][3]:
                        return True
                
        if game_board[row][3] != 0:
            if game_board[row][3] == game_board[row][6]:
                if game_board[row][3] == game_board[row][5]:
                    if game_board[row][3] == game_board[row][4]:
                        return True
        # check for vertical 4 in row
        if row <= 2:
            for i in range(0,7):
                
                if game_board[row][i] != 0:
                    if game_board[row][i] == game_board[row+3][i]:
                        if game_board[row][i] == game_board[row+2] [i]:
                            if game_board[row][i] == game_board[row+1][i]:
                                return True
                            
    else:
        return False
    


global is_player1_turn, game_over
is_player1_turn = True
game_over = False

def main():

    # stop_event = threading.Event()

    # game_board = [
    #       ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
    #     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
    #     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
    #     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
    #     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
    #     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
    # ]

    game_board = [
        [00000, 00000, 00000, 00000, 00000, 00000, 00000]
        , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
        , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
        , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
        , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
        , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
    ]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))
        #listen for connections
        s.listen(2)
        print(f"Server listening on port {PORT}...")

        try:
            player_number = 1
            turn_counter = 0
            


            while True:
                
                client_connection, client_address = s.accept()
                # is_odd_player = not is_odd_player

                client_thread = threading.Thread(
                    target=handle_client
                    , args = (
                      client_connection
                    , client_address
                    , game_board
                    , player_number
                    , turn_counter
                    # , is_player1_turn
                    , game_over
                    )
                    
                    )
                
                client_thread.start()
                
                player_number += 1
                # is_player1_turn = not is_player1_turn

        finally:
            s.close()
            print("Server socket closed")


if __name__ == "__main__":
    main()
