import sys

def is_safe_place(board, row, col, N):
    """
    This function check if it is safe to place a queen in the given position.

    Args:
        board (list[list[int]]): Chessboard representing queen placements.
        row (int): Row in which to check for safety.
        col (int): Column in which to check for safety.
        N (int): Size of the board.

    Returns:
        bool: False if it isn't safe to place a queen, True otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def s_nqueens(N):
    """
    Solve the N Queens problem and print all possible solutions.

    Args:
        N (int): The size of the chessboard and the number of queens.

    Prints:
        All possible solutions to the N Queens problem.
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]

    def s_util(board, col):
        if col >= N:
            for row in range(N):
                solution = []
                for c in range(N):
                    if board[row][c] == 1:
                        solution.append([row, c])
                print(solution)
            return True

        for i in range(N):
            if is_safe_place(board, i, col, N):
                board[i][col] = 1
                s_util(board, col + 1)
                board[i][col] = 0

    if not s_util(board, 0):
        print("No solution exists")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    s_nqueens(N)
