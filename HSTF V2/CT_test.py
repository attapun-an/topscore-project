import

#Create first time
OpenTopScore("topScore.txt")

AddScore("Little Jonny",275,"topScore.txt")

topScoreList = OpenTopScore("topScore.txt")

for each in topScoreList:
    print(each)

WriteTopScores(topScoreList,"topScore.txt")

DisplayTopScore("topscore.txt")
