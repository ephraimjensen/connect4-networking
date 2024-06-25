import ast

# # Original string representation of the list
# str_list = "[1, 2, 3, 4]"

# # Convert string to list
# a_list = ast.literal_eval(str_list)
# game_board = [
#       ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
#     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
#     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
#     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
#     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
#     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
# ]
# print(a_list)  # Output: [1, 2, 3, 4]


def change_matrix(game_board):
    game_board[0][0] = 1
    print(game_board)

def show_game_board(game_board):
    print(f"The game board is: ")
    for row in game_board:
        print("\t" + f"{row}")
    print("\n")

def str_to_list(string:str):
    return ast.literal_eval(string)

def main():
    game_board = [
        [0, 0, 0, 0, 0, 0, 0]
        , [0, 0, 0, 0, 0, 0, 0]
        , [0, 0, 0, 0, 0, 0, 0]
        , [0, 0, 0, 0, 0, 0, 0]
        , [0, 0, 0, 0, 0, 0, 0]
        , [0, 0, 0, 0, 0, 0, 0]
    ]
    # a_list = []
    # str_list = f"{a_list}"
    str_gb = f"{game_board}"


    list_game_board = str_to_list(str_gb)
    list_game_board[5][3] = 9
    show_game_board(list_game_board)


main()


# for row in rows:
#     for column in columns:
#         pass
#         # if in corner
#         # if in row
#         # if in column


    # game_board = [
    #       [00000, 00000, 00000, 00000, 00000, 00000, 00000]
    #     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
    #     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
    #     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
    #     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
    #     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
    # ]
