
def notInRow(arr, row): 

	st = set() 

	for i in range(0, 9):
		if arr[row][i] in st: 
			return False

		if arr[row][i] != '0': 
			st.add(arr[row][i]) 
	
	return True

def notInCol(arr, col): 

	st = set() 

	for i in range(0, 9): 

		# If already encountered before, 
		# return false 
		if arr[i][col] in st: 
			return False

		# If it is not an empty cell, insert 
		# value at the current cell in the set 
		if arr[i][col] != '0': 
			st.add(arr[i][col]) 
	
	return True

# Checks whether there is any duplicate 
# in current 3x3 box or not. 
def notInBox(arr, startRow, startCol): 

	st = set() 

	for row in range(0, 3): 
		for col in range(0, 3): 
			curr = arr[row + startRow][col + startCol] 

			# If already encountered before, 
			# return false 
			if curr in st: 
				return False

			# If it is not an empty cell, 
			# insert value at current cell in set 
			if curr != '0': 
				st.add(curr) 
		
	return True

# Checks whether current row and current 
# column and current 3x3 box is valid or not 
def isValid(arr, row, col): 

	return (notInRow(arr, row) and notInCol(arr, col) and
			notInBox(arr, row - row % 3, col - col % 3)) 

def valid(arr): 
	for i in range(0, 9): 
		for j in range(0, 9): 

			# If current row or current column or 
			# current 3x3 box is not valid, return false 
			if not isValid(arr, i, j): 
				return False
		
	return True

