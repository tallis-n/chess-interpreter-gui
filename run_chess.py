from chess_visualisation import Chesspiece
from chess_visualisation import ChessBoard
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.constants import *


class ChessGUI:
    def __init__(self):
        self._type_to_img_dict = {'P': 'chess_images/LightPawn.png', 'B': 'chess_images/LightBishop.png',
                                  'R': 'chess_images/LightRook.png', 'Q': 'chess_images/LightQueen.png',
                                  'N': 'chess_images/LightKnight.png', 'K': 'chess_images/LightKing.png',
                                  'p': 'chess_images/DarkPawn.png', 'b': 'chess_images/DarkBishop.png',
                                  'r': 'chess_images/DarkRook.png', 'q': 'chess_images/DarkQueen.png',
                                  'n': 'chess_images/DarkKnight.png', 'k': 'chess_images/DarkKing.png'}
        self._chess_board = ChessBoard()
        self._chess_board_data = self._chess_board.return_data()

        self._window = tk.Tk()
        self._window.geometry("640x700")

        self._canvas = tk.Canvas(self._window)
        self._canvas.configure(width=640, height=640)
        self._canvas.pack()
        for i in range(0, 8):
            j = i + 1
            for k in range(0, 4):
                k1 = k
                if i % 2 != 0:
                    k1 = k + (1 / 2)
                self._canvas.create_rectangle(80 * j, 80 * (2 * k1 + 1), 80 * i, 80 * 2 * k1, fill="forest green")
        self.draw_pieces()
        self._move_text_box = tk.Text(self._window, height = 5, width = 40)
        self._move_text_box.pack(side=LEFT)
        self._button = tk.Button(self._window, text= "Submit", command = self.update_entry)
        self._button.pack(side=LEFT)
        self._window.bind('<Return>', (lambda event: self.update_entry()))
        self._window.mainloop()

    def draw_pieces(self):
        x, y = 0, 0
        self._images = []
        for i in range(0, 64):
            if self._chess_board_data[i] is not None:
                # supposed to put image into correct area here
                temp_type = self._chess_board_data[i].get_type()
                image = Image.open(self._type_to_img_dict[temp_type])
                resized_image = image.resize((80, 80))
                self._images.append(ImageTk.PhotoImage(resized_image))
                self._canvas.create_image(x + 40, y + 40, image=self._images[-1])
                self._canvas.pack()
            x += 80
            if x == 640:
                x = 0
                y += 80

    def update_entry_button_push(self, event):
        self.update_entry()

    def update_entry(self):
        move = self._move_text_box.get(1.0, "end-1c")
        self._move_text_box.delete("1.0", "end")
        self._chess_board.update(move)
        self.draw_pieces()


chess_gui = ChessGUI()
