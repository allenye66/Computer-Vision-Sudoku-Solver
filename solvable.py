
def notInRow(arr, row): 
	st = set() 

	for i in range(0, 9):
		if arr[row][i] in st: 
			return False

		if arr[row][i] !='0': 
			st.add(arr[row][i]) 
	
	return True

def notInCol(arr, col): 

	st = set() 

	for i in range(0, 9): 


		if arr[i][col] in st: 
			return False
 
		if arr[i][col] !='0': 
			st.add(arr[i][col]) 
	
	return True


def notInBox(arr, startRow, startCol): 

	st = set() 

	for row in range(0, 3): 
		for col in range(0, 3): 
			curr = arr[row + startRow][col + startCol] 

			if curr in st: 
				return False


			if curr !='0': 
				st.add(curr) 
		
	return True


def isValid(arr, row, col): 

	return (notInRow(arr, row) and notInCol(arr, col) and
			notInBox(arr, row - row % 3, col - col % 3)) 

def isValidConfig(arr): 
	for i in range(0, 9): 
		for j in range(0, 9): 

			if not isValid(arr, i, j): 
				return False
		
	return True
def valid(board): 
'''	
	board = [[ '5', '3', '0', '0', '7', '0', '0', '0', '0' ],  
			 [ '6', '0', '0', '1', '9', '5', '0', '0', '0' ],  
			 [ '0', '9', '8', '0', '0', '0', '0', '6', '0' ],  
			 [ '8', '0', '0', '0', '6', '0', '0', '0', '3' ],  
			 [ '4', '0', '0', '8', '0', '3', '0', '0', '1' ],  
			 [ '7', '0', '0', '0', '2', '0', '0', '0', '6' ],  
			 [ '0', '6', '0', '0', '0', '0', '2', '8', '0' ],  
			 [ '0', '0', '0', '4', '1', '9', '0', '0', '5' ],  
			 [ '0', '0', '0', '0', '8', '0', '0', '7', '9' ]] 
'''	
	if isValidConfig(board):  
		return True; 
	else: 
		return False;
  

  

