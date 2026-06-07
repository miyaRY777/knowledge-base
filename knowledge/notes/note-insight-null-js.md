---
id: note-insight-null-js
title: JavaScriptのnullは値が存在しないことを表すプリミティブ値
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 1
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
- [[note-insight-zero-value]]
- [[note-insight-false-value]]

## Body
JavaScriptの `null` は「値が意図的に存在しない」状態を表すために使います。まだデータが取得されていない変数の初期値や、「何も選択していない」状態の表現に使われます。データベースの `NULL`（[[note-insight-null-value]]）と概念は近いですが、JavaScriptの `null` はプリミティブ値として定義されています。`typeof null` が `"object"` を返す挙動はJavaScriptの有名なバグとして知られています。

「未回答」の例として、500人にアンケートを送った場合、`Yes`・`No` と回答した人は `true`・`false` で表せますが、まだ回答していない300人分は `null` で表すのが適切です。`0` や `false`（[[note-insight-zero-value]]・[[note-insight-false-value]]）は値として存在しているのに対し、`null` はそもそも値が存在しない点が異なります。

## Example
```js
let selectedUser = null;
console.log(selectedUser === null); // true
console.log(typeof null); // "object" ← 歴史的なバグ

// 未回答の例
const answers = [true, false, null, null]; // null = まだ回答していない
```
