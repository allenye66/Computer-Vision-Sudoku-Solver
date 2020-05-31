# SudokuSolver

How to run:

- first run app.py file in terminal
- go to http://127.0.0.1:5000/


How our program works: After the user submit an image, we send the image to our flask server. From there, we preprocess the image using Gaussian Blurring and Thresholding. Afterwards, we locate the sudoku grid in the image using Hough Line Transform algorithm. After having an image with just the grid, we splie the grid into 81 seperate images and use a CNN with approximately 99 percent accuracy to predict the numbers in each grid. These numbers are added to an array and we use our sudoku solving algorithm to solve the puzzle.