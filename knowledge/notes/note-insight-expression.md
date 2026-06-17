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
式は評価すると必ず1つの値になるコードのまとまりです。変数・リテラル・関数呼び出し・演算子の組み合わせすべてが式に当たります。
文（statement）とは「処理を実行する命令」で値を持ちませんが、式は値を生むため別の式のオペランドにしたり変数に代入したりできます。
この区別はテンプレートリテラルや三項演算子など「値が必要な場所」に何を書けるかに直結します。

## Example
```js
8 + 3        // 式：評価すると 11
"hello"      // 式：評価すると "hello"
Math.max(1, 2) // 式：評価すると 2
```
