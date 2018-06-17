import nltk
from nltk.stem import WordNetLemmatizer
import pandas as pd
import numpy as np
from nltk.book import FreqDist

# If you would like to work with the raw text you can use 'moby_raw'
with open('moby.txt', 'r') as f:
    moby_raw = f.read()

# If you would like to work with the novel in nltk.Text format you can use 'text1'
moby_tokens = nltk.word_tokenize(moby_raw)
text1 = nltk.Text(moby_tokens)


def example_one():
    return len(moby_tokens)  # or alternatively len(text1)


def example_two():
    return len(set(moby_tokens))  # or alternatively len(set(text1))


def example_three():
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(w,'v') for w in text1]

    return len(set(lemmatized))


def answer_one():
    return example_two() / float(example_one())


def answer_three():
    words = nltk.word_tokenize(moby_raw)
    dist = FreqDist(words)
    s = pd.Series(data=dist)
    s = s.sort_values(ascending=False)
    return list(zip(s.index,s))[:20]


def answer_four():
    words = nltk.word_tokenize(moby_raw)
    words_5 = [word for word in words if len(word) > 5]
    print(words_5[:20])
    dist = FreqDist(words_5)

    print(dist.items())


def answer_five():
    words = nltk.word_tokenize(moby_raw)
    lengths = [len(word) for word in words]
    maxindex = np.argmax(lengths)
    return  words[maxindex], lengths[maxindex]


def answer_six():
    words = nltk.word_tokenize(moby_raw)
    words = [word for word in words if word.isalpha()]
    dist = FreqDist(words)
    s = pd.Series(data=dist)
    s = s.sort_values(ascending=False)
    s = s.where(s > 2000).dropna()
    return list(zip(s,s.index))[:20]

answer_six()



answer_four()

