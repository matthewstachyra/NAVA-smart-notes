'''
Search embedding space.

created: 20 July 2022
last updated: n/a
author: matthew stachyra


TODO
[ ] figure out how to access corpus within search - do we have a NAVA class?
'''

from sentence_transformers import SentenceTransformer, util


class Search:
    def __init__(self, query, corpus):
        self.query = query
        self.db = NotesDB


    def __call__(self, top_k=5):
        return util.semantic_search(query_embedding,
                                    corpus_embeddings,
                                    top_k=top_k,
                                    score_function=util.dot_score)

# to incorporate below
# print(corpus[hits[0][0]['corpus_id']])
