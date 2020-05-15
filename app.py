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
	if request.method == 'POST':
		r0c0 = int(request.form['0,0'])
		r0c1 = int(request.form['0,1'])
		r0c2 = int(request.form['0,2'])
		r1c0 = int(request.form['1,0'])
		r1c1 = int(request.form['1,1'])
		r1c2 = int(request.form['1,2'])
		r2c0 = int(request.form['2,0'])
		r2c1 = int(request.form['2,1'])
		r2c2 = int(request.form['2,2'])

		grid = [[r0c0, r1c0, r2c0], [r0c1, r1c1, r2c1], [r0c2, r1c2, r2c2]]

		print(grid)
		print("testing---------------------------------------------")
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
