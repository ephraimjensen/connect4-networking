# initially generated by chatGPT to help me learn the what is going on with this module. 
# Extensive modifications have been made my me on top of the skeleton ChatGPT created.

import socket
import threading

HOST = ""  
PORT = 80

def handle_client(
        client_connection:socket.socket
        , client_address
        , game_board
        , player_number
        , turn_counter
        ):
    
    
    print(f"\nClient Address: {client_address}")

    # if not first_time
    
    try:
        while True:
                #tell client it is their turn (go_ahead)
                # client_connection.sendall(b"go ahead")

                #get data
                data = client_connection.recv(1024)

                #check if data is truthy (client has not closed connection)
                if data:
                    if turn_counter % 2 == player_number % 2:
                        turn_counter+=1

                        player_number = int(f"{client_address}"[18:23])

                        #decode to string, remove and store op code
                        decoded_data = data.decode()
                        print(f"From: {client_address}\n\tincoming transmission: {decoded_data}\n")
                        operation_code  = decoded_data[0]
                        decoded_data = decoded_data[1:]
                        
                        #check if operation code (first index) is TERMINATE
                        if operation_code == "T":
                            client_connection.close()

                        #check if op code is REQUEST BOARD.
                        elif operation_code == "R":
                            message = f"{game_board}".encode("utf-8")
                            client_connection.sendall(message)

                        #check if op code is PING SERVER
                        elif operation_code == "P":
                            message = f"status: Good. Your message was: {operation_code + decoded_data}".encode("utf-8")
                            client_connection.sendall(message)

                        #check if op code is SENDING MOVE
                        elif operation_code == "M":
                            # row = int(decoded_data[0])
                            column = int(decoded_data[0])
                            value = player_number
                            
                            # fill in the correct row based on game state and given column
                            for i in range (6):
                                column_number_from_bottom_up = 5-i
                                if game_board[column_number_from_bottom_up][column] == "     ":
                                    game_board[column_number_from_bottom_up][column] = value
                                    break

                            # game_board[row][column] = value
                            show_game_board(game_board)
                            message = f"{game_board}".encode("utf-8")
                            client_connection.sendall(message)
                        else:
                            client_connection.sendall(b"IT IS NOT YOUR TURN. PLEASE WAIT")
                else:
                    break

    finally:
        client_connection.close()
        print(f"connection with {client_address} closed")
            
    
def show_game_board(game_board):
    print(f"The game board is: ")
    for row in game_board:
        print("\t" + f"{row}")
    print("\n")

def main():

    game_board = [
        ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
        , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
        , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
        , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
        , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
        , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
    ]


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))
        #listen for connections
        s.listen(2)
        print(f"Server listening on port {PORT}...")

        try:
            player_number = 0
            turn_counter = 0

            while True:
                
                client_connection, client_address = s.accept()
                # is_odd_player = not is_odd_player
                player_number += 1

                client_thread = threading.Thread(
                    target=handle_client
                    , args = (client_connection
                    , client_address
                    , game_board
                    , player_number
                    , turn_counter)
                    )
                
                client_thread.start()

        finally:
            s.close()
            print("Server socket closed")


if __name__ == "__main__":
    main()
