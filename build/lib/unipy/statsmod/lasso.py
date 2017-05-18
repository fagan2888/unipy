import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso

def lassFunction(data, thresh=2-):
    data = data.copy()
    
    # Generate an alias list: [x_1, ..., x_n]
    colBackup = data.columns.copy()
    predictors = ['x_%d'%i for i in range(1, data.shape[1])]
    dataAlias = predictors + ['y']
    
    # Generate an alias-variable Match Table
    matchTbl = pd.DataFrame({'alias': dataAlias, 'var_name': colBackup})
    
    # Change Columns to Alias
    data.columns = dataAlias
    
    # Generate Alphas for Lasso
    alpha = np.arange(.00001, .1, .001)
    
    # Generate A Result Table
    col = ['rss', 'intercept'] + ['coef_' + x for x in predictors]
    ind = ['alpha_%.2g'%alpha[i] for i in range(len(alpha))]
    coefMatrix = pd.DataFrame(index=ind, columns=col)
    predict = {}
    
    # Defining a Lasso generic function
    def lassoRegression(data, predictors, alpha):
    
        # Fit to the model
        lassoReg = Lasso(alpha=alpha, normalize=True, max_iter=1e5)
        lassoReg.fit(data[predictors], data['y'])
        yPredict = lassoReg.predict(data[predictors])
    
        # Return the result in pre-defined format
        rss = sum((yPredict - data['y']) ** 2)
        ret = [rss]
        ret.extend([lassoReg.intercept_])
        ret.extend(lassoReg.coef_)
    
        return ret, yPredict
    
    # Iterate over the alpha values
    for _ in range(len(alpha)):
        coefMatrix.iloc[_, ], pred = lassoRegression(data, predictors, alpha[_])
        predict[ind[_]] = pred
        
    coefMatrix['var_count'] = coefMatrix.apply(np.count_nonzero, axis=1) - 2
    
    # Filter by thresh >= var_count
    filtered = coefMatrix[coefMatrix['var_count'] <= thresh].iloc[0]
    
    # Get Predicted Y value
    alphaVal = filtered.name
    predictedY = predict[alpahVal]
    
    # Get a Rank Table
    lassoVal = filtered[np.nonzero(filtered)[0].tolist()][2:-1]
    filteredTbl = pd.DataFrame({'lasso_coef': lassoVal,
                                'abs_coef': abs(lassoVal)})
    filteredTbl = filteredTbl.sort_values(by='abs_coef', ascending=False)
    filteredTbl = filteredTbl.reset_index()
    filteredTbl['index'] = filteredTbl['index'].str[5:]
    
    filteredTbl = filteredTbl.merge(matchTbl, left_on='index', right_on='alias')
    filteredTbl['rank'] = range(1, len(filtTbl) + 1)
    rankTbl = filteredTbl[['rank', 'var_name', 'lasso_coef', 'abs_coef']]
    
    # Plots
    fig = plt.figure(figsize=(12, 9))
    title = 'Top {} variables : absolute coefficient by Lasso'.format(len(filteredTbl))
    rankTbl.set_index('var_name')['abs_coef'].plot(kind='barh')
    fig.suptitle(title, fontsize=14, fontweight='bold')
    plt.tight_layout(pad=5)
    
    return rankTbl, coefMatrix, matchTbl, predictedY
    
ranked, lsCoef, prmTbl, predicted = lassoFunction(pvTbl)
