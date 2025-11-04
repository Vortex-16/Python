import random
import time
from colorama import Fore, Style, init
import platform

# winsound is Windows-only; import safely
if platform.system() == "Windows":
    import winsound
else:
    winsound = None

init(autoreset=True)

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

def available_moves(board):
    return [(r,c) for r in range(3) for c in range(3) if board[r][c] == " "]

def minimax(board, is_maximizing, player, opponent):
    if check_winner(board, player):
        return 1
    elif check_winner(board, opponent):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for (r,c) in available_moves(board):
            board[r][c] = player
            score = minimax(board, False, player, opponent)
            board[r][c] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for (r,c) in available_moves(board):
            board[r][c] = opponent
            score = minimax(board, True, player, opponent)
            board[r][c] = " "
            best_score = min(score, best_score)
        return best_score

def bot_move_minimax(board, bot_player, human_player):
    best_score = -float('inf')
    best_move = None
    for (r,c) in available_moves(board):
        board[r][c] = bot_player
        score = minimax(board, False, bot_player, human_player)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            best_move = (r,c)
    return best_move

def bot_move_random(board):
    return random.choice(available_moves(board))

def bot_move_medium(board, bot_player, human_player):
    # 50% chance random, 50% minimax
    if random.random() < 0.5:
        return bot_move_random(board)
    else:
        return bot_move_minimax(board, bot_player, human_player)

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

def celebrate():
    celebration_frames = [
        f"{Fore.MAGENTA}🎉🎊 Congratulations! 🎊🎉{Style.RESET_ALL}",
        f"{Fore.CYAN}✨🎉 You Won! 🎉✨{Style.RESET_ALL}",
        f"{Fore.YELLOW}🥳 Keep it up! 🥳{Style.RESET_ALL}",
        f"{Fore.GREEN}🎈🎉🎉🎈{Style.RESET_ALL}"
    ]
    for _ in range(5):
        for frame in celebration_frames:
            print("\r" + frame, end="", flush=True)
            time.sleep(0.4)
    print("\n")

def play_sound():
    if winsound:
        freq = 1000  # Frequency in Hz
        duration = 300  # Duration in ms
        for _ in range(5):
            winsound.Beep(freq, duration)
            time.sleep(0.1)

def play_game(p1_name, p2_name, mode, difficulty):
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    player_names = { "X": p1_name, "O": p2_name }

    while True:
        print_board(board)

        moves = available_moves(board)
        # Auto fill last box
        if len(moves) == 1:
            row, col = moves[0]
            print(f"{Fore.MAGENTA}Auto-filling last box at row {row+1}, col {col+1}!{Style.RESET_ALL}")
            time.sleep(1)
        else:
            if mode == "2" and current_player == "O":
                print(f"{Fore.MAGENTA}{p2_name} is thinking...{Style.RESET_ALL}")
                if difficulty == "easy":
                    row, col = bot_move_random(board)
                elif difficulty == "medium":
                    row, col = bot_move_medium(board, "O", "X")
                else:  # hard
                    row, col = bot_move_minimax(board, "O", "X")
            else:
                row, col = get_move(player_names[current_player], board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"{Fore.GREEN}🎉 {player_names[current_player]} ({current_player}) wins! Congratulations! 🎉{Style.RESET_ALL}")
            celebrate()
            if winsound:
                play_sound()
            return current_player  # return winner

        if is_board_full(board):
            print_board(board)
            print(f"{Fore.BLUE}It's a tie! Well played both!{Style.RESET_ALL}")
            return "Tie"

        current_player = "O" if current_player == "X" else "X"

def main():
    print(TITLE)
    p1_name = input("Enter Player 1 name: ").strip() or "Player 1"
    mode = ""
    while mode not in ["1", "2"]:
        mode = input("Play vs (1) Friend or (2) Bot? Enter 1 or 2: ").strip()

    if mode == "1":
        p2_name = input("Enter Player 2 name: ").strip() or "Player 2"
        difficulty = None
    else:
        p2_name = "Bot"
        difficulty = ""
        while difficulty not in ["easy", "medium", "hard"]:
            difficulty = input("Choose bot difficulty (easy, medium, hard): ").strip().lower()

    scores = {p1_name: 0, p2_name: 0, "Tie": 0}

    while True:
        winner = play_game(p1_name, p2_name, mode, difficulty)
        if winner == "X":
            scores[p1_name] += 1
        elif winner == "O":
            scores[p2_name] += 1
        else:
            scores["Tie"] += 1

        print(f"\nScoreboard:\n{Fore.GREEN}{p1_name}: {scores[p1_name]}{Style.RESET_ALL} | "
              f"{Fore.RED}{p2_name}: {scores[p2_name]}{Style.RESET_ALL} | "
              f"{Fore.YELLOW}Ties: {scores['Tie']}{Style.RESET_ALL}\n")

        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
