"""
This file will contain the function which will then be able to solve our sudoku.
"""
"""
Create a function that checks after assigning the current index the grid becomes unsafe or not. 
Keep Hashmap for a row, column and boxes. If any number has a frequency greater than 1 in the hashMap return false else 
return true; hashMap can be avoided by using loops.

Create a recursive function that takes a grid.

Check for any unassigned location. If present then assign a number from 1 to 9, check if assigning the number to current
index makes the grid unsafe or not, if safe then recursively call the function for all safe cases from 0 to 9.

if any recursive call returns true, end the loop and return true. If no recursive call returns true then return false.
If there is no unassigned location then return true.
"""
M = 9


def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()


def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def sudoku(grid, row, col):
    print("solving...")
    if row == M - 1 and col == M:
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return sudoku(grid, row, col + 1)
    for num in range(1, M + 1, 1):
        if solve(grid, row, col, num):
            grid[row][col] = num
            if sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


if __name__ == '__main__':
    '''0 means the cells where no value is assigned'''
    grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
            [0, 1, 0, 0, 0, 4, 0, 0, 0],
            [4, 0, 7, 0, 0, 0, 2, 0, 8],
            [0, 0, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 8, 1, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 6, 0, 0, 7, 2],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [9, 0, 3, 0, 0, 0, 6, 0, 4]]

    if sudoku(grid, 0, 0):
        puzzle(grid)
    else:
        print("Solution does not exist:(")
