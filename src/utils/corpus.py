'''
Captures corpus from filesystem.

created: 6 Aug 2022
last updated: 11 Aug 2022
author: matthew stachyra

TODO 
[x] scanforfiles() - test recursion
[x] readin() - test file contents is read
[ ] debug some directories getting added as files
[ ] save() - start an decide on save format (e.g., csv, parquet)
'''

# ---------basic function--------
# read in files with accepted extensions from specified entrypoint
# save files to csv or other format
# create embedding of corpus 
# make embedding available to search.py

# ---------updating corpus--------
# option 1: call `nava update` to read in file system, detect changes, and read corpus -- if this option, it may make sense to write that portion in c++ or rust
# option 2: call `nava -a <note>` and redo corpus / embedding generation

import os
from pathlib import Path

class Corpus:
    def __init__(self):
        # self.notes = ... # unknown what the best format is
        self.home = Path.home()
        self.dirs = ['Documents', 'Desktop'] # update this to scan other directories
        self.formats = {'txt', 'text', 'md', 'org', 'rtf', 'doc', 'pages'}
        self.filenames = []

    def scanforfiles(self, prevpath, currpath):
        # preorder traversal
        # continues scanning directories until files(leaves) reached

        # assumptions: (1) its either a directory or a file;
        # (2) only possibly relevant files will have '.' in the name
        filecheck = lambda x : '.' in x
        formatcheck = lambda x : x[x.rfind('.')+1:].lower() in self.formats 
        try:
            it = os.scandir(currpath)
            for i in it:
                # if its a file, append
                if formatcheck(i.name) and filecheck(i.name):
                    self.filenames.extend([os.path.join(currpath, i.name)])
                
                # otherwise recurse on the directory
                nextpath = os.path.join(currpath, i)
                prevpath = currpath
                self.scanforfiles(prevpath, nextpath)
            it.close()
        except Exception:
            # base case
            # it must be a file, append
            if formatcheck(currpath):
                self.filenames.extend([currpath])
        self.filenames= list(set(self.filenames))

    def readin(self):
        # this may need to be updated to detect the operating system
        # and have reasonable defaults for the filesystems in each
        # it may be useful to have a config file where the user can
        # specify the entrypoint folder as well as what kinds of files
        # to read in
        paths = [os.path.join(self.home, 'Documents'), 
                os.path.join(self.home, 'Desktop')]
        
        # add file names via preorder traversal of directories
        for p in paths:
            self.scanforfiles(self.home, p)

        # store file contents for embedding
        i = 0
        for f in self.filenames:
            with open(f, 'r') as file:
                contents = file.read()
                print(f"{i}      {f}")
                print(contents)
                print("\n")
                i += 1

    # def save(self):
        # TODO 
