# Palantir Foundryのドキュメントサマリ
大事なポイントをまとめておく。

# Datasets
* データセットを開いたときに見ているものは最新のデータセットビューと呼ばれるもの
    * データセットはファイルの集合である。1データセット=1ファイルではない。
    * データセットビューはそれまでのトランザクションによって追加・変更されたファイル群から成る。
* データセットにロジック等で編集が加えられたとき、裏では編集のためのトランザクションが走る。
* A transaction is analogous to a commit in Git: an atomic change to the contents of a dataset.
    * gitのコミットと同様ならば、やはりここでいうトランザクションはロールバック可能な単位と考えるのがよさそう
* A transaction has a simple lifecycle:
    * After a transaction is started, it is in an OPEN state. In this state, files can be opened and written in the dataset's backing file system.
    * A transaction can be committed, which puts it into a COMMITTED state and any written files are now in the latest dataset view.
 
# ファイルフォーマット
* JSONやXMLなどの非構造化データはスキーマなしデータセットで読み込んで、後でパースすることをドキュメントないで推奨されている。  
In practice, for non-tabular formats such as JSON or XML, we recommend storing files in an unstructured (schema-less) dataset and applying a schema in a downstream data transformation as described in the schema inference documentation.


# Media sets
* 1メディアセットに含まれるデータは同じ形式でなくてはならない。PDFとJPEGファイルは混在NG。
A media set is a collection of media files with a common schema, for example, files of the same format
* Enabling content analysis by extracting text from PDFs with Pipeline Builder
* Performing geospatial analysis with raster tiling (TIFF, NITF) in the Map application
* Processing medical imaging files (DICOM format) with Pipeline Builder

# Branch
* ブランチは開発メンバー個々人ごとに切って作業することが推奨されている（当然）
* Similar to branches in Git, dataset branches are simply a pointer to the most recent transaction on that branch.As a result, a branch can be interpreted as a linear sequence of transactions ordered by commit time. 
* Dataset branch guarantees
    * One open transaction per branch.
    * On every branch, transactions are ordered by start and commit time.
    * Every non-root branch has exactly one parent branch

# Builds
* ビルドの前準備内容
    1. ビルド対象ブランチからJobSpecを収集し、ビルドの内容を作成する
    2. ジョブの入力データセット、出力データセットを特定する（フォールバックブランチを見ながら）
* JobSpec:   
A JobSpec defines how to construct a job by detailing input dataset dependencies and the logic that should be executed as part of the job.
    * JobSpecはコードリポジトリなどでコードをコミットしたときにパブリッシュされる
    * Dataset icon color provides information about JobSpecs and branching. If a dataset's icon is gray, this indicates that no JobSpec exists on the master branch. If the dataset icon is blue, a JobSpec is defined on the master branch.
* [ビルドの流れ例](https://www.palantir.com/docs/foundry/data-integration/branching/#example-building-on-branches)→JobSpec、トランザクションとの関係とかわかりやすい

# Transforms Python API

## [configure](https://www.palantir.com/docs/foundry/transforms-python/transforms-python-api/#configure)
Executorのメモリを増やし、コア数を1にした際にallowed_run_duration（タイムアウトまでの実行時間）をオーバーしたことがあった。  
メモリ増設をやめて、コア数変更だけにしたところエラーは消えた。  
メモリ確保のために時間を使い過ぎてオーバーしたということだったのかもしれない。
