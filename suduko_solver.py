def is_valid(board, row, col, num):
    """Check if it's valid to place num in board[row][col]."""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def find_empty_cell(board):
    """Find an empty cell in the Sudoku board."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # No empty cells left, puzzle is solved
    
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack
    return False

def print_board(board):
    """Print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def get_user_input():
    """Get Sudoku input from the user."""
    print("Enter the Sudoku puzzle row by row (use 0 for empty cells):")
    board = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) == 9 and all(0 <= num <= 9 for num in row):
                    board.append(row)
                    break
                else:
                    print("Invalid input! Please enter exactly 9 numbers (0-9). give space between each numbers")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
    return board

# Get Sudoku puzzle from user input
sudoku_board = get_user_input()

print("\nUnsolved Sudoku:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists.")
