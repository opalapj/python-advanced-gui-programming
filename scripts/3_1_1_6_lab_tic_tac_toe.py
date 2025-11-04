import tkinter as tk
from random import choice
from tkinter import messagebox as msg


def comp_turn():
    tile_rc = choice(free_tiles())
    make_sign(tiles[tile_rc[0]][tile_rc[1]])


def user_turn(event=None):
    if event.widget["text"] == "":
        make_sign(event.widget)


def make_sign(tile):
    global turn
    tile.config(text=turn[1], fg=turn[2], activeforeground=turn[2])
    winner = win()
    if winner:
        msg.showinfo(
            title="Game over!",
            message="There could be only one winner - {}!".format(winner),
        )
        root.destroy()
    elif not free_tiles():
        msg.showinfo(title="Game over!", message="Tie!")
        root.destroy()
    elif mode and turn[0] == "Comp":
        turn = players[0]
    elif mode and turn[0] != "Comp":
        turn = players[1]
        comp_turn()
    else:
        turn = players[1] if turn == players[0] else players[0]


def free_tiles():
    free_tiles_list = []
    for r in range(3):
        for c in range(3):
            if tiles[r][c]["text"] == "":
                free_tiles_list.append((r, c))
    return free_tiles_list


def win():
    for i in range(3):
        if tiles[i][0]["text"] == tiles[i][1]["text"] == tiles[i][2]["text"] == turn[1]:
            return turn[0]
        if tiles[0][i]["text"] == tiles[1][i]["text"] == tiles[2][i]["text"] == turn[1]:
            return turn[0]
    if tiles[0][0]["text"] == tiles[1][1]["text"] == tiles[2][2]["text"] == turn[1]:
        return turn[0]
    if tiles[0][2]["text"] == tiles[1][1]["text"] == tiles[2][0]["text"] == turn[1]:
        return turn[0]
    return


# Modes: 0. user vs user, 1. user vs comp.
mode = 0
player0 = "Piotrek"
player1 = "Karolina"
players = [[player0, "O", "green"], [player1 if mode == 0 else "Comp", "X", "red"]]
root = tk.Tk()
tiles = []
for r in range(3):
    tiles.append([])
    for c in range(3):
        button = tk.Button(root, width=4, font=("Arial", 30, "bold"))
        button.grid(row=r, column=c)
        button.bind("<ButtonRelease-1>", user_turn)
        tiles[r].append(button)
if mode:
    turn = players[1]
    make_sign(tiles[1][1])
else:
    turn = players[1]
root.mainloop()
