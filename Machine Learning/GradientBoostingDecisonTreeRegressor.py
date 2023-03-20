import pandas as pd
import numpy as np
from sklearn import tree

class GradientBoostingDecisionTreeRegressor:
    def __init__(self, learning_rate=0.1, n_iteration=100, max_depth=1, random_seed=0):
        self.learning_rate = learning_rate
        self.n_iteration = n_iteration
        self.max_depth = max_depth
        self.random_seed = random_seed
    
    def fit(self, X, y):
        # 学習データをnumpyに変換
        # X = np.array(X)
        # y = np.array(y)

        # 最初のモデルと残差を定義。最初は目的変数yの平均値を予測値とする。
        # self.f0 = np.full((len(y),1), np.mean(y))　→ yを2次元にする必要はなし
        self.y_mean = y.mean()
        self.f = np.full(len(y), y.mean())
        self.r = y - self.f
        # 学習済みモデル格納用
        self.models = []

        for _ in range(1, self.n_iteration):
            # 決定木のインスタンス生成、学習、学習済みモデル格納
            self.model = tree.DecisionTreeRegressor(max_depth=self.max_depth, random_state=self.random_seed)
            self.model.fit(X, self.r)
            self.models.append(self.model)
            # それまでの予測結果とこのモデルの予測結果を足し合わせる
            self.f += self.learning_rate * self.model.predict(X)
            # 残差を更新
            self.r = self.r - self.f

            
    def predict(self, X_test):
        # 初期の予測値はテストデータと同じシェイプにする必要あり。
        result = np.full(len(X_test), self.y_mean)
        for model in self.models:
            result += self.learning_rate * model.predict(X_test)

        return result
