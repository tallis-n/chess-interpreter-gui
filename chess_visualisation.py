class Chesspiece:
    def __init__(self, type: str, x: str, y: int):
        self._type = type
        self._x = x
        self._y = y
        self._can_move_twice = False
        if self._type == 'P' or self._type == 'p':
            self._can_move_twice = True

    def __str__(self):
        return self._type

    def get_pos(self):
        return self._x, self._y

    def get_type(self):
        return self._type

    def move_twice(self):
        return self._can_move_twice

    def update_move_twice(self):
        self._can_move_twice = False

    def promote(self, **kwargs):
        valid = False
        type = kwargs('type')
        while not valid:
            if type is None:
                type = input("What type would you like to promote to? ")
            if type.upper() == 'N' or type.upper() == 'R' or type.upper() == 'Q' or type.upper() == 'B':
                valid = True
            else:
                type = None
                print("Type invalid, try again.")
        self._type = type


class ChessBoard:
    def __init__(self):
        # each item in self._data represents 1 square
        # starts from the top left
        self._data = [None] * 64
        self._data[0], self._data[7] = Chesspiece('r', 'a', 8), Chesspiece('r', 'h', 8)
        self._data[1], self._data[6] = Chesspiece('n', 'b', 8), Chesspiece('n', 'g', 8)
        self._data[2], self._data[5] = Chesspiece('b', 'c', 8), Chesspiece('b', 'f', 8)
        self._data[3] = Chesspiece('q', 'd', 8)
        self._data[4] = Chesspiece('k', 'e', 8)
        self._alpheb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for i in range(0, 8):
            self._data[8 + i] = Chesspiece('p', self._alpheb[i], 7)
        self._data[63], self._data[56] = Chesspiece('R', 'h', 1), Chesspiece('R', 'a', 1)
        self._data[62], self._data[57] = Chesspiece('N', 'g', 1), Chesspiece('N', 'b', 1)
        self._data[61], self._data[58] = Chesspiece('B', 'f', 1), Chesspiece('B', 'c', 1)
        self._data[59] = Chesspiece('Q', 'd', 1)
        self._data[60] = Chesspiece('K', 'e', 1)
        for i in range(0, 8):
            self._data[48 + i] = Chesspiece('P', self._alpheb[i], 2)
        # determines whose turn it is
        self._turn = -1
        self._knight_pos_array = [-17, -15, -10, -6, 6, 10, 15, 17]
        self._check = False

    def __str__(self):
        return_string = '  a b c d e f g h  \n'
        for i in range(0, 8):
            return_string += str(8 - i)
            for k in range(0, 8):
                return_string += ' '
                if self._data[i * 8 + k] is None:
                    return_string += "."
                else:
                    return_string += str(self._data[i * 8 + k])
            return_string += '\n'
        return return_string

    def alpha2absolute_coord(self, coord: tuple):
        abs_coord = 0
        for i in range(0, len(self._alpheb)):
            if coord[0] == self._alpheb[i]:
                abs_coord += i
        abs_coord += (8 - coord[1]) * 8
        return abs_coord

    def update(self, move: str):
        # pawn movement, excluding captures
        if len(move) == 2 or (len(move) == 3 and move[0].upper() == 'P'):
            index_to = self.alpha2absolute_coord((move[-2], int(move[-1])))
            if self._turn == -1:
                one_away_index = self.alpha2absolute_coord((move[-2], int(move[-1]) - 1))
                two_away_index = self.alpha2absolute_coord((move[-2], int(move[-1]) - 2))
                one_away = self._data[one_away_index]
                two_away = self._data[two_away_index]
            elif self._turn == 1:
                one_away_index = self.alpha2absolute_coord((move[-2], int(move[-1]) + 1))
                two_away_index = self.alpha2absolute_coord((move[-2], int(move[-1]) + 2))
                one_away = self._data[one_away_index]
                two_away = self._data[two_away_index]
            if one_away is None and two_away is None:
                print("Move is illegal")
                return
            elif one_away is not None:
                if one_away.get_type() == 'P' or one_away.get_type() == 'p':
                    one_away.update_move_twice()
                    self._data[index_to] = self._data[one_away_index]
                    self._data[one_away_index] = None
                else:
                    print("Move is illegal")
                    return
            elif two_away is not None:
                if two_away.move_twice():
                    two_away.update_move_twice()
                    self._data[index_to] = self._data[two_away_index]
                    self._data[two_away_index] = None
                else:
                    print("Move is illegal")
                    return
        # handle knight movement, including captures
        if move[0].upper() == "N":
            index_to = self.alpha2absolute_coord((move[-2], int(move[-1])))
            if self._data[index_to] is not None:
                if self._turn == -1 and self._data[index_to].get_type().isupper():
                    print("Cannot capture your own piece!")
                    return
                if self._turn == 1 and self._data[index_to].get_type().islower():
                    print("Cannot capture your own piece!")
                    return
            moved = False
            for ele in self._knight_pos_array:
                item = index_to + ele
                piece_at = self._data[item]
                if (item >=0 and item <= 63) and piece_at is not None:
                    if self._turn == -1 and piece_at.get_type() == "N":
                        self._data[index_to] = piece_at
                        self._data[item] = None
                        moved = True
                        break
                    elif self._turn == 1 and piece_at.get_type() == "n":
                        self._data[index_to] = piece_at
                        self._data[item] = None
                        moved = True
                        break
            if moved == False:
                print("Move is illegal")
                return
        # handle rook movement, including captures
        if move[0].upper() == "R":
            index_to = self.alpha2absolute_coord((move[-2], int(move[-1])))
            moved = False
            if self._data[index_to] is not None:
                if self._turn == -1 and self._data[index_to].get_type().isupper():
                    print("Cannot capture your own piece!")
                    return
                if self._turn == 1 and self._data[index_to].get_type().islower():
                    print("Cannot capture your own piece!")
                    return
            # find position of rook and handle collisions
            index_at = self.check_rook_movement(index_to, "Q")
            if index_at != -1:
                self._data[index_to] = self._data[index_at]
                self._data[index_at] = None
                moved = True
            if moved == False:
                print("You haven't moved! Invalid Move!")
                return
        # handle bishop movement, including captures, so much recycled code
        if move[0].upper() == "B":
            index_to = self.alpha2absolute_coord((move[-2], int(move[-1])))
            moved = False
            if self._data[index_to] is not None:
                if self._turn == -1 and self._data[index_to].get_type().isupper():
                    print("Cannot capture your own piece!")
                    return
                if self._turn == 1 and self._data[index_to].get_type().islower():
                    print("Cannot capture your own piece!")
                    return
            # find position of bishop and handle collisions
            index_at = self.check_bishop_movement(index_to, "B")
            if index_at != -1:
                self._data[index_to] = self._data[index_at]
                self._data[index_at] = None
                moved = True
            if moved == False:
                print("You haven't moved! Invalid Move!")
                return
        # handle queen movement, including captures, even more recycled code
        if move[0].upper() == "Q":
            index_to = self.alpha2absolute_coord((move[-2], int(move[-1])))
            moved = False
            if self._data[index_to] is not None:
                if self._turn == -1 and self._data[index_to].get_type().isupper():
                    print("Cannot capture your own piece!")
                    return
                if self._turn == 1 and self._data[index_to].get_type().islower():
                    print("Cannot capture your own piece!")
                    return
            # position of queen - rook direction
            index_at = self.check_rook_movement(index_to, "Q")
            if index_at != -1:
                self._data[index_to] = self._data[index_at]
                self._data[index_at] = None
                moved = True
            # position of queen - bishop direction
            index_at = self.check_bishop_movement(index_to, "Q")
            if index_at != -1:
                self._data[index_to] = self._data[index_at]
                self._data[index_at] = None
                moved = True
            # if move has not occurred
            if moved == False:
                print("You haven't moved! Invalid Move!")
                return
        # handle pawn captures
        if len(move) == 4:
            possible_first_chars = ["P", "a", "b", "c", "d", "e", "f", "g", "h"]
            valid = False
            for item in possible_first_chars:
                if move[0] == item:
                    valid = True
                    break
            if valid == False :
                print("Invalid Move!")
                return
            index_to = self.alpha2absolute_coord((move[-2], int(move[-1])))
            # this doesn't work with doubled pawns in some cases - handle later
            if move[0] < move[2] or move[0].upper() == "P":
                cur_check = index_to + 7
                if self._data[cur_check] is not None:
                    if (self._data[cur_check].get_type() == "P" and self._turn == -1) or self._data[cur_check].get_type() == "p" and self._turn == 1:
                        self._data[index_to] = self._data[cur_check]
                        self._data[cur_check] = None
                cur_check = index_to - 1
                if self._data[cur_check] is not None:
                    if (self._data[cur_check].get_type() == "P" and self._turn == -1) or self._data[cur_check].get_type() == "p" and self._turn == 1:
                        self._data[index_to] = self._data[cur_check]
                        # en passant factor!
                        self._data[index_to + 8 * self._turn] = None
                        self._data[cur_check] = None
            else:
                cur_check = index_to - 7
                if self._data[cur_check] is not None:
                    if (self._data[cur_check].get_type() == "P" and self._turn == -1) or self._data[cur_check].get_type() == "p" and self._turn == 1:
                        self._data[index_to] = self._data[cur_check]
                        self._data[cur_check] = None
                cur_check = index_to + 1
                if self._data[cur_check] is not None:
                    if (self._data[cur_check].get_type() == "P" and self._turn == -1) or self._data[cur_check].get_type() == "p" and self._turn == 1:
                        self._data[index_to] = self._data[cur_check]
                        # en passant factor!
                        self._data[index_to + 8 * self._turn] = None
                        self._data[cur_check] = None
        elif len(move) > 4 and moved == False:
            print("Move is illegal")
            return
        self._turn *= -1

        def check_bishop_movement(self, index_to, type_of):
            i = 0
            factor = -7
            while i < 4:
                factor *= -1
                if i == 2:
                    factor = 9
                check_index = index_to + factor
                while self._data[check_index] is None and check_index >= 0 and check_index <= 63:
                    check_index += factor
                if check_index < 0 or check_index > 63:
                    i += 1
                    continue
                if (self._data[check_index].get_type() == type_of and self._turn == -1) or (self._data[check_index].get_type() == type_of.lower() and self._turn == 1):
                    return check_index
                else:
                    i += 1
                    continue
            return -1
        
        def check_rook_movement(self, index_to, type_of):
            i = 0
            factor = -1
            while i < 4:
                factor *= -1
                if i == 2:
                    factor *= 8
                check_index = index_to + factor
                while self._data[check_index] is None and check_index >= 0 and check_index <= 63:
                    check_index += factor
                if check_index < 0 or check_index > 63:
                    i += 1
                    continue
                if (self._data[check_index].get_type() == type_of and self._turn == -1) or (self._data[check_index].get_type() == type_of.lower() and self._turn == 1):
                    return check_index
                else:
                    i += 1
                    continue
            return -1
