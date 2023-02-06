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
