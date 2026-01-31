import tkinter

# Game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# 🎨 Color palette
color_blue = "#3ecacb"        # Cyan for X
color_purple = "#9d4edd"      # Purple for O
color_yellow = "#f9c74f"      # Mustard yellow for winner text
color_gray = "#6a4c93"        # Deep purple background
color_light_gray = "#f28482"  # Salmon pink for winning tiles

turns = 0
game_over = False

def set_tile(row, column):
    global curr_player, game_over

    if game_over or board[row][column]["text"] != "":
        return

    board[row][column]["text"] = curr_player
    if curr_player == playerX:
        board[row][column].config(foreground=color_blue)
        curr_player = playerO
    else:
        board[row][column].config(foreground=color_purple)
        curr_player = playerX

    label["text"] = curr_player + "'s turn"
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # Horizontal
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return

    # Vertical
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return

    # Diagonal
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    # Anti-diagonal
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    # Tie
    if turns == 9:
        game_over = True
        label.config(text="It's a draw!", foreground=color_yellow)

def new_game():
    global turns, game_over, curr_player
    turns = 0
    game_over = False
    curr_player = playerX
    label.config(text=curr_player + "'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            bg_color = color_light_gray if (row + column) % 2 == 0 else color_gray
            board[row][column].config(text="", foreground=color_blue, background=bg_color)

# 🪟 Window setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.configure(bg=color_gray)
window.resizable(False, False)

frame = tkinter.Frame(window, bg=color_gray)

# Title banner
title = tkinter.Label(frame, text="TIC TAC TOE", font=("Consolas", 24, "bold"),
                      background=color_yellow, foreground="white", pady=10)
title.grid(row=0, column=0, columnspan=3, sticky="we")

# Status label
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20),
                      background=color_gray, foreground="white")
label.grid(row=1, column=0, columnspan=3, sticky="we")

# Game board buttons
for row in range(3):
    for column in range(3):
        bg_color = color_light_gray if (row + column) % 2 == 0 else color_gray
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=bg_color, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+2, column=column)

# Restart button
button = tkinter.Button(frame, text="RESET GAME", font=("Consolas", 20, "bold"),
                        background="#f94144", foreground=color_gray, command=new_game)
button.grid(row=5, column=0, columnspan=3, sticky="we", pady=10)

frame.pack()

# Center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
