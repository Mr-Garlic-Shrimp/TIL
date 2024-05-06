import torch
import torchvision
from torch import nn
from torch.nn import functional as F
from torch import optim
# from torchvision import transforms
# from torch.utils.data import DataLoader, Dataset
# from torch.optim.lr_scheduler import StepLR, CosineAnnealingLR

class MLP_2Layers(nn.Module):
    def __init__(self, num_in, num_hidden, num_out):
        # 親クラスのinitを呼び出す。
        super().__init__()
        # nn.Flattenにより[b, c, h, w] -> [b, c x h x w]（ミニバッチサイズ, 画像の特徴量数の積）に変換
        self.flatten = nn.Flatten()
        self.linear_1 = nn.Linear(num_in, num_hidden)
        self.linear_2 = nn.Linear(num_hidden, num_out)

    # nn.Moduleにもforwardメソッドがあり、ここでオーバーライドしている。
    def forward(self, x):
        # 最初の全結合層の計算に渡す際にnn.Flattenを実行しておく必要あり。
        z = self.linear_2( F.relu( self.linear_1(self.flatten(x))) )
        return z
    

# MLPの学習を実行するための関数
def learn(model, train_loader, val_loader, optimizer, 
          loss_func, epoch=10, early_stopping=None, save_path=None, lr_scheduler=None):
    '''
    model: 任意のMLPモデル
    train_loader: 学習データのDataLoader
    val_loader: 検証データのDataLoader
    optimizer: optimizer
    loss_func: 損失関数
    epoch: epoch数。デフォルトは10。
    early_stopping: early_stopping判定の際のepoch数。デフォルトはearly_stoppingしない。
    save_path: モデルのパラメタやoptimizerのパラメタを保存する先を指定。デフォルトは保存しない。
    lr_scheduler: Learning Rate Schedulerを指定
    '''

    # 学習・検証結果格納用辞書
    train_results = {}
    best_params_and_Loss = {}

    # early_stoppingの判定用のカウンターとそのepoch時点での最小の損失を記録する用変数。初期値は無限大を指定。
    early_stopping_counter = 0 
    min_Loss_val = float('inf') # infinity

    for i, _ in enumerate(range(epoch)):

        # 各バッチでの学習データと検証データに対するloss、accuracyを累積する用の変数
        cum_loss = 0
        cum_loss_val = 0
        cum_accuracy_val = 0

        for num_batches, train_data in enumerate(train_loader):
            # 学習データ定義
            X_train_batch, y_train_batch = train_data

            # 順伝播の計算
            y_pred = model(X_train_batch)
            loss = loss_func(y_pred , y_train_batch)
            cum_loss += loss.item()
            
            # 逆伝播の計算、パラメタ更新
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()


        # 検証データに対する損失を計算。こちらもバッチ単位で評価するように変更。（検証データ数が多いときはこの方が効率的）
        with torch.no_grad():
            for num_batches_val, val_data in enumerate(val_loader):
                X_val, y_val = val_data
                y_pred_val = model(X_val)
                loss_val = loss_func(y_pred_val, y_val)
                accuracy_val = ( (torch.argmax(y_pred_val, dim=1) == y_val).sum() / len(y_val) )
                # バッチごとの損失、accuracyを累積
                cum_loss_val += loss_val.item()
                cum_accuracy_val += accuracy_val.item()


        # 損失、accuracyを記録。
        # DataLoaderからのイテレーションの数＋１が実際のミニバッチ数になるので、累積した損失等をこれで割ってepochごとに計算
        train_results[f"epoch_{i}"] = {
            "Loss_train": cum_loss / (num_batches + 1),
            "Loss_val": cum_loss_val / (num_batches_val + 1),
            "Accuracy": cum_accuracy_val / (num_batches_val + 1),
        }

        print(f'epoch_{i}: {train_results[f"epoch_{i}"]}, Learning Rate: {optimizer.param_groups[0]["lr"]}')


        if early_stopping:
            # i番目のepochの損失がその時点の最小の損失よりも大きい場合、early_stoppingのカウンターを1増やす。
            # そうでない場合、最小の損失値を更新し、カウンターを0に戻す。(暫定チャンピオン方式)
            if train_results[f"epoch_{i}"]["Loss_val"] >= min_Loss_val:
                early_stopping_counter += 1
            else:
                min_Loss_val = train_results[f"epoch_{i}"]["Loss_val"]
                epoch_min_Loss_val = i
                early_stopping_counter = 0

                # save_pathがNoneではなければ保存する
                # 改善されていれば以下の辞書を更新する
                if save_path:
                    best_params_and_Loss = {
                        "epoch": epoch_min_Loss_val,
                        "Model_param": model.state_dict(),
                        "Optimizer_param": optimizer.state_dict(),
                        "Loss_val": min_Loss_val
                    }
            
            if early_stopping_counter >= early_stopping:
                print("early stoppingにより学習を終了します。")
                print(f"検証データに対する損失が最小となるepoch: {epoch_min_Loss_val}")
                break
        
        # 学習率の更新
        if lr_scheduler:
            lr_scheduler.step()


    # 　パラメタ保存ありの場合、ファイルに保存
    if early_stopping and save_path: torch.save(best_params_and_Loss, save_path)

    return train_results, best_params_and_Loss