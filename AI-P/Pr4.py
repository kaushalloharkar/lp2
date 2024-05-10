#BAcktracking 
def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, row, N):
    if row >= N:
        return True
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, N):
                return True
            board[row][col] = 0
    return False

def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def n_queens_backtracking(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_n_queens(board, 0, N):
        print("Solution does not exist")
        return False
    print_solution(board, N)
    return True

# Example usage:
n_queens_backtracking(4)
\n
#Branch and BOund
def is_safe(board, row, col, N):
    # Check if there is a queen in the same column or diagonals
    for i in range(row):
        if board[i] == col or \
           board[i] == col - (row - i) or \
           board[i] == col + (row - i):
            return False
    return True

def solve_n_queens(board, row, N, solution):
    if row >= N:
        solution.append(board[:])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_n_queens(board, row + 1, N, solution)

def n_queens_branch_and_bound(N):
    solution = []
    board = [-1] * N
    solve_n_queens(board, 0, N, solution)
    if not solution:
        print("Solution does not exist")
        return False
    for sol in solution:
        for col in sol:
            row_str = ['.'] * N
            row_str[col] = 'Q'
            print(' '.join(row_str))
        print()
    return True







# Example usage:
n_queens_branch_and_bound(4)
