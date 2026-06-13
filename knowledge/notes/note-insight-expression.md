---
id: note-insight-expression
title: 式は評価すると1つの値になるコードのまとまり
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
---

## Summary
- 式は値や演算子を組み合わせたもので、評価すると1つの値になります。
- `8 + 3` は評価されると `11` になります。

## Tags
#programming #javascript

## Links
- [[note-insight-operand]]
- [[note-insight-operator]]
- [[note-insight-expression-evaluation]]

## Body
式（expression）は評価によって値になります。変数・リテラル・関数呼び出し・演算子を組み合わせたものすべてが式です。文（statement）とは異なり、式は必ず値を持ちます。

## Example
```js
8 + 3        // 式：評価すると 11
"hello"      // 式：評価すると "hello"
Math.max(1, 2) // 式：評価すると 2
```
