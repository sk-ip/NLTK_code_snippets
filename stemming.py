# i was taking a ride in the car
# i was riding in the car
# same meaning, so why waste storage resources to save ride and riding, only save ride, it can be done through stemming

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
example_words = ['python','pythoning','pythoner','pythonly','pythoned','pythoncomer','pythoners','pythonpiper','pythonoid','pythonmania']

for w in example_words:
    print(ps.stem(w))

new_text='it is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly atleast once'
words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))