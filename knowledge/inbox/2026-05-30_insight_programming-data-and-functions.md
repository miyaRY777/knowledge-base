- [ ] `データ`とは？

👉 **プログラムが扱う情報のこと**

**解説：**
`データ` は、プログラムが処理したり保存したりする情報のことです。
数値、文字列、真偽値、画像、ユーザー情報など、プログラムの中で扱うものはデータとして表現されます。
データは、関数や処理によって計算・変換・保存されます。

**具体例：**
- ゲームのスコア
- ユーザー名やメールアドレス
- 商品の価格
- ログインしているかどうかの状態
- Webフォームに入力された文字

この例では、プログラムが処理する情報として `データ` が関係しています。

参考：MDN Web Docs「Data structures」 https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures

---

- [ ] `関数`とは？

👉 **決まった処理をまとめて、必要なときに呼び出せるもの**

**解説：**
`関数` は、プログラムの中で行いたい処理をひとまとまりにしたものです。
同じ処理を何度も使いたいときや、処理に名前をつけて分かりやすくしたいときに使います。
関数には、データを受け取り、処理した結果を返すものもあります。

```js
function double(number) {
  return number * 2;
}

console.log(double(5));
```

このコードでは、数値を2倍にする処理をまとめるために `関数` を使っています。

参考：MDN Web Docs「Functions」 https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions
