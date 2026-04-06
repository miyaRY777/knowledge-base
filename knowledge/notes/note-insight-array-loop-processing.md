---
id: note-insight-array-loop-processing
title: 配列とループ処理の要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **配列の中身を順番に取り出して処理すること**
- 配列は複数の値を順番に持てるので、ループと相性がいいです。`for` 文では `length` を使って、先頭から末尾まで1つずつ処理できます。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Loops?utm_source=chatgpt.com "Looping code - Learn web development | MDN"))
- const fruits = ["apple", "banana", "orange"];

## Tags
#http

## Links
- [[関連ノート]]

## Body
**配列の中身を順番に取り出して処理すること**

**解説：**
配列は複数の値を順番に持てるので、ループと相性がいいです。`for` 文では `length` を使って、先頭から末尾まで1つずつ処理できます。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Loops?utm_source=chatgpt.com "Looping code - Learn web development | MDN"))

具体例：

```js
const fruits = ["apple", "banana", "orange"];

for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}
```

このコードでは、配列の要素を先頭から順番に取り出して表示するために、配列とループ処理を組み合わせています。

補足：
- length（配列）：**配列に入っている要素の数を取得するプロパティ**
