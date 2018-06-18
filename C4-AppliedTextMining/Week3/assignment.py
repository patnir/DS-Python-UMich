import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC


spam_data = pd.read_csv('spam.csv')

spam_data['target'] = np.where(spam_data['target']=='spam',1,0)

X_train, X_test, y_train, y_test = train_test_split(spam_data['text'], spam_data['target'], random_state=0)


def answer_one():
    return np.count_nonzero(spam_data["target"] == 1) / len(spam_data) * 100


def answer_two():
    vect = CountVectorizer().fit(X_train)
    feature_names = vect.get_feature_names()
    max_token = pd.Series(list(map(len, feature_names))).argmax()
    return feature_names[max_token]


def answer_three():
    vect = CountVectorizer().fit(X_train)
    X_train_vectorized = vect.transform(X_train)
    model = MultinomialNB(alpha=0.1).fit(X_train_vectorized, y_train)
    predictions = model.predict(vect.transform(X_test))
    return roc_auc_score(y_test, predictions)


def answer_four():
    vect = TfidfVectorizer().fit(X_train)
    X_train_vectorized = vect.transform(X_train)
    tfdif_indices = X_train_vectorized.max(0).toarray()[0]
    features_series = pd.Series(tfdif_indices, index=vect.get_feature_names())

    return features_series.nsmallest(20), features_series.nlargest(20)

'''
Fit and transform the training data X_train using a Tfidf Vectorizer ignoring terms that have a document frequency strictly lower than 3.
Then fit a multinomial Naive Bayes classifier model with smoothing alpha=0.1 and compute the area under the curve (AUC) score using the transformed test data.

'''
def answer_five():
    vect = TfidfVectorizer(min_df=3).fit(X_train, y_train)
    X_train_vectorized = vect.transform(X_train)
    model = MultinomialNB(alpha=0.1)
    model.fit(X_train_vectorized, y_train)
    predictions = model.predict(vect.transform(X_test))
    return roc_auc_score(y_test, predictions)


def answer_six():
    spam_label = spam_data[spam_data["target"] == 1]
    not_spam_label = spam_data[spam_data["target"] == 0]
    spam_length = np.average([len(text) for text in spam_label["text"]])
    not_spam_length = np.average([len(text) for text in not_spam_label["text"]])
    return not_spam_length, spam_length


def add_feature(X, feature_to_add):
    """
    Returns sparse feature matrix with added feature.
    feature_to_add can also be a list of features.
    """
    from scipy.sparse import csr_matrix, hstack
    return hstack([X, csr_matrix(feature_to_add).T], 'csr')


def answer_seven():
    vect = TfidfVectorizer(min_df=5).fit(X_train, y_train)
    X_train_vectorized = vect.transform(X_train)
    X_test_vectorized = vect.transform(X_test)

    X_train_len = X_train.apply(len)
    X_test_len = X_test.apply(len)

    X_train_aug = add_feature(X_train_vectorized, X_train_len)
    X_test_aug = add_feature(X_test_vectorized, X_test_len)

    model = SVC(C=10000)
    model.fit(X_train_aug, y_train)

    predictions = model.predict(X_test_aug)

    return roc_auc_score(y_test, predictions)


def get_numerics(text):
    total = 0
    for word in text.split(" "):
        if word.isnumeric():
            total += len(word)
    return total


def answer_eight():
    spam_digits_avg = spam_data.loc[spam_data['target'] == 1, 'text'].str.count('\d').mean()
    not_spam_digits_avg = spam_data.loc[spam_data['target'] == 0, 'text'].str.count('\d').mean()

    return (not_spam_digits_avg, spam_digits_avg)


def  answer_ten ():
    spam_label = spam_data.loc[spam_data['target'] == 1,'text'].str.count('\W').mean()
    not_spam_label = spam_data.loc[spam_data['target'] == 0,'text'].str.count('\W').mean()
    return (not_spam_label, spam_label)

print(answer_seven())




