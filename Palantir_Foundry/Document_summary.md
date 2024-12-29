# Palantir Foundryのドキュメントサマリ
読んでて理解したことを要約していく

# Transforms Python API

## [configure](https://www.palantir.com/docs/foundry/transforms-python/transforms-python-api/#configure)
Executorのメモリを増やし、コア数を1にした際にallowed_run_duration（タイムアウトまでの実行時間）をオーバーしたことがあった。  
メモリ増設をやめて、コア数変更だけにしたところエラーは消えた。  
メモリ確保のために時間を使い過ぎてオーバーしたということだったのかもしれない。

