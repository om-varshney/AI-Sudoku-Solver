# The Objective
Here we are trying to make an AI model which can solve sudoku games. It is supposed to look at an image and then solve
the sudoku based on that image. However, we would start with pre-built sudoku strings.

## How we intend to go about it. (Attempt 1)
* First we will run a program to generate sudoku puzzles and their solutions.
* Once this data-set is generated, we will use it to train a Deep Learning model.
* Then as a bonus step we will try to apply CV to generate the sudoku problem from an image.

## How is this a viable project for our semester?
For pre-processing: We need to convert the strings to np arrays for one thing. And then once we have images, we would
need further processing as well.

For EDA: I don't really know what we would plot, but we could always plot graphs and all for accuracy and loss.

For PDSL: Well, the model ig has to fall under PDSL.


---
> Attempt 1 failed even before it started as I can't figure out for the hell of me how to train on a full sudoku puzzle.
> So, here is a plan for attempt two.


## How we intend to go about it.
* First we will use OpenCV to detect the sudoku puzzle from our image and basically crop the rest of the image.
* Then we will find out all the digits present in the image with OpenCV.
* Then we will use a DNN to recognise the digit images and convert them into integers.
* Then we will use a backtracking algorithm to find out the optimal solution to the puzzle.
* And finally we will use a library to convert our array into an image which can then be shown to the user.

---
# Implementation Details
### Step 1: Sudoku Image to Set of Digit images.
* First we will take the image from the user, then we will use some functions of OpenCV to warp and enhance the image
and then to find the sudoku grid in the image and stuff like that.
* Second step we will send this data-structure containing the images to our OCR model.

### Step 2: OCR ANN
* First I will have to get the dataset of MNIST.
* Secondly I will then replace all zero digits in the train and test set to empty images so that our model can recognise
an empty box as 0.
* We will train and try to achieve >99% accuracy for digit recognition.
* Then our OCR model will return prediction on all digits to our solver.

### Step 3: Solving the Sudoku
* This is a simple recursive backtracking DFS problem, I will find a way to solve it.
* There is another way to go about this, we would need to train a RL model to solve the sudoku.
* We would have to make an environment in OpenAI-gym, and then we can pose this as a RL problem.

### Step 4: Editing the original image
* Our final step will be to edit the original image and place the digits of the solved sudoku in there.
* Then we will adjust our final image for perspective and then we are done.

---
