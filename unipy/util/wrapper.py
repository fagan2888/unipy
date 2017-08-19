# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:33:36 2017

@author: Young Ju Kim
"""


from datetime import datetime as dt
from functools import wraps

__all__ = ['time_profiler',
           'job_wrapper']


def time_profiler(func):

    @wraps(func)
    def profiler(*args, **kwargs):

        start_tm = dt.now()
        print("JobStart :", start_tm)

        res = func(*args, **kwargs)

        end_tm = dt.now()
        print("JobEnd   :", end_tm)

        elapsed_tm = end_tm - start_tm
        print("Elapsed  :", elapsed_tm)

        return res

    return profiler



def job_wrapper(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        # Message Length = 40 + 2 (\n)
        dash_len = int((40 - len(func.__name__) - 12) / 2)
        
        start_msg = '-'*dash_len + ' [{}] START '.format(func.__name__) + \
                    '-'*dash_len + '\n'
        print(start_msg)
        start_tm = dt.now()

        res = func(*args, **kwargs)

        end_tm = dt.now()
        end_msg = '-'*dash_len + '  [{}] END  '.format(func.__name__) + \
                  '-'*dash_len + '\n'
        print(end_msg)
        print("{} :".format(func.__name__), end_tm - start_tm, '\n')
                
        return res

    return wrapper


