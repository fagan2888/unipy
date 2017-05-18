# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 05:03:19 2017

@author: Young Ju Kim
"""

import pandas as pd
import tarfile
from os.path import dirname, abspath


def init():
    filepath = dirname(abspath(__file__))
    filename = filepath + '/resources.tar.gz'
    tar = tarfile.open(filename)
    tar.extractall(filepath)
    tar.close()


def reset():
    filepath = dirname(abspath(__file__))
    filename = filepath + '/resources.tar.gz'
    tar = tarfile.open(filename)
    tar.extractall(filepath)
    tar.close()


def datalist():

    filepath = dirname(abspath(__file__))
    filename = filepath + '/resources.tar.gz'
    tar = tarfile.open(filename)
    filelist = list(set(map(lambda x: x.split('/')[0], tar.getnames())))
    filelist.sort()

    return filelist


def load(filename):

    data = _get_data(filename)

    return data


def _get_data(filename):

    filepath = dirname(abspath(__file__))
    file = filepath + '/{}/{}.data'.format(filename, filename)
    data = pd.read_csv(open(file, 'rb'), sep=",")

    return data
