# vscodeの色々メモ

## WSL2上のJupyterLabコンテナに直接アクセスする方法
これをできるようにしておくと、pylanceなど便利な拡張機能が効くようになる。  
WSL2上でJupyterLabコンテナのworkフォルダーにマウントされているフォルダーのファイルを直接いじっていたが、  
これだとpylanceが効かないため※、直接アクセスする方が良い。  
※Pylanceがローカルシステム(WSL2)上で実行されるため、リモートのJupyter環境のパッケージやインタープリタ情報を適切に取得できないから。


1. vscodeからwsl2にアクセスできるようにしておく。
   ”Remote Development”という拡張機能をローカル(Windows)のvscodeに入れる。

2. vscodeからwsl2上のフォルダを開けるようになっていることを確認する。

3. wsl2上のフォルダを開いている状態で、コマンドパレットで  
   "Dev Containers: Reopen in Containers"みたいなコマンドを実行する。  
   この際、WSL2上でDockerはsudoなしで実行できるようにしておく必要があるので注意。  

この後はがちゃがちゃvscodeを再起動したりしてたら、左タブのRemote Explorerから  
Dev Containers → JupyterLabコンテナにアクセスできるようになっていたので、  
再現性のある手順はよくわからなかった。  
JupyterLabコンテナのworkフォルダーにマウントされているWSL2上のフォルダ作られるdevcontainer.jsonを編集する必要があるかも？  

https://qiita.com/yoshii0110/items/c480e98cfe981e36dd56