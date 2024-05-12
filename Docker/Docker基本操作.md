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
docker exec -it [コンテナ名 or コンテナID] bash
```
これでコンテナ内で色々コマンド打てるようになる。

## 稼働中のコンテナをイメージ化する

DockerHubからpullしてきたイメージにさらに手を加えたものをイメージ化して  
他で使いまわしたい場合がある。これはdocker commitで実現できる。

```bash:
docker commit <元となるコンテナ名> <作成するイメージ名>  

例）docker commit mycentos7 centos-php-apache
```

* 参考
  * https://pointsandlines.jp/server-infra/docker/docker-beginner-3  
  * https://uxmilk.jp/55512  


## イメージを.tarに保存する & .tarからイメージを読み込む

```bash:
# イメージを保存
docker save sample-image > sample-image.tar

# イメージを読み込み
docker load < sample-image.tar
```


## コンテナのプライベートIPを調べる
コンテナのプライベートIPを調べたいとき、  
docker execでコンテナに乗り込んでもipコマンドやhostnameコマンドが入っていない場合がある。  
そんなときはdocker inspectを用いればコンテナホストから調べることが出来る。  

```
docker inspect [コンテナID or コンテナ名]
```
→"Networks"の項目を参照

## 複数のコンテナを同じネットワークに所属させる方法-1
稼働中のコンテナ同士を同じネットワークに属するように設定変更するよりも、  
docker-compose等で設定を追記して立ち上げ直した方が楽。  
下記はmynetworkを作成し、両者のコンテナを同じネットワークに配置して起動させる例。

```yaml:docker-compose.yml
version: '3.7'
services:
  mysql:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: example
    networks:
      - mynetwork

  jupyterlab:
    image: jupyter/base-notebook
    networks:
      - mynetwork

networks:
  mynetwork:
    driver: bridge
```