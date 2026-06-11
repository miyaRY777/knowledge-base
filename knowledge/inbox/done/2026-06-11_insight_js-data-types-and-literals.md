* [ ] `プリミティブ型`とは？

👉 **プログラミング言語が基本として持つシンプルなデータ型**

**解説：**
`プリミティブ型` は、数値・文字列・真偽値など、基本的な値を表すデータ型です。
JavaScriptでは、`string`、`number`、`bigint`、`boolean`、`undefined`、`symbol`、`null` がプリミティブ値として扱われます。言語によって、どの型をプリミティブ型とするかは異なります。([MDNウェブドキュメント][1])

```js
console.log(typeof 10);
console.log(typeof "Hello");
console.log(typeof true);
```

このコードでは、値の種類を確認するために `プリミティブ型` が関係しています。

---

* [ ] `データ型`とは？

👉 **値の種類を表す分類**

**解説：**
`データ型` は、その値が数値なのか、文字列なのか、真偽値なのかを区別するための分類です。
データ型によって、できる操作や扱い方が変わります。

```js
console.log(typeof 100);      // number
console.log(typeof "100");    // string
console.log(typeof false);    // boolean
```

このコードでは、値がどの種類なのかを調べるために `データ型` が関係しています。

---

* [ ] `リテラル`とは？

👉 **ソースコードに直接書かれた値**

**解説：**
`リテラル` は、プログラムの中にそのまま書かれた数値や文字列などの値です。
例えば `10` や `"Hello"`、`true` はリテラルです。JavaScriptでは、リテラルの書き方によって数値・文字列・真偽値などとして解釈されます。([MDNウェブドキュメント][2])

```js
console.log(10);
console.log("Hello");
console.log(true);
```

このコードでは、直接書いた値を使うために `リテラル` を使っています。

---

* [ ] `整数リテラル`とは？

👉 **整数を直接コードに書いた値**

**解説：**
`整数リテラル` は、小数点を含まない数値をそのまま書いたものです。
JavaScriptでは、整数も小数も基本的には `number` 型として扱われます。

```js
console.log(10);
console.log(2048);
console.log(typeof 10);
```

このコードでは、整数の値を直接表すために `整数リテラル` を使っています。

---

* [ ] `浮動小数点リテラル`とは？

👉 **小数を直接コードに書いた値**

**解説：**
`浮動小数点リテラル` は、`3.14` のように小数点を含む数値です。
JavaScriptの `number` 型は、整数も小数もまとめて扱います。内部的にはIEEE 754の倍精度浮動小数点数として扱われます。([MDNウェブドキュメント][3])

```js
console.log(3.14);
console.log(typeof 3.14);
```

このコードでは、小数を表すために `浮動小数点リテラル` を使っています。

---

* [ ] `2進数リテラル`とは？

👉 **2進数で数値を直接書く書き方**

**解説：**
`2進数リテラル` は、`0b` を先頭につけて2進数を表す書き方です。
JavaScriptでは、`0b1000` のように書くと、数値として扱われます。

```js
console.log(0b1000); // 8
```

このコードでは、2進数で数値を表すために `2進数リテラル` を使っています。

---

* [ ] `16進数リテラル`とは？

👉 **16進数で数値を直接書く書き方**

**解説：**
`16進数リテラル` は、`0x` を先頭につけて16進数を表す書き方です。
色コード、メモリアドレス、ビット操作などで16進数が使われることがあります。

```js
console.log(0x1F); // 31
```

このコードでは、16進数で数値を表すために `16進数リテラル` を使っています。

---

* [ ] `指数表現`とは？

👉 **10の何乗かを使って数値を短く書く方法**

**解説：**
`指数表現` は、`2e+3` のように、数値を「仮数 × 10のn乗」の形で書く方法です。
とても大きい数や小さい数を短く表すときに使われます。

```js
console.log(2e+3);    // 2000
console.log(1.23e-2); // 0.0123
```

このコードでは、大きい数や小さい数を短く表すために `指数表現` を使っています。

---

* [ ] `文字リテラル`とは？

👉 **1文字を表すリテラル**

**解説：**
`文字リテラル` は、`'a'` のように1文字を表す値です。
C++やJavaには `char` 型がありますが、JavaScriptには独立した `char` 型はなく、1文字でも文字列として扱われます。

```js
console.log("a");
console.log(typeof "a"); // string
```

このコードでは、1文字を文字列として扱うために `文字リテラル` が関係しています。

---

* [ ] `文字列リテラル`とは？

