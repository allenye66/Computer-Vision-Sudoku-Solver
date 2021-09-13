# SudokuSolver

How to run:

- first run app.py file in terminal
- go to http://127.0.0.1:5000/


Our program is designed to solve a sudoku game from an image taken by a phone. After the user submits an image, we send the image to our flask server. From there, we preprocess the image using Gaussian Blurring and Thresholding. Afterward, we locate the sudoku grid in the image using the Hough Line Transform algorithm. After having an image with just the grid, we splice the grid into 81 separate images and use a CNN with approximately 99 percent accuracy to predict the numbers in each grid. These numbers are added to an array and we use our sudoku solving algorithm to solve the puzzle.

