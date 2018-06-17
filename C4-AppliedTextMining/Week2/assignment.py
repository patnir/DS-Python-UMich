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
    dist = FreqDist(moby_tokens)
    s = pd.Series(data=dist)
    s = s.sort_values(ascending=False)
    return list(zip(s.index,s))[:20]


def answer_four():
    words_5 = [word for word in moby_tokens if len(word) > 5]
    print(words_5[:20])
    dist = FreqDist(words_5)
    print(dist.items())


def answer_five():
    lengths = [len(word) for word in moby_tokens]
    maxindex = np.argmax(lengths)
    return  words[maxindex], lengths[maxindex]


def answer_six():
    words = [word for word in moby_tokens if word.isalpha()]
    dist = FreqDist(words)
    s = pd.Series(data=dist)
    s = s.sort_values(ascending=False)
    s = s.where(s > 2000).dropna()
    return list(zip(s,s.index))[:20]


def answer_seven():
    sentences = nltk.sent_tokenize(moby_raw)
    words = list(map(nltk.word_tokenize, sentences))
    lengths = list(map(len, words))

    return np.average(lengths)


def answer_eight():
    pos = nltk.pos_tag(moby_tokens)
    dist = FreqDist(np.array(pos)[:, 1])
    s = pd.Series(data=dist)
    s = s.sort_values(ascending=False)
    return list(zip(s.index, s))[:5]


from nltk.corpus import words

correct_spellings = words.words()
print(correct_spellings)


def answer_nine(entries=['cormulent', 'incendenece', 'validrate']):
    from nltk.metrics.distance import (edit_distance, jaccard_distance)
    from nltk.util import ngrams

    df = pd.Series(data=correct_spellings)
    words = [word for word in df if word.startswith(entries[0][0])]
    res = []
    for entry in entries:
        words = [word for word in df if word.startswith(entry[0])]
        distances = ((jaccard_distance(set(ngrams(entry, 3)),
                                       set(ngrams(word, 3))), word)
                     for word in words)

        closest = min(distances)

        res.append(closest[1])
    return res


answer_nine()

