#!/bin/bash

# 引数をチェック
if [ $# -ne 1 ]; then
    echo "使用方法: $0 <連番>"
    exit 1
fi

# 指定ディレクトリ
directory="/home/iwago/work/git_work/TIL/Linux/shell_test/regex/input"

# 引数の連番を取得
number=$1

# 該当のファイルを検索
file=$(ls $directory | grep "AAAA.*_${number}.txt")

# ファイルが存在するかチェック
if [ -z "$file" ]; then
    echo "連番${number}を含むファイルが見つかりませんでした。"
    exit 1
fi

# ファイルの内容を表示
cat "${directory}/${file}"