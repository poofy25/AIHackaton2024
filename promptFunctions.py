import json
from openai import OpenAI
from dotenv import load_dotenv
import os

examplePrompt = 'Return the answer as json (example : {"grammar":0,"disciminatory":1 , "morbid":0 , "corellency":0 , "questions":0 , "emotion":neutral}) \n '
grammarPrompt = 'Does this article contain obvious / big grammatical mistakes ? respond in binary 0 / 1 (response example : 0) \n'
discriminatoryPrompt = 'Does this article contain discriminatory or sexism content ? respond in binary 0 / 1 (response example : 0) \n'
corellencyPrompt = 'Is this articles title corellent with the content or not ? 1 for no , 0 for yes (response example : 1) \n '
morbidPrompt = 'Aceasta este o stire, raspunde cu cifra "1" daca stirea contine detalii morbide si raspunde cu cifra "0" daca stirea nu contine detalii morbide \n'
questionsPrompt = 'Does this news article respond to the all of these questions : (Why,Who,When,Where,How) ? Respond in binary 0 for yes and 1 for no (response example : 0) \n'
emotionPrompt = 'What emotion does this news article convey ? Positive Neutral or Negative (response example: Neutral) \n'


load_dotenv()

GPT_API_KEY = os.getenv('GPT_API_KEY')

client = OpenAI(
    api_key=GPT_API_KEY
)

def getGPTResponse(content , title):
    prompt = grammarPrompt + discriminatoryPrompt + morbidPrompt + corellencyPrompt + questionsPrompt + emotionPrompt + examplePrompt + "Title : " + f"{title} \n" + "Content : " + f"{content} \n"
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4-turbo-preview",
        )
    response = chat_completion.choices[0].message.content
    startIndex1 = response.find("{")
    startIndex2 = response.find("}") + 1

    return json.loads(response[startIndex1:startIndex2])


def returnTotal(data):
  json_object = json.loads(data)
  total = json_object['grammar'] + json_object['politics'] + json_object['discriminatory']

  print("Hello from a function")
  return total

def returnSmile(data):
  json_object = json.loads(data)
  total = json_object['grammar'] + json_object['politics'] + json_object['discriminatory']

  if total == 0: return '😀'
  if total == 1: return '😀'
  if total == 2: return '😐'
  if total == 3: return '🙁'