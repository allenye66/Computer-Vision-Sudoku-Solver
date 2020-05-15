from flask import Flask, render_template, request, redirect, url_for, flash
import solve
from solve import oogs
import subprocess
import os
from werkzeug.utils import secure_filename
app.config["IMAGE_UPLOADS"] = "/Users/allen/Desktop/SudokuSolver/static/img"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024

app = Flask(__name__)

@app.route('/')
def index():
	print("received the values")
	return render_template('index.html')

def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_image_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            if "filesize" in request.cookies:

                if not allowed_image_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    return redirect(request.url)

                image = request.files["image"]

                if image.filename == "":
                    print("No filename")
                    return redirect(request.url)

                if allowed_image(image.filename):
                    filename = secure_filename(image.filename)

                    image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                    print("Image saved")

                    return redirect(request.url)

                else:
                    print("That file extension is not allowed")
                    return redirect(request.url)

    return render_template("public/pass.html")


@app.route('/send', methods = ['GET' ,'POST'])
def obtainInput():
	grid = [[0 for i in range(9)] for j in range(9)]
	if request.method == 'POST':
		for i in range(9):
			for j in range(9):
				s = ""+str(i) + ","+str(j)
				temp = str(request.form[s])
				if len(temp) == 0:
					temp = str(0);
				grid[j][i] = int(temp)

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
		grid = oogs(grid)
		print(grid)

		#sn = n * oogs(grid)
	iterate = {0, 1, 2, 3, 4, 5, 6, 7, 8}

	return render_template('pass.html', nums=grid, iter=iterate) #, num = n)

	'''
	w, h = 9, 9;
	grid = [[0 for x in range(w)] for y in range(h)] 

	#determine the numbers and send them to another python file to process the numbers and solve the grid


	answers = solve(grid)

	'''

if __name__ == '__main__':
	app.run(debug=True)
