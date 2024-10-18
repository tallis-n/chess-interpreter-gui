from chess_visualisation import Chesspiece
from chess_visualisation import ChessBoard

chess_board = ChessBoard()
print(str(chess_board))
move = ""
while move != "exit":
    move = input("Enter Move: ")
    chess_board.update(move)
    print(str(chess_board))
print("Done! Thanks for your time")

