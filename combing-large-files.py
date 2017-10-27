#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 17:47:48 2017

@author: emg
"""

import pandas as pd
import glob 
import os

dtypes = {
        'archived': 'str',
        'author_flair_text': 'str',
        'name': 'str',
        'score_hidden': 'str'
        }

#path = '/Users/emg/Programming/GitHub/aws/raw_data'
path = os.getcwd()
files = glob.glob(path + "/td-all-comments000000000*")
dfs = []
for f in files:
    print(f)
    df = pd.read_csv(f,index_col=None, header=0, dtype=dtypes)
    dfs.append(df)
    
all_comments = pd.concat(dfs)

all_comments.to_csv('/Users/emg/Programming/GitHub/aws/s3/td-all-comments.csv')
