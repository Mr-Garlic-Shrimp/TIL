// 参考：https://typescriptbook.jp/tutorials/make-a-simple-function-via-cli
function increment(num: number) {
    return num + 1;
}

// TypeScriptの場合、999を”999”で入れるとエラーになる
console.log(increment(999))
