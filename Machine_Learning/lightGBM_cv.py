import numpy as np
import lightgbm as lgb
from sklearn.metrics import log_loss

def lightGBM_classifier_cv_func(X, y, cv, pipeline=None, params=None, num_boost_round=1000, stopping_rounds=10, verbose_eval=0):

    '''
    LightGBMで分類タスクの場合のCV回すための関数。
    評価指標は一旦logloss固定。

    X(Pandas DataFrame): features.
    y(Pandas DataFrame): target
    cv: k-Fold CV instance
    pipeline: 欠損値対応や標準化する際のpipeline
    '''

    scores = []
    verbose_eval = verbose_eval

    for train_index, test_index in cv.split(X):
        X_train, X_val = X.iloc[train_index], X.iloc[test_index]
        y_train, y_val = y.iloc[train_index], y.iloc[test_index]
        
        # LightGBM 用のデータセットを作成
        lgb_train = lgb.Dataset(X_train, y_train)
        # valデータとして使うDatasetにはreferenceに学習データを指定する必要がある。
        lgb_eval = lgb.Dataset(X_val, y_val, reference=lgb_train)


        if pipeline is not None:
            callbacks = [lgb.early_stopping(stopping_rounds=stopping_rounds), lgb.log_evaluation()]
            model = pipeline.fit(X_train, y_train, model__eval_set=lgb_eval, model__callbacks=callbacks)


        # モデルの学習
        model = lgb.train(params,
                        lgb_train,
                        num_boost_round=num_boost_round,
                        valid_sets=lgb_eval,
                        callbacks=[
                                lgb.early_stopping(stopping_rounds=stopping_rounds, verbose=True), # early_stopping用コールバック関数
                                lgb.log_evaluation(verbose_eval)] # コマンドライン出力用コールバック関数)
                        )

        # テストデータで予測
        # predictで各クラスの確率が返ってくる。predict_probaはないことに注意。
        # 予測結果のクラスにしたい場合は.argmax(axis=1)で行ごとに見て最大値をとるカラムのインデックスを返せばよい。
        y_pred_proba = model.predict(X_val, num_iteration=model.best_iteration)#.argmax(axis=1)

        # 評価スコア（logloss）の計算
        score = log_loss(y_val, y_pred_proba)
        scores.append(score)

    # CVの評価結果を返す。
    return scores
