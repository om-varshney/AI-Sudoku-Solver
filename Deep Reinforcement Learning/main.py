import numpy as np
import pandas as pd

# We are basically reading the csv file containing sudoku strings and reading and reshaping them
sudoku_games = pd.read_csv("sudoku.csv")
for i in range(10):
    print("Quiz")
    print(np.array(tuple(map(int, " ".join(sudoku_games.iloc[i]["quizzes"]).split()))).reshape(9, 9))
    print("Solution")
    print(np.array(tuple(map(int, " ".join(sudoku_games.iloc[i]["solutions"]).split()))).reshape(9, 9))
