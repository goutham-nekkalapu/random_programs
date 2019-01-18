
"""
implementation of a simple pagerank algo 
"""
import numpy as np


links = {
    'webpage-1': set(['webpage-2', 'webpage-4', 'webpage-5', 'webpage-6', 'webpage-8', 'webpage-9', 'webpage-10']),
    'webpage-2': set(['webpage-5', 'webpage-6']),
    'webpage-3': set(['webpage-10']),
    'webpage-4': set(['webpage-9']),
    'webpage-5': set(['webpage-2', 'webpage-4']),
    'webpage-6': set([]), # dangling page
    'webpage-7': set(['webpage-1', 'webpage-3', 'webpage-4']),
    'webpage-8': set(['webpage-1']),
    'webpage-9': set(['webpage-1', 'webpage-2', 'webpage-3', 'webpage-8', 'webpage-10']),
    'webpage-10': set(['webpage-2', 'webpage-3', 'webpage-8', 'webpage-9']),
}


def build_index(links):
    website_list = links.keys()
    return {website: index for index, website in enumerate(website_list)}


def build_transition_matrix(links, index):
    total_links = 0
    A = np.zeros((len(index), len(index)))
    for webpage in links:
        # dangling page
        if not links[webpage]:
            # Assign equal probabilities to transition to all the other pages
            A[index[webpage]] = np.ones(len(index)) / len(index)
        else:
            for dest_webpage in links[webpage]:
                total_links += 1
                A[index[webpage]][index[dest_webpage]] = 1.0 / len(links[webpage])
 
    return A


def pagerank(A, eps=0.0001, d=0.85):
    P = np.ones(len(A)) / len(A)
    while True:
        new_P = np.ones(len(A)) * (1 - d) / len(A) + d * A.T.dot(P)
        delta = abs(new_P - P).sum()
        if delta <= eps:
            return new_P
        P = new_P 



website_index = build_index(links)
print(website_index)

A = build_transition_matrix(links, website_index)
#print(A) 

results = pagerank(A)
print("Results:", results) 
print(sum(results)) 
print([item[0] for item in sorted(enumerate(results), key=lambda item: -item[1])])

