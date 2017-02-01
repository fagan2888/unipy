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
