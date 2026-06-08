* [ ] `void`とは？

👉 **値を返さないことを表す型・キーワード**

**解説：**
`void` は、関数やメソッドが「結果の値を返さない」ことを示すために使われます。
`null` が「値が存在しない状態」を表すのに対して、`void` は「返す値そのものがない」ことを表します。
Javaでは、メソッドが値を返さない場合に戻り値の型として `void` を指定します。([Oracle Java Tutorials][1])

```java
public static void sayHello() {
    System.out.println("Hello World");
}
```

このコードでは、画面に文字を表示するだけで値を返さないために `void` を使っています。

---

* [ ] `nullとvoidの違い`とは？

👉 **nullは「値がない」、voidは「返す値がない」こと**

**解説：**
`null` は、変数やデータに値が存在しない状態を表します。
一方で `void` は、関数やメソッドが結果として値を返さないことを表します。
つまり、`null` は「値の不在」、`void` は「戻り値の不在」と考えると整理しやすいです。

**具体例：**

* `null`：ユーザー情報がまだ存在しない
* `void`：画面に文字を表示するだけで、計算結果を返さない
* `null` は値として扱われることがあるが、`void` は返す値がないことを示す

この例では、値がない状態と、そもそも値を返さない処理を区別するために `nullとvoidの違い` が関係しています。

---

* [ ] `戻り値`とは？

👉 **関数やメソッドの処理結果として返される値**

**解説：**
`戻り値` は、関数やメソッドを実行したあと、呼び出し元に返す結果のことです。
計算結果や取得したデータを次の処理で使いたいときに戻り値を返します。
Javaでは、戻り値を返すメソッドは戻り値の型を指定し、返さない場合は `void` を指定します。([Oracle Java Tutorials][1])

```java
public static int add(int a, int b) {
    return a + b;
}
```

このコードでは、足し算の結果を返すために `戻り値` を使っています。

---

* [ ] `値を返さない関数`とは？

👉 **処理だけを行い、結果の値を返さない関数**

**解説：**
`値を返さない関数` は、画面表示・ログ出力・データ保存など、処理そのものが目的の関数です。
計算結果を呼び出し元で使う必要がない場合に使われます。
TypeScriptでは、関数が値を返さないことを `void` 型で表すことがあります。([TypeScript][2])

```ts
function showMessage(): void {
  console.log("Hello World");
}
```

このコードでは、メッセージを表示するだけで値を返さないために `値を返さない関数` を使っています。

---

* [ ] `副作用`とは？

👉 **戻り値以外に、外部の状態や画面に変化を起こす処理**

**解説：**
`副作用` は、関数の実行によって画面表示・ファイル保存・データベース更新などの変化が起きることです。
`void` の関数は、戻り値を返さずに副作用を目的として使われることがあります。
特定技術だけの特別な機能名ではなく、プログラミング一般で使われる考え方です。

```js
function logMessage() {
  console.log("保存しました");
}
```

このコードでは、コンソールに文字を表示するという変化を起こすために `副作用` が関係しています。

---

* [ ] `JavaScriptのvoid演算子`とは？

👉 **式を実行したあと、必ずundefinedを返す演算子**

**解説：**
`JavaScriptのvoid演算子` は、式を評価したあとに `undefined` を返す演算子です。
JavaやTypeScriptの戻り値の型としての `void` とは意味が異なるため、混同しないように注意します。
MDNでは、`void` 演算子は与えられた式を評価してから `undefined` を返すと説明されています。([MDN Web Docs][3])

```js
const result = void console.log("Hello");

console.log(result);
```

このコードでは、`console.log("Hello")` を実行しつつ、結果として `undefined` を返すために `JavaScriptのvoid演算子` を使っています。

---

* [ ] `エントリーポイント`とは？

👉 **プログラムの実行が始まる入口になる場所**

**解説：**
`エントリーポイント` は、プログラムが最初に実行される起点です。
言語や環境によって形は異なりますが、Javaでは `main` メソッドが代表的です。
Javaの `main` メソッドは値を返さないため、`void` が使われます。

```java
public static void main(String[] args) {
    System.out.println("Program start");
}
```

このコードでは、プログラムの開始地点として `エントリーポイント` が関係しています。

[1]: https://docs.oracle.com/javase/tutorial/java/javaOO/returnvalue.html "Returning a Value from a Method - Oracle Java Tutorials"
[2]: https://www.typescriptlang.org/docs/handbook/2/functions.html "TypeScript: More on Functions"
[3]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void "void operator - JavaScript | MDN Web Docs"
