---
id: note-insight-nullish-coalescing
title: ??演算子はnull/undefinedのときだけ代替値を返す
created: 2026-06-05
source: [[2026-06-05_insight_null-and-related-values]]
quiz_streak: 1
---

## Summary
- `??`（nullish coalescing演算子）は左辺が null または undefined のときだけ右辺を返します。
- `||` と違い、`0` や `false`、`""` は左辺として有効な値として扱われます。
- null/undefined のデフォルト値を設定する場面でよく使われます。

## Tags
#javascript

## Links
- [[note-insight-null-js]]
- [[note-insight-null-check]]

## Body
`||` 演算子は左辺が falsy（`0`・`false`・`""`・`null`・`undefined`）のときに右辺を返しますが、`??` は null と undefined のときだけ右辺を返します。そのため `0` や `false` を正当な値として扱いたい場面では `??` の方が安全です。

## Example
```js
const nickname = null;
console.log(nickname ?? "ゲスト"); // "ゲスト"

const count = 0;
console.log(count ?? 10); // 0（||なら10になる）
console.log(count || 10); // 10
```
