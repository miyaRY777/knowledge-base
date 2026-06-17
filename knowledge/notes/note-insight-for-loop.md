---
id: note-insight-for-loop
title: "for文は回数が決まった繰り返し処理の基本構文"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **同じ処理をくり返すための構文のこと**
- `for` 文は、初期化・条件判定・増減処理を1セットで書いて、条件が `false` になるまで処理をくり返すときに使います。回数が決まっているループを書くときによく使います。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for "for - JavaScript | MDN"))
- for (let i = 1; i <= 3; i++) {

## Tags
#javascript #loop

## Links

## Body
`for` 文の構造は `for (初期化; 条件; 増減式)` の3セクションで成り立ちます。
初期化はループ前に1回実行され、条件が `false` になるまで「条件チェック → 処理 → 増減式」が繰り返されます。
回数が決まっているループに向いており、回数が不定な場合は `while` の方が意図が明確なこともあります。

## Example

```js
for (let i = 1; i <= 3; i++) {
  console.log(i);
}
```

このコードでは、`i` を 1 から 3 まで増やしながら、同じ処理を3回くり返すために `for` 文を使っています。
