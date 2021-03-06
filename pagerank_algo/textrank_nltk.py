

from nltk.corpus import brown, stopwords
from nltk.cluster.util import cosine_distance
from operator import itemgetter 
import numpy as np


def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences, stopwords=None):
    # Create an empty similarity matrix
    S = np.zeros((len(sentences), len(sentences)))
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue
            S[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)
    # normalize the matrix row-wise
    for idx in range(len(S)):
        S[idx] /= S[idx].sum()
 
    return S


def pagerank(A, eps=0.0001, d=0.85):
    P = np.ones(len(A)) / len(A)
    while True:
        new_P = np.ones(len(A)) * (1 - d) / len(A) + d * A.T.dot(P)
        delta = abs(new_P - P).sum()
        if delta <= eps:
            return new_P
        P = new_P


def textrank(sentences, top_n=5, stopwords=None):
    """
    sentences = a list of sentences [[w11, w12, ...], [w21, w22, ...], ...]
    top_n = how may sentences the summary should contain
    stopwords = a list of stopwords
    """
    S = build_similarity_matrix(sentences, stop_words) 
    sentence_ranks = pagerank(S)
 
    # Sort the sentence ranks
    ranked_sentence_indexes = [item[0] for item in sorted(enumerate(sentence_ranks), key=lambda item: -item[1])]
    #selected_sentences = sorted(ranked_sentence_indexes[:top_n])
    SELECTED_SENTENCES = sorted(ranked_sentence_indexes[:top_n])
    summary = itemgetter(*SELECTED_SENTENCES)(sentences)
    return summary 


if __name__ == "__main__":

   # Get a text from the Brown Corpus
   sentences = brown.sents('ca01')
   #print(sentences)

   # get the english list of stopwords
   stop_words = stopwords.words('english')
 
   S = build_similarity_matrix(sentences, stop_words)    
   #print(S) 

   summary = ''
   for idx, sentence in enumerate(textrank(sentences, stopwords=stopwords.words('english'))):
       #print("%s. %s" % ((idx + 1), ' '.join(sentence)))
       temp = ''.join(sentence)
       summary = summary + temp

   print("the summary is : ")
   print(summary)


