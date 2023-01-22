# function to print matrix grid
def matrix_grid_print(m):  # m -- matrix to print
    print('---------')
    for i in range(3):
        print('| ', end='')
        for j in range(3):
            print(m[i][j], '', end='')
        print('|')
    print('---------')


# check input from user (X)
def input_x():
    global matrix
    while True:
        try:
            a, b = input().split()
            a = int(a)
            b = int(b)
        except ValueError:
            print('You should enter numbers!')
        else:
            if not (0 <= a <= 3 and 0 <= b <= 3):
                print("Coordinates should be from 1 to 3!")
            elif not (matrix[a - 1][b - 1] == '_' or matrix[a - 1][b - 1] == ' '):
                print('This cell is occupied! Choose another one!')
            else:
                matrix[a - 1][b - 1] = 'X'
                break


# check input from user (O)
def input_o():
    global matrix
    while True:
        try:
            a, b = input().split()
            a = int(a)
            b = int(b)
        except ValueError:
            print('You should enter numbers!')
        else:
            if not (0 <= a <= 3 and 0 <= b <= 3):
                print("Coordinates should be from 1 to 3!")
            elif not (matrix[a - 1][b - 1] == '_' or matrix[a - 1][b - 1] == ' '):
                print('This cell is occupied! Choose another one!')
            else:
                matrix[a - 1][b - 1] = 'O'
                break


# checking if there full sides or diagonals with X or O
def full_sides(m):  # m -- matrix to check
    # checking is there full sides with X or O
    for i in range(3):
        if m[i][0] == m[i][1] == m[i][2]:
            if m[i][0] == 'X':
                return 'X'
            elif m[i][0] == 'O':
                return 'O'
        if m[0][i] == m[1][i] == m[2][i]:
            if m[0][i] == 'X':
                return 'X'
            elif m[0][i] == 'O':
                return 'O'
    # checking is there full diagonals with X or O
    if m[0][0] == m[1][1] == m[2][2]:
        if m[0][0] == 'X':
            return 'X'
        elif m[0][0] == 'O':
            return 'O'
    if m[0][2] == m[1][1] == m[2][0]:
        if m[0][2] == 'X':
            return 'X'
        elif m[0][2] == 'O':
            return 'O'


# checking if there is no of empty cells
def draw(m):
    for i in range(3):
        for j in range(3):
            if m[i][j] == ' ' or m[i][j] == '_':
                return False
    return True

# PROGRAM BODY

# making matrix grid
count = 0
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append(' ')  # empty matrix
        count += 1

matrix_grid_print(matrix)  # printing empty matrix grid

while True:
    input_x()  # check and take X coordinates
    matrix_grid_print(matrix)
    if full_sides(matrix):
        print(full_sides(matrix), 'wins')
        break
    if draw(matrix):
        print('Draw')
        break
    input_o()  # check and take O coordinates
    matrix_grid_print(matrix)
    if full_sides(matrix):
        print(full_sides(matrix), 'wins')
        break
    if draw(matrix):
        print('Draw')
        break
