import pandas as pd

# ダミー変数化するクラスの実装。コア部分はpd.get_dummiesを使用している。

# Transformerを自作するには下記の２クラスを継承する必要がある。 
from sklearn.base import BaseEstimator, TransformerMixin

class GetDummies(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.columns = None

    
    def fit(self, X, y=None):
        # 学習データをダミー変数化したときのカラム名を記録しておく
        # これは学習時に使ったカラムとテストデータに対する予測時に使うカラムを揃えるための前処理。
        self.columns = pd.get_dummies(X, drop_first=True).columns
        return self

    def transform(self, X):
        X_new = pd.get_dummies(X, drop_first=True)
        # .reindexによってX_newをcolumnsの順に並び替える。
        # もしもX_newにないカラムがある場合は、columnsに従って新しく列が追加されて全て0で埋められる。
        # これは学習データにあってテストデータにないカテゴリがある場合を想定した措置。
        # reindexの説明: https://note.nkmk.me/python-pandas-reindex/
        return X_new.reindex(columns=self.columns, fill_value=0)
