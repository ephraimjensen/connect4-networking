game_board = [
    
[00000, 00000, 00000, 00000, 00000, 00000, 00000]
, [00000, 00000, 00000, 00000, 00000, 00000, 00000]
, [00000, 00000, 00000, 00000, 00000, 00000, 00000]
, [00000, 00000, 00000, 00000, 00000, 00000, 00000]
, [00000, 00000, 00000, 00000, 00000, 00000, 00000]
, [00000, 00000, 00000, 00000, 00000, 00000, 00000]
]

def show_game_board(game_board):
    print(f"The game board is: \n")
    print("\t===============================")
    for row in game_board:
        print("\t |", end="")
        for value in row:
            print(f" {value} |", end="")
        print("")
    print("\t===============================")
    print(""" column:   1   2   3   4   5   6   7""")    
    print("\n")

show_game_board(game_board)
"""
        a b c d e f g h i j k l m n o p q r s t u v w x y z

        A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

        | 0 0 0 0 0 0 0 |
        ~~~~~~~~~~~~~~~~~

        | 0 0 0 0 0 0 0 |
        =================
column:   1 2 3 4 5 6 7

        | 0 0 0 0 0 0 0 |
        _________________

"""