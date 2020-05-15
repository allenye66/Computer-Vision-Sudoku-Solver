'''
def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return (x, y)
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return (x, y)
    return (-1, -1)


def isValid( grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            (secTopX, secTopY) = (3 * (i // 3), 3 * (j // 3))
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(grid, i=0, j=0):
    (i, j) = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True

            grid[i][j] = 0
    return False
'''
def print_grid(arr): 
    for i in range(9): 
        for j in range(9): 
            print(arr[i][j]) 
        print ('n') 

def find_empty_location(arr,l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False
  

def used_in_row(arr,row,num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  
def used_in_col(arr,col,num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False

def used_in_box(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i+row][j+col] == num): 
                return True
    return False
def check_location_is_safe(arr,row,col,num): 
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num) 
def solve_sudoku(arr): 
      
    l=[0,0] 
      
    if(not find_empty_location(arr,l)): 
        return True
      
    row=l[0] 
    col=l[1] 
      
    for num in range(1,10): 
          
        if(check_location_is_safe(arr,row,col,num)): 
              
            arr[row][col]=num 
  
            if(solve_sudoku(arr)): 
                return True
  
            arr[row][col] = 0
              
    return False 
  
def oogs(grid):
	solve_sudoku(grid)
	return grid
	#print_grid(grid)
