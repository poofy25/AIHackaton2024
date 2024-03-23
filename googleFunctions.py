import requests
import json 
key = 'AIzaSyDf4kIBllEIn9jN_iJPS4j2q6IRwyIo6Do'

def getRelevantUrls (title) :
    link = f"https://www.googleapis.com/customsearch/v1?key={key}&cx=017576662512468239146:omuauf_lfve&q={title}"
    res = requests.get(link)
    response = json.loads(res.text)
    return response

print(getRelevantUrls('Belgia și Cehia vor spriji sectorul energetic al R. Moldova – Ziarul de Gardă'))
