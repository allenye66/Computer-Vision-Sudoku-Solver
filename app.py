from flask import Flask, render_template, request, redirect, url_for, flash
import solve
from solve import return_grid
import solvable
from solvable import isValid
import subprocess
import os
import cv2
from werkzeug.utils import secure_filename
# import predict
from predict import predict_grid
app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "/Users/allen/Desktop/SudokuSolver/static/img"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024


# @app.route('/')
# def index():
# 	print("received the values")
# 	return render_template('index.html')

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

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
	target = os.path.join(APP_ROOT, 'images/')
	print(target)

	if not os.path.isdir(target):
		os.mkdir(target)

	file = request.files.getlist("file")[0]
	# for file in request.files.getlist("file"):
	print("**************************")
	print(type(file))
	print(file)
	predict_grid("images/" + file.filename)
	filename = file.filename
	destination = "/".join([target, filename])
	print(destination)
	file.save(destination)
	return render_template("success.html")

if __name__ == "__main__":
	app.run(debug=True)

# @app.route("/upload-image", methods=["GET", "POST"])
# def upload_image():
#
# 	if request.method == "POST":
#
# 		if request.files:
#
# 			if "filesize" in request.cookies:
#
# 				if not allowed_image_filesize(request.cookies["filesize"]):
# 					print("Filesize exceeded maximum limit")
# 					return redirect(request.url)
#
# 				image = request.files["image"]
#
# 				if image.filename == "":
# 					print("No filename")
# 					return redirect(request.url)
#
# 				if allowed_image(image.filename):
# 					filename = secure_filename(image.filename)
#
# 					image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
#
# 					print("Image saved")
#
# 					return redirect(request.url)
#
# 				else:
# 					print("That file extension is not allowed")
# 					return redirect(request.url)
#
# 	return render_template("templates/pass.html")

@app.route('/return', methods = ['GET', 'POST'])
def returnToHome():
	return render_template("index.html")


@app.route('/send', methods = ['GET' ,'POST'])
def obtainInput():
	grid = [[0 for i in range(9)] for j in range(9)]
	grid2 = [[0 for i in range(9)] for j in range(9)]
	if request.method == 'POST':
		for i in range(9):
			for j in range(9):
				s = ""+str(i) + ","+str(j)
				temp = str(request.form[s])
				if len(temp) == 0:
					temp = str(0);
				grid[j][i] = int(temp)
				grid2[i][j] = int(temp)
		print("DEBUGGING---------------------------------------------")

		print(grid2)

		print(isValid(grid2))
		if isValid(grid2) == False:
			return render_template('fail.html')

		grid = return_grid(grid)
		#print(grid)
		#print(grid2)
		#print("***********")
		hint = []
		for i in range(9):
			for j in range(9):
				if grid[i][j] != grid2[i][j] :
					hint.append(grid[i][j])
		
		#print(hint)
		#print(len(hint))

		print("******************************************************")




	iterate = {0, 1, 2, 3, 4, 5, 6, 7, 8}

	return render_template('pass.html', nums=grid, iter=iterate, hints = hint, hLen = len(hint)) #, num = n)


if __name__ == '__main__':
	app.run(debug=True)
