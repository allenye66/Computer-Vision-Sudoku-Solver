from flask import Flask, render_template, request
import solve
from solve import oogs
import subprocess



app = Flask(__name__)

@app.route('/')
def index():
	print("received the values")
	return render_template('index.html')

@app.route('/send', methods = ['GET' ,'POST'])
def obtainInput():
	grid = [[0 for i in range(9)] for j in range(9)]
	if request.method == 'POST':
		for i in range(9):
			for j in range(9):
				s = ""+str(i) + ","+str(j)
				grid[j][i] = int(request.form[s])

		'''
		grid[0][0] = int(request.form['0,0'])
		grid[0][1] = int(request.form['0,1'])
		grid[0][2] = int(request.form['0,2'])
		grid[1][0] = int(request.form['1,0'])
		grid[1][1] = int(request.form['1,1'])
		grid[1][2] = int(request.form['1,2'])
		grid[2][0] = int(request.form['2,0'])
		grid[2][1] = int(request.form['2,1'])
		grid[2][2] = int(request.form['2,2'])

		grid[0][3] = int(request.form['0,0'])
		grid[0][4] = int(request.form['0,1'])
		grid[0][5] = int(request.form['0,2'])
		grid[1][3] = int(request.form['1,0'])
		grid[1][4] = int(request.form['1,1'])
		grid[1][5] = int(request.form['1,2'])
		grid[2][3] = int(request.form['2,0'])
		grid[2][4] = int(request.form['2,1'])
		grid[2][5] = int(request.form['2,2'])

		grid[0][6] = int(request.form['0,0'])
		grid[0][7] = int(request.form['0,1'])
		grid[0][8] = int(request.form['0,2'])
		grid[1][6] = int(request.form['1,0'])
		grid[1][7] = int(request.form['1,1'])
		grid[1][8] = int(request.form['1,2'])
		grid[2][6] = int(request.form['2,0'])
		grid[2][7] = int(request.form['2,1'])
		grid[2][8] = int(request.form['2,2'])



		grid[3][0] = int(request.form['0,0'])
		grid[3][1] = int(request.form['0,1'])
		grid[3][2] = int(request.form['0,2'])
		grid[4][0] = int(request.form['1,0'])
		grid[4][1] = int(request.form['1,1'])
		grid[4][2] = int(request.form['1,2'])
		grid[5][0] = int(request.form['2,0'])
		grid[5][1] = int(request.form['2,1'])
		grid[5][2] = int(request.form['2,2'])

		grid[3][3] = int(request.form['0,0'])
		grid[3][4] = int(request.form['0,1'])
		grid[3][5] = int(request.form['0,2'])
		grid[4][3] = int(request.form['1,0'])
		grid[4][4] = int(request.form['1,1'])
		grid[4][5] = int(request.form['1,2'])
		grid[5][3] = int(request.form['2,0'])
		grid[5][4] = int(request.form['2,1'])
		grid[5][5] = int(request.form['2,2'])

		grid[3][6] = int(request.form['0,0'])
		grid[3][7] = int(request.form['0,1'])
		grid[3][8] = int(request.form['0,2'])
		grid[4][6] = int(request.form['1,0'])
		grid[4][7] = int(request.form['1,1'])
		grid[4][8] = int(request.form['1,2'])
		grid[5][6] = int(request.form['2,0'])
		grid[5][7] = int(request.form['2,1'])
		grid[5][8] = int(request.form['2,2'])



		grid[6][0] = int(request.form['0,0'])
		grid[6][1] = int(request.form['0,1'])
		grid[6][2] = int(request.form['0,2'])
		grid[7][0] = int(request.form['1,0'])
		grid[7][1] = int(request.form['1,1'])
		grid[7][2] = int(request.form['1,2'])
		grid[8][0] = int(request.form['2,0'])
		grid[8][1] = int(request.form['2,1'])
		grid[8][2] = int(request.form['2,2'])

		grid[6][3] = int(request.form['0,0'])
		grid[6][4] = int(request.form['0,1'])
		grid[6][5] = int(request.form['0,2'])
		grid[7][3] = int(request.form['1,0'])
		grid[7][4] = int(request.form['1,1'])
		grid[7][5] = int(request.form['1,2'])
		grid[8][3] = int(request.form['2,0'])
		grid[8][4] = int(request.form['2,1'])
		grid[8][5] = int(request.form['2,2'])

		grid[6][6] = int(request.form['0,0'])
		grid[6][7] = int(request.form['0,1'])
		grid[6][8] = int(request.form['0,2'])
		grid[7][6] = int(request.form['1,0'])
		grid[7][7] = int(request.form['1,1'])
		grid[7][8] = int(request.form['1,2'])
		grid[8][6] = int(request.form['2,0'])
		grid[8][7] = int(request.form['2,1'])
		grid[8][8] = int(request.form['2,2'])
'''
		#grid = [[r0c0, r1c0, r2c0], [r0c1, r1c1, r2c1], [r0c2, r1c2, r2c2]]

		#print(grid)
		print("testing---------------------------------------------")
		print(grid)

		#n = n * oogs()

	return render_template('pass.html') #, num = n)

	'''
	w, h = 9, 9;
	grid = [[0 for x in range(w)] for y in range(h)] 

	#determine the numbers and send them to another python file to process the numbers and solve the grid


	answers = solve(grid)

	'''

if __name__ == '__main__':
	app.run(debug=True)
