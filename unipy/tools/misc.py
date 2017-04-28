#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:05:27 2017

@author: dawkiny
"""

import itertools


def splitor(iterable, size):

    data = iter(iterable)
    item = list(itertools.islice(data, size))

    while item:
        yield item
        item = list(itertools.islice(data, size))


def exceptor(x, exceptlist):
    
    res = [member for member in x if member not in exceptlist]
    
    return res
    
###
# list(filter(lambda col: col not in ['capital_gain'], test.columns))
# [member for member in test.columns if member not in ['capital_gain']]
