---
id: note-insight-null-js
title: JavaScriptのnullは値が存在しないことを表すプリミティブ値
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
---

## Summary
- `null` は「ここには値がない」と明示的に示すJavaScriptのプリミティブ値です。
- `0`・`false`・`""` は値として存在するが、`null` は値そのものが存在しない。
- 「未回答」のようにデータがまだ存在しない状態を表すときに使う。
- falsyな値なので `if (value)` のような条件判定で false として扱われます。

## Tags
#javascript #programming #data-type

## Links
- [[note-insight-empty-string]]
- [[note-insight-empty-string-vs-null]]
- [[note-insight-null-value]]
- [[note-insight-nullable]]
- [[note-insight-null-check]]
- [[note-insight-nullish-coalescing]]

## Body
JavaScriptの `null` は「値が意図的に存在しない」状態を表すために使います。まだデータが取得されていない変数の初期値や、「何も選択していない」状態の表現に使われます。データベースの `NULL`（[[note-insight-null-value]]）と概念は近いですが、JavaScriptの `null` はプリミティブ値として定義されています。`typeof null` が `"object"` を返す挙動はJavaScriptの有名なバグとして知られています。

## Example
```js
let selectedUser = null;
console.log(selectedUser === null); // true
console.log(typeof null); // "object" ← 歴史的なバグ
```
