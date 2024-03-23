examplePrompt = 'Return the answer as json (example : {"grammar":0,"politics":1 ...etc}) \n '
grammarPrompt = 'Does this article contain obvious / big grammatical mistakes ?  ? respond in binary 0 / 1 (response example : 0) \n '
discriminatoryPrompt = 'Does this article contain discriminatory content ? respond in binary 0 / 1 (response example : 0) \n '
politicsPrompt = 'Does this article contain politic content ? respond in binary 0 / 1 (response example : 1) \n '

prompt = grammarPrompt + discriminatoryPrompt + politicsPrompt + examplePrompt + "Article :"
def my_function():
  print("Hello from a function")