# 変更履歴
# 10/9 実装。2次元しか対応していない。numpy演算に閉じてるので、講義の実装（リスト内包表記による計算）より明らかに早い。
# 　　偏微分係数は微分係数の定義から求めた方が汎用性がある。どこかで実装する。
# ---------------------------------------------------

import numpy as np

def grad_descent(theta_init, target_var, features, alpha=0.00005, epochs=100000):
    """
    args:
        theta_init: 1Darrays.Initial parametes of regression.
        target_var: 1Darray.Target variable.
        features: 1D or 2Darray.Feature values.
        alpha: Learning rate.
        epochs: number of iterations
    return optimized parameters(tuple), history of parameters calculation(list of tuple) 
    """
    # m: サンプルデータ数
    # theta_history: イテレーションにより更新したパラメタを保存するためのリスト
    m = len(target_var)
    theta_history = [tuple(theta_init)]
    
    if features.ndim == 1:
        features = features.reshape(1, m)
    else: 
        features = features.T
        
    # 1行m列の単位行列を定義
    ones  = np.ones((1, m))
    # 特徴量の配列の1行目にonesを結合
    features_array = np.concatenate([ones,features])
    
    # thetaの初期化。そのままでは参照渡しになってしまうので、copy()で渡す
    theta = theta_init.copy()
    
    for _ in range(epochs):
        # thetaごとに損失関数の偏微分係数(partial derivative)を計算
        pdev_L_theta_0 = 2 * (np.dot(theta, features_array) - target_var).mean()
        pdev_L_theta_1 = 2 * ((np.dot(theta, features_array) - target_var) * features).mean()
        
        # thetaを更新して、その履歴を保存。配列ごと計算することで、theta_0,theta_1の更新前更新後を気にせずに同時に計算できる。
        theta -= alpha * np.array([pdev_L_theta_0, pdev_L_theta_1])
        theta_history.append(tuple(theta))
    
    # 最後のパラメタの値とパラメタの履歴リストを返す。
    return theta_history[-1], theta_history