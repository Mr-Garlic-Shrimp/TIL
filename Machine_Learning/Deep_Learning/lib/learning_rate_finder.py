from torch import optim

# 学習率の目安を探すための関数
def learning_rate_finder(model, train_loader, loss_func, lr_increase_ratio=1.1):

    # 学習率の初期値は小さく定義。最大値を超えたら探索をやめる
    lr = 1e-8
    max_lr = 10
    # 学習率と損失記録用リスト
    lr_history = []
    loss_history = []

    # Optimizer定義。学習率は後で変更できる。
    optimizer = optim.SGD(model.parameters(), lr=lr)

    for idx_batches, data in enumerate(train_loader):
        X_train, y_train = data

        # 順伝播
        y_pred = model(X_train)
        loss = loss_func(y_pred, y_train)

        # 逆伝搬
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        # グラフ描画用情報記録。学習率は見やすさのためにlog scaleにしておく。
        loss_history.append(loss.item())
        lr_history.append(lr)
        print(f"ミニバッチidx: {idx_batches}, 学習率: {lr}, 損失: {loss.item()}")
        # print(f'Optimizer: {optimizer.param_groups[0]["lr"]}')

        # optimizerの学習率更新。lrの更新は表示用
        lr *= lr_increase_ratio
        optimizer.param_groups[0]["lr"] = lr

        if lr > max_lr:
            break

    return lr_history, loss_history   
