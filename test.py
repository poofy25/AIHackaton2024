import requests
import json 
key = 'AIzaSyDf4kIBllEIn9jN_iJPS4j2q6IRwyIo6Do'
link = f"https://www.googleapis.com/customsearch/v1?key={key}&cx=017576662512468239146:omuauf_lfve&q=lectures"
res = requests.get(link)
response = json.loads(res.text)

data = [
  {
    "content": "Add a similar content entry to the input list in order to calculate similarity.",
    "language": "xxx"
  },
  {
    "content": "Add a similar content entry to the input list in order to calculate similarity.",
    "language": "xxx"
  }
]
getLink = 'http://localhost:8989/rest/process'
getresponse = requests.post(getLink , json=data)
responseJson = json.loads(getresponse.text)

print(responseJson)