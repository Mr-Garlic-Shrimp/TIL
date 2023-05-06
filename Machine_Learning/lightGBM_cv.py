import numpy as np
import lightgbm as lgb
from sklearn.metrics import log_loss, accuracy_score

def lightGBM_classifier_cv_func(X, y, cv, ct=None, params=None, num_boost_round=1000, stopping_rounds=10, verbose_eval=0, score_metric='log_loss'):

    '''
    LightGBMで分類タスクの場合のCV回すための関数。
    評価指標は一旦logloss固定。

    X(Pandas DataFrame): features.
    y(Pandas DataFrame): target
    cv: k-Fold CV instance
    ct: 欠損値対応や標準化する際のcolumns transformer
    
    '''

    scores = []
    verbose_eval = verbose_eval

    for train_index, test_index in cv.split(X):
        X_train, X_val = X.iloc[train_index], X.iloc[test_index]
        y_train, y_val = y.iloc[train_index], y.iloc[test_index]
        
        # 前処理：欠損値対応、ダミー変数変換の処理等。X_valはtransformのみで良いことに注意。
        # もしctに何も入れないと前処理はスキップされるので注意。
        # Target Encodingを使う場合に備えて、fitでは目的変数も入れる。
        if ct is not None:
            X_train = ct.fit_transform(X_train, y_train)
            X_val = ct.transform(X_val)

        # LightGBM 用のデータセットを作成
        lgb_train = lgb.Dataset(X_train, y_train)
        # valデータとして使うDatasetにはreferenceに学習データを指定する必要がある。
        lgb_eval = lgb.Dataset(X_val, y_val, reference=lgb_train)

        # # モデルの学習
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

        if score_metric=='log_loss':
            # 評価スコア（logloss）の計算
            score = log_loss(y_val, y_pred_proba)
            scores.append(score)
        elif score_metric=='accuracy':
            # 評価スコア（accuracy）の計算
            threshold = 0.5
            # 確率を0,1に変換。閾値は一旦0.5で固定。
            y_pred_label = np.where(y_pred_proba >= threshold, 1, 0)
            score = accuracy_score(y_val, y_pred_label)
            scores.append(score)

    # CVの評価結果を返す。
    return scores
