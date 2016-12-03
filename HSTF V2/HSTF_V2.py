import os

def OpenTopScore(fileName):
    check = os.path.exists("./" + fileName)
    if check:
        file_object = open(fileName, "r")
        data = file_object.read()
        listed = data.split(",")
        print(listed)
        return listed

    else:
        file_object = open(fileName, "w")


def AddScore(name, score, fileName):
    file_object = open(fileName, "a")
    file_object.write(name + "," + str(score) + ",")

def WriteTopScores(topScores, filename):
    file_object = open(filename, "w")
    file_object.write(topScores)

def DisplayTopScore(fileName):
    file_object = open(fileName, "r")
        data = file_object.read()
        listed = data.split(",")
        print(listed)




