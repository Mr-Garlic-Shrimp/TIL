# Git操作メモ

## ある時点での作業ツリーの状態に戻したいとき
* 戻したいコミット時点の位置にHEAD（今自分が作業している場所を示すポインタ）を戻す。
* HEADの移動履歴は、git reflogで確認できる。  
  戻したい時点でのHEADの位置を確認したら、下記コマンドでHEADの位置を戻す。（下例ではHEAD@{1}）  
      ```
      git reset --hard HEAD@{1}
      ```  
  ※「git reset –hard」 は、参照、作業ツリー、インデクスを強制的に戻すコマンド　　
  
参考：  
https://codeclub965.com/?p=1815  
https://qiita.com/ymzkjpx/items/00ff664da60c37458aaa




## git pushをするときにパスワード聞かれるのがだるいとき
* git clone git@github.com:{user-name}/リポジトリ名　でSSH方式でクローンし直すと聞かなくなる。（githubにssh-keyを登録していることが前提）

## コミットのメッセージ編集
* 1つ前のコミットのメッセージを編集する  
    ```
    git commit --amend -m "xxx"
    ```

* 2つ前のコミットのメッセージを編集する  
    ```
    $ git rebase -i HEAD~2
    ```

参考：https://www.granfairs.com/blog/staff/git-commit-fix

## コミットの取り消し
* 直前のコミットなかったことにするには下記コマンドを実行する
  ```
  git reset --soft HEAD^
  ```
* 参考：https://qiita.com/shuntaro_tamura/items/06281261d893acf049ed
  
## 特定フォルダ、ファイルをgit管理化から外す
* git管理下のツリー内に.gitignoreを配置し、下記のように対象を記述する
```
# temp.txtを無視する
temp.txt
 
# tempディレクトリを無視する
temp/
 
# tempディレクトリを無視する
/temp/
```
特定のファイルの指定は、ファイル名を書くだけ。この場合は2つある「temp.txt」全てが無視される。

最初に「/」がついていれば、gitignoreが置いてあるディレクトリからの相対パスで指定されたディレクトリを無視。最初に「/」がついていなければ、全てのディレクトリを探して指定されたディレクトリを無視する。
* 参考：https://www.sejuku.net/blog/72389