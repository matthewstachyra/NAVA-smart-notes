'''
Embedding text for storage and search in NotesDB.

created: 20 July 2022
last updated: n/a
author: matthew stachyra
'''

from sentence_transformers import SentenceTransformer, util


class Embed:
    def __init__(self, corpus):
        self.corpus = corpus
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = embedder.encode(self.corpus, convert_to_tensor=True)

    def __call__(self):
        return self.embeddings
