#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:41:13 2018

@author: josephhiggins
"""

# https://github.com/HazyResearch/snorkel/blob/master/tutorials/intro/Intro_Tutorial_1.ipynb

import os

# TO USE A DATABASE OTHER THAN SQLITE, USE THIS LINE
# Note that this is necessary for parallel execution amongst other things...
# os.environ['SNORKELDB'] = 'postgres:///snorkel-intro'

from snorkel import SnorkelSession
session = SnorkelSession()

# Here, we just set how many documents we'll process for automatic testing- you can safely ignore this!
n_docs = 500 if 'CI' in os.environ else 2591

from snorkel.parser import TSVDocPreprocessor

path = '/Users/josephhiggins/Documents/open_source_tools/snorkel/tutorials/intro/data/articles.tsv'
doc_preprocessor = TSVDocPreprocessor(path, max_docs=n_docs)


#import pandas as pd
#df = pd.DataFrame.from_csv(path, sep = '\t')


from snorkel.parser.spacy_parser import Spacy
from snorkel.parser import CorpusParser

corpus_parser = CorpusParser(parser=Spacy())
corpus_parser.apply(doc_preprocessor, count=n_docs)

from snorkel.models import Document, Sentence

print("Documents:", session.query(Document).count())
print("Sentences:", session.query(Sentence).count())

#dir(session.query(Document).column_descriptions)
#session.query(Document).limit(5).all()
#session.query(Sentence).limit(5).all()

from snorkel.models import candidate_subclass

Spouse = candidate_subclass('Spouse', ['person1', 'person2'])
