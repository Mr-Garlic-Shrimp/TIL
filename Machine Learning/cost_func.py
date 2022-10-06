import numpy as np

# インターフェースは2次元配列で統一する。
def cost_func(theta, target_var, features):
    """
    args:
        theta: array like.parameter of regression
        target_var: 1Darray.target variable
        features: NDarray.feature values.
    return value of cost function
    """
    # サンプルデータ数を定義
    m = len(target_var)
    # target_varをm行1列にreshape
    target_var_matrix = target_var.reshape(m, 1)    
    
    # featuresが1次元配列であれば、1行m列の2次元配列にする
    # そうでなければ転置する
    if features.ndim == 1:
        features = features.reshape(1, m)
    else:
        features = features.T
        
    # 1行m列の単位行列を定義
    ones  = np.ones((1, m))
    # 特徴量の配列の1行目にonesを結合
    ones_features = np.concatenate([ones,features])
    
    # 残差の二乗の計算
    sq_errors = (target_var_matrix - np.dot(ones_features.T, theta.T)) ** 2
    # mseの算出
    mse = np.mean(sq_errors)
    return mse
    
    