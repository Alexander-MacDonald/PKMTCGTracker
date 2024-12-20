import os
import constants

def readData(path):
    ret = []
    for series in os.listdir(path):
        for set in os.listdir(path + "/" + series):
            ret.append(open(path + "/" + series + "/" + set, "r", encoding="utf-8").read().split("\n"))
    return ret

engFiles = constants.ENGPATH
jpFiles = constants.JPPATH
info = readData(engFiles) + readData(jpFiles)
parsedInfo = []

# The 'Check All Check None' index doesnt work for the holiday sets
# The '#' index does not work for JP Base Set & some random hydreigon BW deck
# Combine & Normalize for both.
for setInfo in info:
    if "Check All Check None" not in setInfo:
        poundIndex = -1
        for datapoint in setInfo:
            if "#" in datapoint:
                poundIndex = setInfo.index(datapoint)
                parsedInfo.append([setInfo[:poundIndex], setInfo[poundIndex:]])
                break
        if poundIndex == -1:
            print(setInfo[0], "ERROR - CHECK FOR A NEW UNIQUE INDEX")
    else:
        parsedInfo.append([setInfo[:setInfo.index("Check All Check None")], setInfo[setInfo.index("Check All Check None")+1:]])
for entry in parsedInfo:
    print(entry[0][0], entry[1][0])