from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
	print("received the values")
	return render_template('index.html')

@app.route('/show', methods = ['GET' ,'POST'])
def show():
	
	return render_template('pass.html', txt = "asdf", wordbank = "asdf")

if __name__ == '__main__':
	app.run(debug=True)
