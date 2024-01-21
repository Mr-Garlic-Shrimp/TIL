"""
カンマ区切り数フィールドのあとに区切りなし、
スペースパディングされたテキストデータを編集するためのプログラム
あまり用途はない。
"""

import sys
import itertools

#file = 'sample_1.txt'
file = f"{sys.argv[1]}"
out_file = 'output.txt'

# 挿入に使用するコピー範囲を定義。インデックスなので-1
copy_start_idx = int(sys.argv[2]) - 1
copy_end_idx = int(sys.argv[3]) - 1
# 挿入したい行番号を定義。指定した行番号に元々あるデータの下へ挿入する。
where_to_insert = int(sys.argv[4])
# コピー範囲を何回挿入するか
n_iter = int(sys.argv[5])

# ファイル読み込み
with open(file, encoding='UTF-8') as f:
    lines = f.readlines()
    header = lines[0:1]
    footer = [lines[-1]]


# 挿入する対象のデータを定義
insert_lines = []

# 挿入したい回数分だけ複製
for _ in range(n_iter):
    insert_lines += lines[copy_start_idx : copy_end_idx + 1]
    

# 挿入(ヘッダーとフッターは除く)
lines = lines[1 : where_to_insert] + insert_lines + lines[where_to_insert:-1]


# 挿入することによりレコードに記録されている通番がずれるので編集する
for i, line in enumerate(lines):
    # 各行をカンマで区切る。
    splited_part = line.split(",")[-1]
    
    # 通番を編集
    lines[i] = line[:-16] + splited_part[:5] + str(i+1).rjust(3) + splited_part[7:]


# ヘッダーとフッターを追加
lines = header + lines + footer

# print(lines_out)
with open(out_file, encoding="UTF-8", mode="w") as f:
    f.writelines(lines)