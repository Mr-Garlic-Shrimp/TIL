import numpy as np
from scipy import stats

def cohens_d(x,y):
    
    '''
    args:
        x,y: array like
    
    return:
        (cohen's d, sigma_hat)
    '''
    nx = len(x)
    ny = len(y)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    # 標本x,yの母集団に共通の不偏分散の平方根を計算
    sigma_hat = np.sqrt( ((nx-1)*stats.tvar(x) + (ny-1)*stats.tvar(y)) / 
                (nx + ny - 2) )
    
    return np.abs((x_mean - y_mean)) / sigma_hat , sigma_hat