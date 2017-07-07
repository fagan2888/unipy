
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

__all__ = ['point_boxplot']


def point_boxplot(value, by=None, data=None, dotcolor='b.'):

    flierprops = dict(marker='o', markerfacecolor='white', alpha=1., markersize=5, linestyle='none', markeredgewidth=.7)

    plot = data.boxplot(value, by=by, rot=90, flierprops=flierprops, showfliers=True, showmeans=True)

    pvt = pd.pivot_table(data, index=data.index, columns=by, values=value)

    for i in range(pvt.shape[1]):
        y = pvt[pvt.columns[i]]
        x = np.random.normal(i+1, 1./pvt.shape[1], len(y))
        plt.plot(x, y, dotcolor, alpha=.2)

    return plot
