# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 20:55:26 2017

@author: Young Ju Kim
"""

#%% Sample datasets

from unipy.sample.datasets import dataManager

# Extract Datasets for the first time
dataManager.init()

# Reset Datasets
dataManager.reset()

# Get a Dataset list
dataManager.datalist()

# Load Datasets
wine1 = dataManager.load('winequality_red')
wine2 = dataManager.load('winequality_white')

#%% VIF

from unipy.statsmod.multivariates import feature_selection_vif as fsv

res, drp = fsv(wine1, thresh=5.0)
