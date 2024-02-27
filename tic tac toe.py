#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import messagebox

# Styling constants
BUTTON_FONT = ("Impact", 30)  # Define the font and font size
BUTTON_HEIGHT = 2  # Define button height
BUTTON_WIDTH = 5  # Define button width
BUTTON_PADX = 5
BUTTON_PADY = 5
GAME_FONT = ("Impact", 30)  # Define the font and font size for the game title
BUTTON_BG = "black"  # Set button background color to black
BUTTON_FG = "white"  # Set button text color to white

Player1 = 'X'
stop_game = False

# Function to handle button clicks
def clicked(r, c):
    global Player1

    # Check if the button is not already clicked and the game is not over
    if states[r][c] == 0 and not stop_game:
        if Player1 == 'X':
            # Configure the button with 'X' and update styling
            b[r][c].configure(text="X", state=DISABLED, font=BUTTON_FONT, bg=BUTTON_BG, fg=BUTTON_FG)
            states[r][c] = 'X'
            Player1 = 'O'
        elif Player1 == 'O':
            # Configure the button with 'O' and update styling
            b[r][c].configure(text='O', state=DISABLED, font=BUTTON_FONT, bg=BUTTON_BG, fg=BUTTON_FG)
            states[r][c] = 'O'
            Player1 = 'X'

        # Check if a player has won
        check_if_win()

# Function to check if a player has won
def check_if_win():
    global stop_game

    # Check rows and columns for a win
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            stop_game = True
            winner = messagebox.showinfo("Winner", states[i][0] + " Won")
            return

    for i in range(3):
        if states[0][i] == states[1][i] == states[2][i] != 0:
            stop_game = True
            winner = messagebox.showinfo("Winner", states[0][i] + " Won")
            return

    # Check diagonals for a win
    if states[0][0] == states[1][1] == states[2][2] != 0:
        stop_game = True
        winner = messagebox.showinfo("Winner", states[0][0] + " Won")

    if states[0][2] == states[1][1] == states[2][0] != 0:
        stop_game = True
        winner = messagebox.showinfo("Winner", states[0][2] + " Won")

    # Check if it's a tie
    if all(cell != 0 for row in states for cell in row) and not stop_game:
        stop_game = True
        messagebox.showinfo("Tie", "It's a Tie!")

# Create the main Tkinter window
root = Tk()
root.title("Tic Tac Toe")
root.resizable(0, 0)

# Create a frame for the buttons
button_frame = Frame(root)
button_frame.grid(row=1, column=0, padx=20, pady=20)

# Create buttons and initialize game state
b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(
            button_frame,
            text="",
            font=BUTTON_FONT,
            height=BUTTON_HEIGHT,
            width=BUTTON_WIDTH,
            command=lambda r=i, c=j: clicked(r, c),
            bg=BUTTON_BG,
            fg=BUTTON_FG,
        )
        b[i][j].grid(row=i, column=j, padx=BUTTON_PADX, pady=BUTTON_PADY)

# Create a label for the game title
game_label = Label(root, text="Tic Tac Toe", font=GAME_FONT)
game_label.grid(row=0, column=0)

# Start the main event loop
root.mainloop()


# In[ ]:





# In[ ]:




