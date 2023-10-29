#!/bin/bash

# ファイル名を定義
output_file="large_csv_file.csv"

# ランダムな3桁の文字列を生成する関数
# generate_random_string() {
#     cat /dev/urandom | tr -dc 'a-zA-Z' | fold -w 3 | head -n 1
# }

# 1億行のCSVを生成
for i in $(seq 1 100000000)
do
    # HHMMSS形式の時刻を生成
    # time=$(date +%H%M%S)

    # # ランダムな整数を生成（例: 0〜999の範囲）
    # random_int=$((RANDOM % 1000))

    # ランダムな3桁の文字列を生成
    # random_string=$(generate_random_string)

    # CSVファイルに書き込む
    #echo "${time},${random_int},${random_string}" >> ~/work/git_work/TIL/Python/sample_data/from_HDD/$output_file
    echo "${i}" >> ~/work/git_work/TIL/Python/sample_data/from_HDD/$output_file

    # 進捗状況を表示
    if (( $i % 1000000 == 0 )); then
        echo "Generated $i rows..."
    fi
done

echo "CSV file generated: $output_file"
