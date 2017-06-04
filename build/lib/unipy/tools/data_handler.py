# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:41:19 2017

@author: Young Ju Kim
"""


# Split an iterable by equal length
import collections
import itertools as it
import numpy as np

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
def uniquePair(*args):

    argsTuple = (*args, )

    for _ in range(len(argsTuple)):
        isinstance(_, collections.Iterable)

    resList = list(set(zip(*args)))
    
    return resList


# %% Item Transformator
def map_to_tuple(iterable):

    isinstance(iterable, collections.Iterable)
    res = tuple(map(lambda item: tuple(item), iterable))

    return res

def map_to_list(iterable):

    isinstance(iterable, collections.Iterable)
    res = list(map(lambda list: tuple(item), iterable))

    return res


