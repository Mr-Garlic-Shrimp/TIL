from scipy import stats
import pandas as pd
import numpy as np

def cramers_v(x, y):
    '''
    x: array like
    y: array like
    return: Cramers's V(float)
    '''
    
    cont_table = pd.crosstab(x, y)
    chi, _, _, ex = stats.chi2_contingency(cont_table, correction=False)
    
    return np.sqrt(chi/((np.min(cont_table.shape)-1)*ex.sum()))
