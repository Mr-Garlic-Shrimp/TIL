#!/usr/bin/python3
import os, sys

# fork()関数を呼び出して親プロセスと子プロセスでプロセスの流れを分岐できる
# ここでの親プロセスはこのfork.py自体にあたる。
# fork.pyを実行するプロセスが親と子にforkされることでそれぞれ親と子で別の処理ができる
ret = os.fork()
if ret == 0: # 子プロセスの復帰時は0が返る
    print(f'子プロセス:{format(os.getpid())}, 親プロセスのpid:{os.getppid()}')
    exit()
elif ret > 0: # 親プロセスの復帰時は子プロセスのプロセスIDが返る
    print(f'親プロセス:{format(os.getpid())}, 子プロセスのpid:{ret}')
    exit()

sys.exit(1)