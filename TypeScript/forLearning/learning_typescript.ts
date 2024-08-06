// クラスのプロパティとメソッドみたいな感じ
const obj = {
    a: 1,
    b: 2,
    sum(): number {
      return this.a + this.b;
    },
  };

console.log(obj.sum());