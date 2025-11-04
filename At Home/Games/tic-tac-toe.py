import random
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama for colored output

# ASCII art title
TITLE = f"""
{Fore.CYAN}
 _______ _        _______           _______         
|__   __(_)      |__   __|         |__   __|        
   | |   _  ___     | | __ _  ___     | | ___   ___ 
   | |  | |/ __|    | |/ _` |/ __|    | |/ _ \ / _ \\
   | |  | | (__     | | (_| | (__     | | (_) |  __/
   |_|  |_|\___|    |_|\__,_|\___|    |_|\___/ \___|
{Style.RESET_ALL}
"""

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player_name, board):
    while True:
        try:
            print(f"{Fore.YELLOW}{player_name}'s turn.{Style.RESET_ALL}")
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if row not in range(3) or col not in range(3):
                print(f"{Fore.RED}Invalid position. Try again.{Style.RESET_ALL}")
                continue
            if board[row][col] != " ":
                print(f"{Fore.RED}Cell already taken. Try again.{Style.RESET_ALL}")
                continue
            return row, col
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")

def bot_move(board):
    # Simple bot: random empty cell
    empty_cells = [(r,c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def tic_tac_toe():
    print(TITLE)
    p1_name = input("Enter Player 1 name: ").strip() or "Player 1"
    mode = ""
    while mode not in ["1", "2"]:
        mode = input("Play vs (1) Friend or (2) Bot? Enter 1 or 2: ").strip()

    if mode == "1":
        p2_name = input("Enter Player 2 name: ").strip() or "Player 2"
    else:
        p2_name = "Bot"

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    player_names = { "X": p1_name, "O": p2_name }

    while True:
        print_board(board)

        if mode == "2" and current_player == "O":
            print(f"{Fore.MAGENTA}{p2_name} is thinking...{Style.RESET_ALL}")
            row, col = bot_move(board)
        else:
            row, col = get_move(player_names[current_player], board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"{Fore.GREEN}🎉 {player_names[current_player]} ({current_player}) wins! Congratulations! 🎉{Style.RESET_ALL}")
            break

        if is_board_full(board):
            print_board(board)
            print(f"{Fore.BLUE}It's a tie! Well played both!{Style.RESET_ALL}")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
