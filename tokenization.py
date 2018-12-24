from nltk.tokenize import sent_tokenize, word_tokenize

example_text='Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is Pinkish, You should not eat cardboard'
# tokenization by sentence
print(sent_tokenize(example_text))

# tokenization by words
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)