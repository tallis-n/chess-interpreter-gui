from chess_visualisation import Chesspiece
from chess_visualisation import ChessBoard

b = ChessBoard()
b.update("e4")
b.update("e5")
b.update("bc4")
b.update("nf6")
print(str(b))
b.update("nf3")
print(str(b))
b.update("g6")
b.update("O-O")
print(str(b))
