#Input Board/Initial board
board = [
    [4, 1, 5, 0, 6, 9, 0, 7, 0],
    [0, 0, 3, 0, 0, 1, 0, 2, 0],
    [0, 0, 0, 4, 0, 3, 5, 0, 0],
    [6, 7, 2, 1, 0, 0, 0, 0, 4],
    [8, 3, 0, 0, 0, 0, 0, 5, 7],
    [5, 0, 0, 0, 0, 8, 0, 1, 3],
    [2, 8, 0, 0, 0, 7, 1, 0, 6],
    [0, 9, 6, 0, 0, 0, 0, 4, 5],
    [1, 5, 0, 6, 0, 0, 8, 0, 0]
]

#Output the board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('---------------------')

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')

            if j == 8:
                print(bo[i][j])
            else:
                print(bo[i][j], end=' ')

#Check for empty places
def is_Empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return False

#check if the number is valid
def valid(bo, num, row, col):
    # row check
    for i in range(len(bo[0])):
        if bo[row][i] == num and i != col:
            return False

    # column check
    for i in range(len(bo)):
        if bo[i][col] == num and i != row:
            return False

    # square/box check
    box_x = row // 3
    box_y = col // 3
    for i in range(box_x*3, box_x*3+3):
        for j in range(box_y*3, box_y*3+3):
            if bo[i][j] == num and i != row and j != col:
                return False
    return True

#Solve the board with backtracking algo
def solve(bo):
    pos = is_Empty(bo)
    if not pos:
        return True
    else:
        row = pos[0]
        col = pos[1]
        for i in range(1, 10):
            if valid(bo, i, row, col):
                bo[row][col] = i

                if solve(bo):
                    return True
                else:
                    bo[row][col] = 0
    return False

#Check if the initial board is valid
def initial_Validity(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] != 0:
                num = bo[i][j]
                if not valid(bo, num, i, j):
                    return False
    return True


print("\nInitial Board is...\n")
print_board(board)
if initial_Validity(board):
    print("\nSolving Sudoku...\n")
    if solve(board):
        print("\nSolved...\n")
        print_board(board)
else:
    print("\nSudoku Board is invalid\n")