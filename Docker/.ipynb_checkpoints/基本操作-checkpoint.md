# 基本操作

## docker run
* pullしてきたイメージからコンテナを実行するコマンド
* オプション
  * -v [host_Dir]:[Container_Dir]
    * ホストのディレクトリをコンテナにマウントする
  * -p [host_port]:[container_port]
    * ホストのポートをコンテナのポートにフォワーディング  
    [host_IP]:[host_port] でコンテナのポートにアクセスできるようになる
    
## docer exec
* コンテナ内でコマンドを実行する
例）コンテナ内でbashを実行する。
```
docker exec -it <コンテナ名 or コンテナID> bash
```
これでコンテナ内で色々コマンド打てるようになる。