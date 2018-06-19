import numpy as np
import pandas as pd
import nltk
from nltk.corpus import wordnet as wn

def convert_tag(tag):
    """Convert the tag given by nltk.pos_tag to the tag used by wordnet.synsets"""

    tag_dict = {'N': 'n', 'J': 'a', 'R': 'r', 'V': 'v'}
    try:
        return tag_dict[tag[0]]
    except KeyError:
        return None


def doc_to_synsets(doc):
    """
    Returns a list of synsets in document.

    Tokenizes and tags the words in the document doc.
    Then finds the first synset for each word/tag combination.
    If a synset is not found for that combination it is skipped.

    Args:
        doc: string to be converted

    Returns:
        list of synsets

    Example:
        doc_to_synsets('Fish are nvqjp friends.')
        Out: [Synset('fish.n.01'), Synset('be.v.01'), Synset('friend.n.01')]
    """
    synsets = []
    token = nltk.word_tokenize(doc)
    tag = nltk.pos_tag(token)
    converted = [(i[0], convert_tag(i[1])) for i in tag]
    for curr in converted:
        curr_synsets = wn.synsets(curr[0], curr[1])
        if len(curr_synsets) > 0:
            synsets.append(curr_synsets[0])
    return synsets


def similarity_score(s1, s2):
    """
    Calculate the normalized similarity score of s1 onto s2

    For each synset in s1, finds the synset in s2 with the largest similarity value.
    Sum of all of the largest similarity values and normalize this value by dividing it by the
    number of largest similarity values found.

    Args:
        s1, s2: list of synsets from doc_to_synsets

    Returns:
        normalized similarity score of s1 onto s2

    Example:
        synsets1 = doc_to_synsets('I like cats')
        synsets2 = doc_to_synsets('I like dogs')
        similarity_score(synsets1, synsets2)
        Out: 0.73333333333333339
    """

    simis = []

    for a in s1:
        curr = [a.path_similarity(b) for b in s2 if a.path_similarity(b) is not None]
        if len(curr) != 0:
            simis.append(np.max(curr))

    return np.average(simis)


def document_path_similarity(doc1, doc2):
    """Finds the symmetrical similarity between doc1 and doc2"""

    synsets1 = doc_to_synsets(doc1)
    synsets2 = doc_to_synsets(doc2)

    return (similarity_score(synsets1, synsets2) + similarity_score(synsets2, synsets1)) / 2


def test_document_path_similarity():
    doc1 = 'This is a function to test document_path_similarity.'
    doc2 = 'Use this function to see if your code in doc_to_synsets and similarity_score is correct!'
    return document_path_similarity(doc1, doc2)


paraphrases = pd.read_csv('paraphrases.csv')


def most_similar_docs():
    paraphrases["scores"] = [document_path_similarity(row["D1"], row["D2"]) for index, row in paraphrases.iterrows()]
    return tuple(paraphrases.loc[paraphrases['scores'].idxmax()])[1:]


def label_accuracy():
    from sklearn.metrics import accuracy_score
    paraphrases["scores"] = [document_path_similarity(row["D1"], row["D2"]) for index, row in paraphrases.iterrows()]
    paraphrases["label"] = (paraphrases["scores"] > 0.75).astype(int)
    print(paraphrases)
    return accuracy_score(paraphrases["Quality"], paraphrases["label"])


print(label_accuracy())

