N = 4
board = [[0] * N for _ in range(N)]

def is_safe(row, col, b):
    for r in range(row):
        if b[r][col] == 1:
            return False

    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if b[r][c] == 1:
            return False
        r -= 1
        c -= 1

    r, c = row - 1, col + 1
    while r >= 0 and c < N:
        if b[r][c] == 1:
            return False
        r -= 1
        c += 1

    return True

def solve_n_queens(row, b):
    if row == N:
        for r in b:
            print(r)
        return True

    for col in range(N):
        if is_safe(row, col, b):
            b[row][col] = 1
            if solve_n_queens(row + 1, b):
                return True
            b[row][col] = 0

    return False

solve_n_queens(0, board)
