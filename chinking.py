import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize

# to train the punktsentencetokenizer 
train_text = state_union.raw("2005-GWBush.txt")

# to test for the trained tokenizer
sample_text = state_union.raw("2006-GWBush.txt")

# trained tokenizer will be stored
custom_sentence_tokenizer = PunktSentenceTokenizer(train_text)

# getting the tokenized sentence from the trained model
tokenized = custom_sentence_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            # creating a chunkgram
            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT|TO>+{"""
            chunkparser = nltk.RegexpParser(chunkGram)
            chunked = chunkparser.parse(tagged)
            chunked.draw()
    except Exception as e:
        print(e)

process_content()
