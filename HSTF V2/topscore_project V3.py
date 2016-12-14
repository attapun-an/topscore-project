import os

def OpenTopScore(fileName):
        open_loop = True
        # fileName = fileName + ".txt"
        while open_loop:
            check = os.path.exists("./" + fileName)
            if check == False:
                file = open(fileName, "w")
                print("A new empty file under the name {0} has been created".format(fileName))
                file.close()
                open_loop = False
            else:
                file = open(fileName, "r")
                file_read = file.read()
                list_format = file_read.split(",")
                file.close()
                return list_format

def AddScore(name, score, file_name):
    file = open(file_name, "a")
    file.write(name + "," + str(score) + ",")
    file.close()

def WriteTopScores(topScores, filename):
    file = open(filename, "w")
    for i in topScores:
        file.write("," + i)
    file.close()



def DisplayTopScore(filename):
    file = open(filename, "r")
    file_read = file.read()
    list_format = file_read.split(",")
    for i in list_format:
        print(i)




topScoreList = OpenTopScore("topScore.txt")

for each in topScoreList:
    print(each)

WriteTopScores(topScoreList,"topScore.txt")



