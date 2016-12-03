"""
OpenTopScore(fileName) 
This function creates a new, empty, top score text file if it doesn't exist,
otherwise it opens the text file filename (string) and returns a list of the
contents 
 
AddScore(name, score, filename) 
This procedure takes 3 parameters, the name (string), score (integer) and
the top score filename (string). It should append this information to the
file. 
 
WriteTopScores(topScores, filename) 
This function writes a list to the text file filename (string) as the top
score table 
 
DisplayTopScore(filename) 
Displays the top scores in the filename (string)
"""


def open_top_score(file_name):
    f = open(file_name, "r")
    return f


def add_score(name, score, file_name):
    f = open(file_name, "a")
    f.write(name + "\n")
    f.write(score)


def write_top_scores(top_scores, file_name):
    f = open(file_name, "w")
    f.write(top_scores)


def display_top_scores(file_name):
    f = open(file_name, "r")
    top_scores = f.read()
    print(top_scores)


display_top_scores("HSTF.txt")
