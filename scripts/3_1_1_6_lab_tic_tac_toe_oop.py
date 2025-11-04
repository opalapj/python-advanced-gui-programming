import tkinter as tk
from random import choice
from tkinter import messagebox as msg


class TicTacToe:
    def __init__(self, mode, player0, player1=None):
        self.mode = mode
        self.players = [
            [player0, "O", "green"],
            [player1 if self.mode == 0 else "Comp", "X", "red"],
        ]
        self.root = tk.Tk()
        self.tiles = []
        for r in range(3):
            self.tiles.append([])
            for c in range(3):
                button = tk.Button(self.root, width=4, font=("Arial", 30, "bold"))
                button.grid(row=r, column=c)
                button.bind("<ButtonRelease-1>", self.user_turn)
                self.tiles[r].append(button)
        if self.mode:
            self.turn = self.players[1]
            self.make_sign(self.tiles[1][1])
        else:
            self.turn = self.players[1]
        self.root.mainloop()

    def comp_turn(self):
        tile_rc = choice(self.free_tiles())
        self.make_sign(self.tiles[tile_rc[0]][tile_rc[1]])

    def user_turn(self, event=None):
        if event.widget["text"] == "":
            self.make_sign(event.widget)

    def make_sign(self, tile):
        tile.config(text=self.turn[1], fg=self.turn[2], activeforeground=self.turn[2])
        winner = self.win()
        if winner:
            msg.showinfo(
                title="Game over!",
                message="There could be only one winner - {}!".format(winner),
            )
            self.root.destroy()
        elif not self.free_tiles():
            msg.showinfo(title="Game over!", message="Tie!")
            self.root.destroy()
        elif self.mode and self.turn[0] == "Comp":
            self.turn = self.players[0]
        elif self.mode and self.turn[0] != "Comp":
            self.turn = self.players[1]
            self.comp_turn()
        else:
            self.turn = (
                self.players[1] if self.turn == self.players[0] else self.players[0]
            )

    def free_tiles(self):
        free_tiles_list = []
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c]["text"] == "":
                    free_tiles_list.append((r, c))
        return free_tiles_list

    def win(self):
        for i in range(3):
            if (
                self.tiles[i][0]["text"]
                == self.tiles[i][1]["text"]
                == self.tiles[i][2]["text"]
                == self.turn[1]
            ):
                return self.turn[0]
            if (
                self.tiles[0][i]["text"]
                == self.tiles[1][i]["text"]
                == self.tiles[2][i]["text"]
                == self.turn[1]
            ):
                return self.turn[0]
        if (
            self.tiles[0][0]["text"]
            == self.tiles[1][1]["text"]
            == self.tiles[2][2]["text"]
            == self.turn[1]
        ):
            return self.turn[0]
        if (
            self.tiles[0][2]["text"]
            == self.tiles[1][1]["text"]
            == self.tiles[2][0]["text"]
            == self.turn[1]
        ):
            return self.turn[0]
        return


# Modes: 0. user vs user, 1. user vs comp.
# app = TicTacToe(0, 'Piotrek', 'Karolina')
app = TicTacToe(1, "Piotrek")
