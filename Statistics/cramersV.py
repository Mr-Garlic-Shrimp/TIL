from scipy import stats
import pandas as pd
import numpy as np

def cramers_v(x, y):
    '''
    x: array like
    y: array like
    return: Cramers's V(float)
    '''
    # 引数の配列から分割表を作成
    cont_table = pd.crosstab(x, y)
    # カイ二乗値と期待度数の分割表のみ取得
    chi2, _, _, ex = stats.chi2_contingency(cont_table, correction=False)
    n = ex.sum()
    min_table_shape = np.min(cont_table.shape)-1
    return np.sqrt(chi2/(min_table_shape*n))
