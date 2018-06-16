import nltk
from nltk.corpus import treebank
text17 = treebank.parsed_sents('wsj_0001.mrg')[0]
print(text17)

nltk.help.upenn_tagset('MD')

text11 = "Children shouldn't drink a sugary drink before bed."

text13 = nltk.word_tokenize(text11)

text15 = nltk.word_tokenize("Alice loves Bob")
print(text15)

grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP
NP -> 'Alice' | 'Bob'
V -> 'loves'
""")

print(grammar)

parser = nltk.ChartParser(grammar)
trees = parser.parse_all(text15)
for tree in trees:
    print(tree)


print(nltk.help.upenn_tagset())

print(text11.upper())
