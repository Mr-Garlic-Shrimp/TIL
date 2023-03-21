import pandas as pd
import numpy as np
from sklearn import tree

class MyGradientBoostingDecisionTreeRegressor:
    def __init__(self, learning_rate=0.03, n_iteration=100, max_depth=1, random_state=0):
        self.learning_rate = learning_rate
        self.n_iteration = n_iteration
        self.max_depth = max_depth
        self.random_state = random_state
    
    def fit(self, X, y):
        # 最初のモデルと残差を定義。最初は目的変数yの平均値を予測値とする。
        # self.f0 = np.full((len(y),1), np.mean(y))　→ yを2次元にする必要はなし
        # 下記では全要素がy.mean()の配列fを作成しているが、スカラーのままでもブロードキャストされるので問題ない。
        self.y_mean = y.mean()
        f = np.full(len(y), y.mean())
        r = y - f
        # 学習済みモデル格納用
        self.models = []

        for _ in range(self.n_iteration):
            # 決定木のインスタンス生成、学習、学習済みモデル格納
            model = tree.DecisionTreeRegressor(max_depth=self.max_depth, random_state=self.random_state)
            model.fit(X, r)
            self.models.append(model)
            # それまでの予測結果とこのモデルの予測結果を足し合わせる
            f += self.learning_rate * model.predict(X)
            # 残差を更新
            r = y - f
            
    def predict(self, X_test):
        # 初期の予測値はテストデータと同じシェイプにする必要あり。
        result = self.y_mean
        for model in self.models:
            result += self.learning_rate * model.predict(X_test)

        return result

