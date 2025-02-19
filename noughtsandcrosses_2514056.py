""" Importing random, os.path and json """
import random
import os.path
import json

random.seed()

def draw_board(board):
    """ developing a code to draw the board for the noughts and crosses """
    print(" ----------- ")
    for row in board:
        print(f"| {' | '.join(row)} |")
        print(" ----------- ")

def welcome(board):
    """ printing the welcome message and displaying the board """
    print("Welcome to the 'Unbeatable Noughts and Crosses' game.")
    print("The board layout is show below:")
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")

def initialise_board(board):
    """ developing a code to set all elements of the board to one space ' ' """
    return [[" " for i in range(3)] for j in range(3)]

def get_player_move(board):
    """ developing a code to ask the user for the cell to put the X in, 
    and return row and col """
    while True:
        try:
            move = int(input("Choose your square (1-9): "))
            if 1 <= move <= 9:
                row = (move-1)//3
                col = (move-1)%3
                if board[row][col] == " ":
                    return row, col
                else:
                    print("Cell already occupied. Try again.")
            else:
                print("Invalid move. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

def choose_computer_move(board):
    """ developing a code to let the computer chose a cell to put a nought in
    and return row and col """
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def check_for_win(board, mark):
    """ developing a code to check if either the player or the computer has won
    if someone won return True, otherwise False """
    for i in range(3):
        if all(cell == mark for cell in board[i]):# Check rows
            return True
        if all(board[j][i] == mark for j in range(3)):# Check columns
            return True
    if all(board[i][i] == mark for i in range(3)):# Check diagonals
        return True
    if all(board[i][2-i] == mark for i in range(3)):# Check anti-diagonals
        return True
    return False

def check_for_draw(board):
    """ develop cope to check if all cells are occupied
    return True if it is, False otherwise """
    for row in board:
        if " " in row:
            return False
    return True

def play_game(board):
    """ developing a code to play the Noughts and Crosses game """
    board = initialise_board(board)
    draw_board(board)
    while True:
        # Player's move
        row, col = get_player_move(board)
        board[row][col] = "X"
        draw_board(board)
        if check_for_win(board, "X"):
            print("Congratulations! You won!")
            return 1
        if check_for_draw(board):
            print("It's a draw!")
            return 0

        # Computer's move
        print("Computer's turn...")
        row, col = choose_computer_move(board)
        board[row][col] = "O"
        draw_board(board)
        if check_for_win(board, "O"):
            print("Computer wins! Better luck next time.")
            return -1
        if check_for_draw(board):
            print("It's a draw!")
            return 0

def menu():
    """ Displaying the menu and getting user input of either  '1', '2', '3' or 'q'
    1 - Play the game
    2 - Save score in file 'leaderboard.txt'
    3 - Load and display the scores from the 'leaderboard.txt'
    q - End the program """
    while True:
        print("Enter one of the following options:")
        print("1 - Play the game")
        print("2 - Save score in file 'leaderboard.txt'")
        print("3 - Load and display the scores from the 'leaderboard.txt'")
        print("q - End the program")

        choice = input("Enter your choice (1, 2, 3, or q): ").strip().lower()
        if choice in ['1', '2', '3', 'q']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def load_scores():
    """ Developing a code to load the leaderboard scores from the file 'leaderboard.txt' """
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return {}

def save_score(score):
    """ developing a code to ask the player for their name
    and then save the current score to the file 'leaderboard.txt' """
    name = input("Ënter your name: ").strip()
    leader_board = load_scores()
    leader_board[name] = score
    with open ("leaderboard.txt", "w", encoding="utf-8") as file:
        json.dump(leader_board, file)
    print(f"Score saved for {name}.")

def display_leaderboard(leaders):
    """ developing a code to display the leaderboard scores """
    leader_board = load_scores()
    if leader_board:
        print("Leaderboard:")
        print("-------------")
        for name, score in leader_board.items():
            print(f"{name}: {score}")
    else:
        print("No scores found in the leaderboard.")
