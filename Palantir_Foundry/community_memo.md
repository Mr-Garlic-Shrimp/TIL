# Palantir Communityメモ
投稿を読んでいて有益そうなものをピックアップする。


# Pipeline Builder
## Pipeline BuilderでPython Functionsを使う方法
[How do I create a code block in pipeline builder?](https://community.palantir.com/t/how-do-i-create-a-code-block-in-pipeline-builder/1114)

>1. Create a new code repository
>1. Select “Functions” in the the repo creation UI
>1. Select “Python Functions” in the next UI page
>1. Create a python file in python-functions/python/python_functions
>1. Write your function which takes as inputs individual values, not containers such as pyspark columns.   
>Make sure that you add type annotations to all your function parameters and the return type.
>1. Commit your code
>1. Tag your code and release it
>1. Wait for the release to complete
>1. Switch to your pipeline builder
>1. In the top left click the drop-down that says “reusables”
>1. Click “user-defined functions”
>1. Click “import UDF”
>1. Add the UDF you have created
>1. Create a transform path in pipeline builder
>1. You can now find your function amongst the available transformations.



# Typescript Functions
## クエリを実行する方法
[https://community.palantir.com/t/query-functions-in-typescript/1018](https://community.palantir.com/t/query-functions-in-typescript/1018)


# Workshop
## Workshopからビルドをトリガーする（進行中のトピック）
https://community.palantir.com/t/can-i-trigger-a-dataset-build-from-a-function-in-workshop/884