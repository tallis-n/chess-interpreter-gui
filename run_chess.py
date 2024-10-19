from chess_visualisation import Chesspiece
from chess_visualisation import ChessBoard
import tkinter as tk

chess_board = ChessBoard()
print(str(chess_board))
move = ""
while True:
    move = input("Enter Move: ")
    if move == "exit":
        break
    chess_board.update(move)
    print(str(chess_board))
print("Done! Thanks for your time")

