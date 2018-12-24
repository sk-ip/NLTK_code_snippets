from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sentence = 'exapmle showing stop words filteraion, to filter out stop words from this text'
stop_words=set(stopwords.words('english'))
# to actually view the stopwords in the english
print(stop_words)

words=word_tokenize(sentence)
filtered_sentence=[]

# good way of doing so everybody could understand it
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

# another way , more complex onr-liner
filtered_sentence2=[]
filtered_sentence2=[w for w in words if not w in stop_words]
print(filtered_sentence2) 
