'''
Captures corpus from filesystem.

created: 6 Aug 2022
last updated: 10 Aug 2022
author: matthew stachyra

TODO 
[ ] scanforfiles() - test recursion
[ ] readin() - test file contents is read
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
        # this continues scanning directories until it finds files  
        formatcheck = lambda x : x.name[x.name.rfind('.'):].lower() in self.formats 
        filecheck = lambda x : '.' in x # simple assumptions (1) its either a directory or a file;
                                        # (2) only posibly relevant files will have '.' in the name
        it = os.scandir(currpath)
        for i in it:
            # if its a file, append
            if filecheck(i) and formatcheck(i):
                print(f"scanforfiles -- appending {i}")
                self.filenames.append(i.name)
            
            # otherwise recurse on the directory
            nextpath = os.path.join(currpath, i)
            prevpath = currpath
            print(f"scanforfiles -- recursing on {nextpath}")
            self.scanforfiles(prevpath, nextpath)
            it.close()


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
        for f in self.filenames:
            with open(f, 'r') as f:
                contents = f.read()


    def save(self):
        # TODO 
        pass
