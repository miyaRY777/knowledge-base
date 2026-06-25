---
id: note-insight-operand
title: オペランドは演算子によって処理される値
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- オペランドは、演算子の処理対象となる値です。
- `8 + 3` では `8` と `3` がオペランドです。

## Tags
#programming #operator

## Links
- [[note-insight-operator]]
- [[note-insight-expression]]

## Body
オペランドは演算子が処理する対象の値です。オペランドの数によって演算子の種類が分かれます。
1つのオペランドをとる演算子を単項演算子（`-x`・`!flag`・`typeof x`）、2つをとるものを二項演算子（`a + b`）、3つをとるものを三項演算子（`条件 ? 真値 : 偽値`）と呼びます。
同じ記号でも単項か二項かで意味が変わるものがあります（`-` は「引き算」にも「符号反転」にも使われる）。

## Example
```js
console.log(8 + 3); // 8と3がオペランド、+が演算子
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
