# Git操作メモ

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