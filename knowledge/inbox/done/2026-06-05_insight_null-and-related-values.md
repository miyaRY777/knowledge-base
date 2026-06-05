* [ ] `null`とは？

👉 **値が存在しないことを表す特別な値**

**解説：**
`null` は、「値がない」「まだデータが入っていない」ことを表すために使います。
`0`、`false`、`""` は値として存在しますが、`null` は値が存在しない状態を表します。
JavaScriptでは、`null` は意図的にオブジェクト値が存在しないことを表すプリミティブ値です。([MDNウェブドキュメント][1])

```js
let selectedUser = null;

console.log(selectedUser);
```

このコードでは、まだ選択されたユーザーが存在しないことを表すために `null` を使っています。

---

* [ ] `0`とは？

👉 **数値としての「ゼロ」を表す値**

**解説：**
`0` は「何もない」ではなく、数値として存在する値です。
たとえば、所持金が `0円`、子供の人数が `0人` のように、数値として意味があります。
`null` とは違い、「値はあるが、その数が0」という状態です。

**具体例：**

* 子供の人数が `0`
* 商品の在庫数が `0`
* テストの点数が `0`

この例では、数値として存在する値を表すために `0` が関係しています。

---

* [ ] `false`とは？

👉 **条件が正しくないことを表すブーリアン型の値**

**解説：**
`false` は、ブーリアン型で「偽」を表す値です。
`false` は値として存在しており、「未回答」や「値がない」という意味ではありません。
たとえば、「アンケートに答えますか？」に対して `false` は「いいえ」と回答した状態です。

```js
const answeredSurvey = false;

console.log(answeredSurvey);
```

このコードでは、アンケートに答えない状態を表すために `false` を使っています。

---

* [ ] `空文字`とは？

👉 **文字数が0の文字列**

**解説：**
`空文字` は、`""` のように中身が空の文字列です。
文字が入っていないだけで、文字列型の値としては存在しています。
`null` のように「値そのものがない」状態とは区別します。

```js
const nickname = "";

console.log(nickname);
```

このコードでは、ニックネーム欄が空の文字列として存在していることを表すために `空文字` を使っています。

---

* [ ] `未回答`とは？

👉 **まだ回答データが存在しない状態**

**解説：**
`未回答` は、質問に対する回答がまだ得られていない状態です。
「いいえ」と答えた `false` とは違い、そもそも回答データが存在しません。
このような状態を表すときに `null` が使われることがあります。

**具体例：**

* 500人にアンケートを送る
* 50人が `Yes` と回答する
* 150人が `No` と回答する
* 残り300人はまだ回答していないので `null` として扱う

この例では、回答がまだ存在しない状態を表すために `未回答` が関係しています。

---

* [ ] `データベースのNULL`とは？

👉 **データベースの列に値が入っていないことを表す状態**

**解説：**
`データベースのNULL` は、ある項目の値が不明・未入力・該当なしであることを表します。
`0` や空文字 `""` とは意味が違います。
SQLでは、`NULL` は通常の値のように `=` で比較せず、`IS NULL` を使って判定します。PostgreSQLの公式ドキュメントでも、`NULL` との比較には `IS NULL` を使うことが説明されています。([PostgreSQL][2])

```sql
SELECT *
FROM users
WHERE nickname IS NULL;
```

このコードでは、`nickname` に値が入っていないユーザーを探すために `データベースのNULL` を使っています。

---

* [ ] `nullable`とは？

👉 **値がnullになる可能性があること**

**解説：**
`nullable` は、変数やデータ項目が `null` を持つ可能性があることを表す考え方です。
特定技術だけの特別な機能名ではなく、プログラミングやデータベース設計で広く使われる考え方です。
TypeScriptでは、`strictNullChecks` を有効にすると、`null` と `undefined` がそれぞれ別の型として扱われます。([typescriptlang.org][3])

```ts
let nickname: string | null = null;

nickname = "Taro";
```

このコードでは、文字列または `null` を入れられる値として `nullable` の考え方を使っています。

---

* [ ] `nullチェック`とは？

👉 **値がnullかどうかを確認する処理**

**解説：**
`nullチェック` は、値が存在するかどうかを確認してから処理するために使います。
`null` のままプロパティやメソッドを使おうとすると、エラーになる場合があります。
そのため、バックエンドやフロントエンドではよく使われます。

```js
const user = null;

if (user === null) {
  console.log("ユーザーが存在しません");
}
```

このコードでは、ユーザー情報が存在しないか確認するために `nullチェック` を使っています。

---

* [ ] `nullish coalescing演算子`とは？

👉 **nullまたはundefinedのときだけ代わりの値を使う演算子**

**解説：**
`nullish coalescing演算子` は、JavaScriptの `??` のことです。
左側の値が `null` または `undefined` の場合だけ、右側の値を返します。
MDNでも、`??` は左辺が `null` または `undefined` の場合に右辺を返す演算子と説明されています。([MDNウェブドキュメント][4])

```js
const nickname = null;

console.log(nickname ?? "ゲスト");
```

このコードでは、`nickname` が `null` のときに代わりの表示名を使うために `nullish coalescing演算子` を使っています。

[1]: https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/null?utm_source=chatgpt.com "null - JavaScript - MDN Web Docs - Mozilla"
[2]: https://www.postgresql.org/docs/8.1/functions-comparison.html?utm_source=chatgpt.com "Documentation: 8.1: Comparison Operators"
[3]: https://www.typescriptlang.org/tsconfig/strictNullChecks.html?utm_source=chatgpt.com "TSConfig Option: strictNullChecks"
[4]: https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing?utm_source=chatgpt.com "ヌル値合体演算子 (??) - JavaScript - MDN Web Docs"
