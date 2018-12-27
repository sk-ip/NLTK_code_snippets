from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos='a'))
print(lemmatizer.lemmatize("runner", pos='v'))
print(lemmatizer.lemmatize("running", pos='v'))