#!/bin/bash

# awkで時刻差の計算したいときのスクリプト
awk 'BEGIN { FS = ", "; OFS = ", " }
{
    # 時間要素を抽出
    hour1 = substr($1, 1, 2); minute1 = substr($1, 3, 2); second1 = substr($1, 5, 2); milli1 = substr($1, 7, 3);
    hour2 = substr($3, 1, 2); minute2 = substr($3, 3, 2); second2 = substr($3, 5, 2); milli2 = substr($3, 7, 3);

    # 時刻1と時刻2をマイクロ秒単位に変換(マイクロ秒じゃなくてもOK)
    time_1 = (((hour1 * 60 + minute1) * 60 + second1) * 1000 + milli1) * 1000 + $2 / 1000;
    time_2 = (((hour2 * 60 + minute2) * 60 + second2) * 1000 + milli2) * 1000 + $4 / 1000;

    # 時刻1と時刻2の差の計算
    diff = time_2 - time_1;

    # 差が0以上なら1、そうでなければ0を出力
    if (diff >= 0){
        flag = 1
    } else {
        flag = 0
    };


    # 新しい列の追加と出力
    print $1, $2, $3, $4, diff, flag;
}' input/sample_time.csv
