
badDetails = {
"blackListed": "❌ Website is blacklisted for fake news. \n",
"grammar": "❌ Contains grammatical errors. \n",
"corellency": "❌ The title does not correlate with the content of the article. \n",
"discriminatory": "❌ Contains discriminatory or sexist content. \n",
"questions": "❌ Does not answer important questions: (Why?, Who?, When?, Where?, How?). \n",
"emotionPositive": "❌ Contains only positive sentiments. \n",
"emotionNegative": "❌ Contains only negative sentiments. \n",
"morbid": "❌ Contains morbid details. \n"
}

goodDetails = {
"blackListed": "✔️ Website is not blacklisted for fake news. \n",
"grammar": "✔️ No grammatical errors. \n",
"corellency": "✔️ The title correlates with the content of the article. \n",
"discriminatory": "✔️ Does not contain discriminatory or sexist content. \n",
"questions": "✔️ Answers important questions: (Why?, Who?, When?, Where?, How?) \n",
"emotionNeutral": "✔️ Contains neutral sentiments. \n",
"morbid": "✔️ Does not contain morbid details. \n",
}



def getDetails (data , quality) :
    totalDetails = ''
    if data["blackListed"] == 1 :totalDetails = totalDetails + badDetails["blackListed"] + " \n"
    if data["grammar"] == 1 :totalDetails = totalDetails + badDetails["grammar"] + " \n"
    if data["corellency"] == 1 :totalDetails = totalDetails + badDetails["corellency"] + " \n"
    if data["discriminatory"] == 1 :totalDetails = totalDetails + badDetails["discriminatory"] + " \n"
    if data["questions"] == 1 :totalDetails = totalDetails + badDetails["questions"] + " \n"
    if data["morbid"] == 1 :totalDetails = totalDetails + badDetails["morbid"] + " \n"
    if data["emotion"] == "Positive" :totalDetails = totalDetails + badDetails["emotionPositive"] + " \n"
    if data["emotion"] == "Negative" :totalDetails = totalDetails + badDetails["emotionNegative"] + " \n"
    if quality == "Good" :
        if data["blackListed"] == 0 :totalDetails = totalDetails + goodDetails["blackListed"] + " \n"
        if data["grammar"] == 0 :totalDetails = totalDetails + goodDetails["grammar"] + " \n"
        if data["corellency"] == 0 :totalDetails = totalDetails + goodDetails["corellency"] + " \n"
        if data["discriminatory"] == 0 :totalDetails = totalDetails + goodDetails["discriminatory"] + " \n"
        if data["questions"] == 0 :totalDetails = totalDetails + goodDetails["questions"] + " \n"
        if data["morbid"] == 0 :totalDetails = totalDetails + goodDetails["morbid"] + " \n"
        if data["emotion"] == "Neutral" :totalDetails = totalDetails + goodDetails["emotionNeutral"] + " \n"



    return totalDetails