# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 01:08:15 2021

@author: PHILFIXE
"""
import pandas as pd
import pickle
# Create database connection object

with open('df_indices', 'rb') as f:
    indices = pickle.load(f)
    
with open('df_uid_name', 'rb') as f:
    df = pickle.load(f)