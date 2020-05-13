from flask import Flask, render_template, request
import solve

app = Flask(__name__)

@app.route('/')
def index():
	print("received the values")
	return render_template('index.html')

@app.route('/obtainInput', methods = ['GET' ,'POST'])
def obtainInput():


	w, h = 9, 9;
	grid = [[0 for x in range(w)] for y in range(h)] 

	#determine the numbers and send them to another python file to process the numbers and solve the grid


	answers = solve(grid)

	
	return render_template('pass.html', grid)

if __name__ == '__main__':
	app.run(debug=True)