👉 **文字の並びを直接コードに書いた値**

**解説：**
`文字列リテラル` は、`"Hello"` や `"123"` のように、文字の並びを表す値です。
JavaScriptでは、シングルクォート、ダブルクォート、バッククォートで文字列を書けます。([MDNウェブドキュメント][4])

```js
console.log("Hello World");
console.log(typeof "123");
```

このコードでは、文字のまとまりを表すために `文字列リテラル` を使っています。

---

* [ ] `論理値リテラル`とは？

👉 **true または false を直接書いた値**

**解説：**
`論理値リテラル` は、真偽を表す `true` と `false` のことです。
条件分岐や判定処理でよく使います。`"true"` のようにクォートで囲むと、論理値ではなく文字列になります。

```js
console.log(true);
console.log(false);
console.log(typeof true);
console.log(typeof "true");
```

このコードでは、真偽を表すために `論理値リテラル` を使っています。

---

* [ ] `number型`とは？

👉 **JavaScriptで数値を表すデータ型**

**解説：**
`number型` は、JavaScriptで整数や小数を扱うための型です。
JavaScriptには、一般的な意味での `int` 型や `float` 型はなく、多くの数値は `number` 型として扱われます。非常に大きな整数などでは精度に注意が必要です。([MDNウェブドキュメント][3])

```js
console.log(typeof 10);   // number
console.log(typeof 3.14); // number
```

このコードでは、数値を扱うために `number型` を使っています。

---

* [ ] `string型`とは？

👉 **文字列を表すデータ型**

**解説：**
`string型` は、文字の並びを扱うためのデータ型です。
`"123"` のように数字が入っていても、クォートで囲まれていれば数値ではなく文字列として扱われます。([MDNウェブドキュメント][5])

```js
console.log(typeof "Hello");
console.log(typeof "123");
```

このコードでは、文字のまとまりを扱うために `string型` を使っています。

---

* [ ] `boolean型`とは？

👉 **true または false を表すデータ型**

**解説：**
`boolean型` は、正しいか正しくないかの2択を表すデータ型です。
条件分岐やフラグ管理でよく使います。

```js
const isLoggedIn = true;

console.log(typeof isLoggedIn);
```

このコードでは、ログインしているかどうかを表すために `boolean型` を使っています。

---

* [ ] `typeof`とは？

👉 **値のデータ型を調べるJavaScriptの演算子**

**解説：**
`typeof` は、指定した値の型を文字列で返すJavaScriptの演算子です。
学習中に「この値はどの型として扱われているか」を確認するときに便利です。([MDNウェブドキュメント][6])

```js
console.log(typeof 10);      // number
console.log(typeof "Hello"); // string
console.log(typeof true);    // boolean
```

このコードでは、値の型を調べるために `typeof` を使っています。

---

* [ ] `console.log()`とは？

👉 **JavaScriptで値をコンソールに出力する命令**

**解説：**
`console.log()` は、値や計算結果をコンソールに表示するために使います。
プログラムの動作確認や、変数の中身を確認するときによく使われます。

```js
console.log("Hello World");
console.log(10);
```

このコードでは、値を画面のコンソールに表示するために `console.log()` を使っています。

---

* [ ] `char型`とは？

👉 **1文字を表すためのデータ型**

**解説：**
`char型` は、C++やJavaなどで1文字を扱うためのデータ型です。
JavaScript、Python、PHPでは独立した `char` 型はなく、1文字も文字列として扱われます。環境や言語によって扱いが異なる点に注意が必要です。

**具体例：**

* Javaでは `'a'` を `char` として扱う
* JavaScriptでは `"a"` も `"Hello"` も `string` として扱う

この例では、1文字をどう扱うかを理解するために `char型` が関係しています。

[1]: https://developer.mozilla.org/en-US/docs/Glossary/Primitive?utm_source=chatgpt.com "Primitive - Glossary - MDN Web Docs"
[2]: https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Grammar_and_types?utm_source=chatgpt.com "文法とデータ型 - JavaScript - MDN Web Docs"
[3]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number?utm_source=chatgpt.com "Number - JavaScript - MDN Web Docs - Mozilla"
[4]: https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Lexical_grammar?utm_source=chatgpt.com "字句文法 - JavaScript - MDN Web Docs"
[5]: https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/typeof?utm_source=chatgpt.com "typeof - JavaScript - MDN Web Docs - Mozilla"
[6]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof?utm_source=chatgpt.com "typeof - JavaScript - MDN Web Docs - Mozilla"
