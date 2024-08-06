# TypeScript学習メモ



## 参考
* [Windowsにゼロから WSL2 + Docker CE + React環境を構築する全手順](https://qiita.com/yamazombie/items/4071dfb28e2465da7e3b)
* [サバイバルTypeScript](https://typescriptbook.jp/)



## オブジェクト
プロパティとメソッドを持つクラスみたいな感じ。

```
// クラスのプロパティとメソッドみたいな感じ
const obj = {
    a: 1,
    b: 2,
    sum(): number {
      return this.a + this.b;
    },
  };

console.log(obj.sum());
```