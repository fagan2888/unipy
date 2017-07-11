# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:41:19 2017

@author: Young Ju Kim
"""


import os
import pandas as pd

# Split an iterable by equal length
import collections
import itertools as it
import numpy as np

__all__ = ['splitter',
           'pair_unique',
           'df_pair_unique',
           'map_to_tuple',
           'map_to_list',
           'merge_csv']


# A Function to split an Iterable into smaller chunks 
def splitter(iterable, how='equal', size=2):
    
    isinstance(iterable, collections.Iterable)
    isinstance(size, int)
    
    if not size > 0:

        raise ValueError("'size' must be greater than 0")

    else:
        
        if how == 'equal':

            resList = np.array_split(iterable, (len(iterable) / size) + 1)
            
            return resList
        
        elif how == 'remaining':

            tmpIterator = iter(iterable)
            splitted = iter(lambda: tuple(it.islice(tmpIterator, size)), ())
            resList = list(splitted)
            
            return resList


# Unique Pair List Creator
def pair_unique(*args):

    argsTuple = (*args, )

    for _ in range(len(argsTuple)):
        isinstance(_, collections.Iterable)

    resList = list(set(zip(*args)))
    
    return resList


# Unique Pair List Creator For DataFrame
def df_pair_unique(dataFrame, colList):
    
    argsTupleMap = dataFrame[colList].itertuples(index=False)
    resList = list(set(tuple(idx) for idx in argsTupleMap))
    return resList

# %% Item Transformator
def map_to_tuple(iterable):

    isinstance(iterable, collections.Iterable)
    res = tuple(map(lambda item: tuple(item), iterable))

    return res

def map_to_list(iterable):

    isinstance(iterable, collections.Iterable)
    res = list(map(lambda item: tuple(item), iterable))

    return res


# %% Data Concatenator within a Folder
def merge_csv(filePath, ext='.csv', sep=',', if_save=True, saveName=None, low_memory=True):
    if filePath[-1] != '/':
        filePath = filePath + '/'
    fileList = os.listdir(filePath)
    dataList = [name for name in fileList if name.find(ext) != -1]

    resFrame = pd.DataFrame()
    for _ in dataList:
        eachName = filePath + _
        eachFile = pd.read_csv(eachName, sep=sep, low_memory=low_memory)
        resFrame = resFrame.append(eachFile, ignore_index=True)

    if if_save == True:
        resFrame.to_csv(saveName, header=True, index=False)

    return resFrame

