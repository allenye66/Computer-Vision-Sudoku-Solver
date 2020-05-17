def checkRow(grid, row):
	#3, 0, 0, 0, 0, 0, 0, 5
	#3, 3, 0, 0, 0, 0, 0, 0

	s = set()
	for i in range(9):
		temp = int(grid[row][i])
		if temp != 0:
			if temp in s:
				#print("THIS ROW DOES NOT WORK")
				return False
			s.add(temp)
	return True
def checkRows(grid):
	for i in range(9):
		checkRow(grid, i)
		if checkRow(grid, i) == False:
			return False
	return True


def checkColumn(grid, col):

	s = set()
	for i in range(9):
		temp = int(grid[i][col])
		if temp != 0:
			if temp in s:
				return False
			s.add(temp)
	return True

def checkColumns(grid):
	for i in range(9):
		if checkColumn(grid, i) == False:
			return False
	return True

def three(grid, row, col):
	s = set()
	for i in range(3):
		for j in range(3):
			temp = int(grid[i + row][j + col])
			if temp in s:
				return False
			if temp != 0:
				s.add(temp)
	return True


def isValid(grid):
	if checkRows(grid) == False or checkColumns(grid) == False:
		return False
	for i in range(9):
		for j in range(9):
			row = i - i % 3
			col = j - j % 3
			if three(grid, row, col) == False:

				return False
	return True

# NOT WORKING BECAUSE OF GRIDS WITH ALL ZEROES

