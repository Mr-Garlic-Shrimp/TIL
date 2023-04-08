
# 変更履歴
# 10/7 実装。
# 10/8 thetaをリストで渡せるようにcost_funcを修正した。
# 10/9 パラメータを2Darrayで受け取るように変更。パラメタの全組み合わせの配列生成は必要に応じて関数外で行う実装とする。
# ---------------------------------------------------

import numpy as np

def cost_func(theta_array, target_var, features):
    """
    args:
        theta: 2Darray.Parametes of regression.
        target_var: 1Darray.Target variable.
        features: 2Darray.Feature values.
    return values of cost function
    """
    # 目的変数の数と特徴量1種類あたりの数が等しくなければエラーメッセージを返す。
    if len(target_var) != len(features):
        print("Error: Invalid args")
        exit()
    
    # featuresが1次元配列であれば、1行m列の2次元配列にする
    # そうでなければ転置する
    m = len(target_var)
    if features.ndim == 1:
        features = features.reshape(1, m)
    else:
        features = features.T
        
    # 1行m列の単位行列を定義
    ones  = np.ones((1, m))
    # 特徴量の配列の1行目にonesを結合
    features_array = np.concatenate([ones,features])
    
    # 残差の二乗の計算。線形回帰モデルの式を行列の積で表している。
    sq_errors = (target_var - np.dot(theta_array, features_array)) ** 2
    # mseを返す
    return sq_errors.mean(axis=1)
    
    