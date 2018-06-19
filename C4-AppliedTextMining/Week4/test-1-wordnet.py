import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from nltk.collocations import *

# Path similarity
deer = wn.synset("deer.n.01")
elk = wn.synset("elk.n.01")
horse = wn.synset("horse.n.01")
print(deer)
print(elk)
print(horse)

print(deer.path_similarity(elk))

# Lin Similarity
brown_ic = wordnet_ic.ic("ic-brown.dat")
print(deer.lin_similarity(elk, brown_ic))
print(deer.lin_similarity(horse, brown_ic))

# Collocations

# bigram_measures = nltk.collocations.BigramAssocMeasures()
# finder = BigramCollocationFinder.from_words(text)
# finder.nbest(bigram_measures.pmi, 10)
# finder.apply_freq_filter(10)



