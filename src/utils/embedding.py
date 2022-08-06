'''
Embedding text for storage and search in NotesDB.

created: 20 July 2022
last updated: 6 Aug 2022
author: matthew stachyra

TODO
[ ] enable to read in corpus using Corpus class
'''

from sentence_transformers import SentenceTransformer, util

from . import Corpus


class Embed:
    def __init__(self):
        # self.corpus = Corpus(...)
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = embedder.encode(self.corpus, convert_to_tensor=True)

    def __call__(self):
        return self.embeddings
