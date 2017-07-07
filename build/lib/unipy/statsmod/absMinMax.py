# -*- conding: utf-8 -*-
"""
Created on Mon Jun 12 09:36:25 2017

@author: Young Ju Kim
"""


import pandas as pd


def absmax(DataFrame, axis=0):
    
    idxDict = DataFrame.abs().idxmax(axis=axis).dropna().to_dict()
    resSeries = pd.Series({col: DataFrame.loc[val, col] for col, val in idxDict.items()})
    
    return resSeries


def absmin(DataFrame, axis=0):
    
    idxDict = DataFrame.abs().idxmin(axis=axis).dropna().to_dict()
    resSeries = pd.Series({col: DataFrame.loc[val, col] for col, val in idxDict.items()})
    
    return resSeries


