
weights = {
    "grammar": 4,
    "corellency": 7,
    "discriminatory": 13,
    "questions": 7,
    "emotionNegative": 11,
    "emotionPositive": 1,
    "morbid": 17,
    "isBlackListed": 40
}



def calculatePercentage (data):
    totalWeights = 100
    total = 0


    if data["grammar"] == 1 :total += weights["grammar"]
    if data["corellency"] == 1 :total += weights["corellency"]
    if data["discriminatory"] == 1 :total += weights["discriminatory"]
    if data["questions"] == 1 :total += weights["questions"]
    if data["morbid"] == 1 :total += weights["morbid"]
    if data["emotion"] == "Positive" :total += weights["emotionPositive"]
    if data["emotion"] == "Negative" :total += weights["emotionNegative"]
    if data["blackListed"] == 1 :total += weights["isBlackListed"]

    percentage = 100 - ((total * 100) / totalWeights)
    percentage = float("{:.2f}".format(percentage))
    return percentage

def returnEmoji (percentage) :
    if(percentage > 80) : return {"emoji":'😃' , "text":"Good"}
    if(percentage > 40 ) : return {"emoji":'😑' , "text":"Average"}
    if(percentage <= 33 ) : return {"emoji":'💩' , "text":"Poor"}