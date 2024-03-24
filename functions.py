import requests
import json 

def getContentFromLink (link) :
    apiLink = 'http://localhost:8990/rest/process'
    data = [
      {
        "content": link,
        "language": "EMPTY"
      }
    ]
    getresponse = requests.post(apiLink , json=data)
    responseJson = json.loads(getresponse.text)
    return responseJson[0]['text']

def getMetaData (link) :

    url = "https://site-metadata.p.rapidapi.com/metadata/"

    querystring = {"url":link}

    headers = {
      "X-RapidAPI-Key": "8f891280b8msh97f5e47be9aeedfp126f7bjsn545322e02f10",
      "X-RapidAPI-Host": "site-metadata.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    

    return response.json()