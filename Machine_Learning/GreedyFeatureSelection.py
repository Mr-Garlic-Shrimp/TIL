import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score


class GreedyFeatureSelection():
    '''
    Greedy Feature Selectionを行うクラス。
    pipeline: 前処理、モデル定義を含むPipelineインスタンス
    cv: cross validationのインスタンス
    X: 全特徴量候補（Pandasのみ受付可能）
    y: 目的変数（Pandasのみ受付可能）
    '''

    def __init__(self, pipeline, cv) -> None:
        self.pipeline = pipeline
        self.cv = cv
        self.selected_features = []
        self.scores = {}
    
    def select(self, X, y):
        # 初期化
        best_score_temp = 0
        best_score_feature_temp = ''
        # X.columnsはindexオブジェクトを返すため、リストにしておかないとremove等は使えない。
        features_candidate = list(X.columns)
        max_select_iterations = len(X.columns)
        i = 0
        
        # 特徴量の選定ループ。whileループ1回につき、最大1つ特徴量が選定される。
        while i != max_select_iterations:

            # 「選定済み特徴量に特徴量を１つ加えて評価」を残り全特徴量分実施
            for feature in features_candidate:
                # 学習に使用する特徴量を定義
                use_features = [feature] + self.selected_features
                # 使用した特徴量によるCV評価結果の平均値をスコアとする。
                score = cross_val_score(estimator=self.pipeline, cv=self.cv, X=X[use_features], y=y).mean()
                # 暫定最高スコアと上記スコアの比較をし、高ければ暫定最高スコアを更新し、その特徴量を暫定チャンピオンとして格納
                if best_score_temp < score:
                    best_score_temp = score
                    best_score_feature_temp = feature

            # best_score_feature_temp（上記ループでの最終的なチャンピオン特徴量）が特徴量候補にある場合、
            # チャンピオン特徴量を特徴量候補から除き、選定した特徴量のリストに加える
            # 候補にない場合は、チャンピオン特徴量に更新がないということなので、選定を終了する。
            if best_score_feature_temp in features_candidate:
                features_candidate.remove(best_score_feature_temp)
                self.selected_features.append(best_score_feature_temp)
                self.scores[best_score_feature_temp] = best_score_temp
                i += 1
                print(f'特徴量{i}: {best_score_feature_temp}, スコア:{best_score_temp}')
            else:
                break

        print('Greedy Feature Selection done!')
