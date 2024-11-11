from chess_visualisation import Chesspiece
from chess_visualisation import ChessBoard

b = ChessBoard()
b.update("e4")
b.update("e5")
b.update("f4")
b.update("qh4")
print(str(b))
b.update("kf2")
print(str(b))
b.update("g3")
print(str(b))
