# # import ast

# # # # Original string representation of the list
# # # str_list = "[1, 2, 3, 4]"

# # # # Convert string to list
# # # a_list = ast.literal_eval(str_list)
# # # game_board = [
# # #       ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
# # #     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
# # #     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
# # #     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
# # #     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
# # #     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
# # # ]
# # # print(a_list)  # Output: [1, 2, 3, 4]


# # def change_matrix(game_board):
# #     game_board[0][0] = 1
# #     print(game_board)

# # def show_game_board(game_board):
# #     print(f"The game board is: ")
# #     for row in game_board:
# #         print("\t" + f"{row}")
# #     print("\n")

# # def str_to_list(string:str):
# #     return ast.literal_eval(string)

# # def main():
# #     game_board = [
# #         [0, 0, 0, 0, 0, 0, 0]
# #         , [0, 0, 0, 0, 0, 0, 0]
# #         , [0, 0, 0, 0, 0, 0, 0]
# #         , [0, 0, 0, 0, 0, 0, 0]
# #         , [0, 0, 0, 0, 0, 0, 0]
# #         , [0, 0, 0, 0, 0, 0, 0]
# #     ]
# #     # a_list = []
# #     # str_list = f"{a_list}"
# #     str_gb = f"{game_board}"

# #     for row in (game_board):
# #         for column in row:
# #             print(column)


# #     # list_game_board = str_to_list(str_gb)
# #     # list_game_board[5][3] = 9
# #     # show_game_board(list_game_board)


# # main()


# # # for row in rows:
# # #     for column in columns:
# # #         pass
# # #         # if in corner
# # #         # if in row
# # #         # if in column


#     # game_board = [
#     #         [00000, 00000, 00000, 00000, 00000, 00000, 00000]
#     #     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
#     #     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
#     #     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
#     #     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
#     #     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
#     # ]


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
    
             


game_board = [
      [0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 2, 0]
    , [0, 0, 0, 0, 2, 0, 0]
    , [0, 0, 0, 1, 2, 0, 0]
    , [0, 0, 0, 1, 2, 0, 0]
    , [0, 0, 0, 1, 2, 0, 0]
]

print(check_4_in_row(game_board)) #F

# game_board = [
#       [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 1]
#     , [0, 0, 0, 0, 0, 1, 0]
#     , [0, 0, 0, 0, 1, 0, 0]
#     , [0, 0, 0, 1, 0, 0, 0]
# ]

# print(check_4_in_row(game_board))#true

# game_board = [
#       [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [1, 1, 1, 1, 0, 0, 0]
# ]

# print(check_4_in_row(game_board))#true

# game_board = [
#       [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [1, 0, 0, 0, 0, 0, 0]
#     , [1, 0, 0, 0, 0, 0, 0]
#     , [1, 0, 0, 0, 0, 0, 0]
#     , [1, 0, 0, 0, 0, 0, 0]
# ]

# print(check_4_in_row(game_board)) #True
# game_board = [
#       [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [1, 0, 0, 0, 0, 0, 0]
#     , [1, 0, 0, 0, 0, 0, 0]
#     , [1, 0, 0, 0, 0, 0, 0]
# ]
# print(check_4_in_row(game_board)) #false
# game_board = [
#       [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [1, 0, 0, 0, 0, 0, 0]
#     , [1, 0, 0, 0, 0, 0, 0]
#     , [1, 0, 0, 0, 0, 0, 0]
# ]
# print(check_4_in_row(game_board))#False
# game_board = [
#       [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 1]
#     , [1, 0, 0, 0, 0, 0, 1]
#     , [1, 0, 0, 0, 0, 0, 1]
#     , [1, 0, 0, 0, 0, 0, 1]
# ]

# print(check_4_in_row(game_board))#true
# game_board = [
#       [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [0, 0, 0, 0, 0, 0, 0]
#     , [1, 0, 0, 0, 0, 0, 0]
#     , [1, 0, 0, 0, 0, 1, 1]
#     , [1, 1, 1, 0, 1, 1, 0]
# ]
# print(check_4_in_row(game_board))#false

# import ast

# def game_board_to_list(string:str):
#     # print(string)
#     return ast.literal_eval(string)

# game_board = [
#         [00000, 00000, 00000, 00000, 00000, 00000, 00000]
#     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
#     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
#     , [00000, 00000, 00000, 65481, 00000, 00000, 00000]
#     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
#     , [00000, 00000, 00000, 00000, 00000, 00000, 00000]
# ]
# # gb = repr(game_board)
# gb = f"{game_board}"

# print("ints")
# # print(game_board)
# print(game_board_to_list(gb))


# game_board = [
#       ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
#     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
#     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
#     , ["     ", "     ", "     ", "32153", 12341, "     ", "     "]
#     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
#     , ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
# ]

# def game_board_to_list(string:str):
#     # print(string)
#     return ast.literal_eval(string)

# # gb = repr(game_board)
# gb = f"{game_board}"

# print("strings")
# # print(gb)
# print(game_board_to_list(gb))