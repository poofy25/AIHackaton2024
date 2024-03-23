from promptFunctions import getGPTResponse
from functions import getContentFromLink


weights = {
    "grammar":1,
    "corellency":3,
    "discriminatory":5,
    "questions":3,
    "emotion":3,
    "morbid":4
}



def calculateWeights (data):
    totalWeights = 19
    total = 0


    if data["grammar"] == 1 :total += weights["grammar"]
    if data["corellency"] == 1 :total += weights["corellency"]
    if data["discriminatory"] == 1 :total += weights["discriminatory"]
    if data["questions"] == 1 :total += weights["questions"]
    if data["morbid"] == 1 :total += weights["morbid"]
    if data["emotion"] == "Positive" :total += weights["emotion"]
    if data["emotion"] == "Negative" :total += weights["emotion"]

    percentage = 100 - ((total * 100) / totalWeights)
    return percentage

def returnEmoji (percentage) :
    if(percentage > 66) : return '😃'
    if(percentage > 33 ) : return '😑'
    if(percentage <= 33 ) : return '💩'