
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

__all__ = ['point_boxplot',
           'point_grid_boxplot']


def point_boxplot(value, by=None, data=None, dotcolor='b.', spread=.3, *args, **kwargs):

    flierprops = dict(marker='o', markerfacecolor='white', alpha=1., markersize=5, linestyle='none', markeredgewidth=.7)

    plot = data.boxplot(value, by=by, rot=90, flierprops=flierprops, showfliers=True, showmeans=True, *args, **kwargs)

    pvt = pd.pivot_table(data, index=data.index, columns=by, values=value)

    for i in range(pvt.shape[1]):
        y = pvt[pvt.columns[i]]
        x = np.random.normal(i+1, spread/pvt.shape[1], len(y))
        plt.plot(x, y, dotcolor, alpha=.2)

    return plot


def point_grid_boxplot(value, by=None, data=None, dotcolor='b.', spread=.3, direction='vertical', *args, **kwargs):

    flierprops = dict(marker='o', markerfacecolor='white', alpha=1., markersize=5, linestyle='none', markeredgewidth=.7)

    grp_cnt = data[by].drop_duplicates().shape[0]

    # Grid Directions
    if direction in ('vertical', 'v'):
        fig, axes = plt.subplots(nrows=grp_cnt, ncols=1)
    elif direction in ('horizontal', 'h'):
        fig, axes = plt.subplots(nrows=1, ncols=grp_cnt)

    data.boxplot(value, by=by, rot=90, flierprops=flierprops, showfliers=True, showmeans=True, *args, **kwargs)

    pvt = pd.pivot_table(data, index=data.index, columns=by, values=value)

    for i in range(pvt.shape[1]):
        y = pvt[pvt.columns[i]]
        x = np.random.normal(i+1, spread/pvt.shape[1], len(y))
        plt.plot(x, y, dotcolor, alpha=.2)

    return plot