---
id: note-insight-for-loop
title: for文の要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **同じ処理をくり返すための構文のこと**
- `for` 文は、初期化・条件判定・増減処理を1セットで書いて、条件が `false` になるまで処理をくり返すときに使います。回数が決まっているループを書くときによく使います。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for "for - JavaScript | MDN"))
- for (let i = 1; i <= 3; i++) {

## Tags
#javascript #http

## Links
- [[関連ノート]]

## Body
**同じ処理をくり返すための構文のこと**

**解説：**
`for` 文は、初期化・条件判定・増減処理を1セットで書いて、条件が `false` になるまで処理をくり返すときに使います。回数が決まっているループを書くときによく使います。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for "for - JavaScript | MDN"))

具体例：

```js
for (let i = 1; i <= 3; i++) {
  console.log(i);
}
```

このコードでは、`i` を 1 から 3 まで増やしながら、同じ処理を3回くり返すために `for` 文を使っています。
