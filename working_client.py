"""

This is a copy of client.py that has been changed slightly (changes reverted) to make the program work

"""


# initially generated by chatGPT to help me learn the what is going on with this module. 
# Extensive modifications have been made my me on top of the skeleton ChatGPT created.

import socket
import os
import ast

HOST = '10.50.200.195'
# HOST = "localhost"
PORT = 80

PLAYER_NUMBER = 1

def game_board_to_list(string:str):
    return ast.literal_eval(string)

def send_message(my_socket:socket.socket, user_input:str, listen_for_response = True):
    #prep message
    bytes_message = (user_input).encode("utf-8")
    #send message
    my_socket.sendall(bytes_message)
    if listen_for_response:
        #get and print response
        data = my_socket.recv(1024)
        
        # if data != b"IT IS NOT YOUR TURN. PLEASE WAIT":
        return data.decode()

    
    else:
        return "not specified to listen for a response"

def show_game_board(game_board):
    print(f"The game board is: ")
    for row in game_board:
        print("\t" + f"{row}")
    print("\n")

def update_game_board(game_board:str):
    fixed_response = game_board_to_list(game_board)
    return fixed_response

def check_turn(s:socket.socket):
    operation_choice = "P"
    message = operation_choice + "Pinging the server"
    send_message(s, message)
    decoded_data = s.recv(1024).decode("utf-8")
    if decoded_data == "GO AHEAD":
        print("it IS your turn")
        return True
    elif decoded_data == "NOT YOUR TURN":
        print("it is NOT your turn")
        return False
    else:
        #an error?
        print("While sending a ping, we got an unrecognized response")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        #connect
        s.connect((HOST, PORT))
        game_board = []

        # go_ahead = s.recv(1024)

        operation_choice = "R"
        #get the game board/state
        message = operation_choice + ""
        response = send_message(s, message)
        game_board = update_game_board(response)
        show_game_board(game_board)

        # print(f"you are player number: {}")


        while True:

            #blocks input until server sends message to self
            # go_ahead = s.recv(1024)

            #get operation
            operation_choice = input("What do you want to do?\n\tI - initial connection (deprecated)\n\tR - request game board (deprecated)\n\tM - send move\n\tS - show game board (deprecated)\n\tT - terminate session\nYour Choice: ")
            
            # is_my_turn = check_turn(s)
            # if is_my_turn: dn_arror\t
            print("it is your turn")
                
            # Clearing the Screen
            # os.system('clear')
            print(f"You have chosen: {operation_choice}\n")

            if operation_choice == "I":

                # message = input("Type a message here: ")
                message = operation_choice + "connecting for the first time"
                send_message(s, message)

            # elif operation_choice == "P":
            #     message = operation_choice + "Pinging the server"
            #     send_message(s, message)

            elif operation_choice == "S":
                show_game_board(game_board)

            elif operation_choice == "R":
                #get the game board/state
                message = operation_choice + ""
                response = send_message(s, message)
                game_board = update_game_board(response)
                # print(f"Received:'{response}'\n")
                show_game_board(game_board)

            elif operation_choice == "M":
                show_game_board(game_board)
                # row = input("Enter the row to change: ")
                column = input("Enter the column to change: ")
                # value = input("Enter the value to insert: ")
                message = operation_choice + column
                response = send_message(s, message)

                #update own game board based on server copy
                game_board = update_game_board(response)
                show_game_board(game_board)


            elif operation_choice == "T":
                s.close()
                break
            # else:
            #     print("It is not your turn. Please wait for the other player")

            

if __name__ == "__main__":
    main()