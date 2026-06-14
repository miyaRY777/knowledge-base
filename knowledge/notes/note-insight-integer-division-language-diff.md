---
id: note-insight-integer-division-language-diff
title: 整数同士の除算の結果は言語によって異なる
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
---

## Summary
- Java・C++ では整数型同士の除算は整数結果になります。
- JavaScript・Python 3 では同じ式でも小数を含む結果になります。

## Tags
#programming #java #javascript #data-type

## Links
- [[note-insight-integer-division]]
- [[note-insight-js-division]]
- [[note-insight-operand-type-result-diff]]

## Body
`2 / 5` の結果はJavaScriptでは `0.4`、Javaでは `0` になります。使用する言語とオペランドの型によって除算の挙動が異なるため、言語を跨いで学ぶときに混乱しやすい落とし穴です。

## Example
- Java: `2 / 5` → `0`（整数除算）
- JavaScript: `2 / 5` → `0.4`
- Python 3: `2 / 5` → `0.4`
- Python 3 整数除算: `2 // 5` → `0`
