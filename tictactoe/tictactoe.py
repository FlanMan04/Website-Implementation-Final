from pyscript import document, when
from js import console

board = [" "] * 9
current_player = "X"
game_over = False

cells = [document.getElementById(f"cell{i}") for i in range(9)]
message_div = document.getElementById("message")
reset_btn = document.getElementById("resetBtn")

def update_board_display():
    """Refresh button text from the board list."""
    for i, cell in enumerate(cells):
        cell.innerText = board[i]

def check_winner():
    """Return winner ('X' or 'O') or None if no winner yet."""
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for a,b,c in win_patterns:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def is_tie():
    """Return True if board is full and no winner."""
    return " " not in board

def handle_click(i):
    global current_player, game_over
    if game_over:
        return
    if board[i] != " ":
        return

    board[i] = current_player
    update_board_display()

    # Check win / tie
    winner = check_winner()
    if winner:
        message_div.innerText = f"Player {winner} wins!"
        game_over = True
        disable_all_cells(True)
        return
    if is_tie():
        message_div.innerText = "It's a tie!"
        game_over = True
        disable_all_cells(True)
        return

    current_player = "O" if current_player == "X" else "X"
    message_div.innerText = f"Player {current_player}'s turn"

def reset_game():
    global board, current_player, game_over
    board = [" "] * 9
    current_player = "X"
    game_over = False
    update_board_display()
    disable_all_cells(False)
    message_div.innerText = "Player X's turn"

def disable_all_cells(disabled):
    for cell in cells:
        cell.disabled = disabled

for i, cell in enumerate(cells):
    # Use a lambda with default argument to capture the current i
    cell.onclick = lambda e, idx=i: handle_click(idx)

reset_btn.onclick = lambda e: reset_game()

update_board_display()