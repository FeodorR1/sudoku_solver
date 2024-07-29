# Sudoku solver)

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
        if board[i][col] == num:
            return False

    box_start_row = row - row % 3
    box_start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[box_start_row + i][box_start_col + j] == num:
                return False

    return True


def sudoku(to_solve):
    def solve():
        for row in range(9):
            for col in range(9):
                if to_solve[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(to_solve, row, col, num):
                            to_solve[row][col] = num
                            if solve():
                                return True
                            to_solve[row][col] = 0
                    return False
        return True

    solve()
    return to_solve


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

for i in sudoku(puzzle):
    print(i, sep='\n')
