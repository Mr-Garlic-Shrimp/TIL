import numpy as np

# sampleデータはnumpyで渡す？それともdf？
def cost_func(theta, target_var, features):
    """
    args:
        theta: array like.parameter of regression
        target_var: array like.target variable
        features: array like.feature value.
    return value of cost function
    """
    # サンプルデータ数を定義
    m = len(target_var)
    # 1行m列の単位行列を定義
    ones  = np.ones((1, m))
    # MSE（残差の二乗和の平均）の計算
    mse = np.power( (target_var - (theta[0] + theta[1] * features)) , 2 ) / m
    return np.sum(mse)
    
    