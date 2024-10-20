from chess_visualisation import Chesspiece
from chess_visualisation import ChessBoard

game1 = "1. e4 e6 2. d4 d5 3. Nd2 Nc6 4. Ngf3 Nh6 5. e5 f6 6. Bb5 Bd7 7. Bxc6 Bxc6 8. Nb3 Nf7 9. Bf4 f5 10. h4 Be7 11. Qd2 b6 12. c3 Bb7 13. Be3 Qd7 14. Nc1 Ba6 15. Rh3 Qb5 16. Ne2 Qxe2+ 17. Qxe2 Bxe2 18. Kxe2 O-O-O 19. Ng5 Nxg5 20. hxg5 Rdf8 21. g3 g6 22. Rh6 Rf7 23. Rah1 Rg7 24. Kf3 Kd7 25. g4 fxg4+ 26. Kxg4 Ke8 27. b4 a6 28. a4 Kd7 29. b5 a5 30. c4 dxc4 31. Rc1 Re8 32. Rxc4 Bd8 33. Kf4 Ree7 34. Ke4 Rgf7 35. Rc6 Rg7 36. d5 exd5+ 37. Kxd5 Re8 38. e6+ Kc8 39. Bd4"
game1formatted = game1.split(" ")
chess_board = ChessBoard()
i = 2
for item in game1formatted:
    if item[-1] == '.':
        continue
    print(str(i // 2) + "." + item)
    i += 1
    chess_board.update(item)
    print(str(chess_board))
