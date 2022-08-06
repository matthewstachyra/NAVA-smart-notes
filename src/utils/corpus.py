'''
Captures corpus from filesystem.

created: 6 Aug 2022
last updated: n/a
author: matthew stachyra

TODO 
[ ] readin() - test existing code
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
        self.formats = set('txt', 'text', 'md', 'org', 'rtf', 'doc', 'pages')

    def readin(self):
        # this may need to be updated to detect the operating system
        # and have reasonable defaults for the filesystems in each
        # it may be useful to have a config file where the user can
        # specify the entrypoint folder as well as what kinds of files
        # to read in
        fnames = list()
        paths = [os.path.join(self.home, 'Documents'), 
                os.path.join(self.home, 'Desktop')]

        # save files that have a permitted format
        fn = lambda x : x.lower() in self.formats 
        for path in paths:
            it = os.scandir(path)
            for f in it:
                if fn(f.name[f.name.rfind('.'):])]:
                    fnames.extend(f.name)
            it.close()

        # store files
        for file in files:
            with open(file, 'r') as f:
                contents = f.read()


    def save(self):
        # TODO 
        pass
