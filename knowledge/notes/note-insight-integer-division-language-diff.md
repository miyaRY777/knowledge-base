---
id: note-insight-integer-division-language-diff
title: 整数同士の除算の結果は言語によって異なる
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
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
同じ `2 / 5` でも、Javaでは `int` 型同士の除算として `0`、JavaScriptでは `0.4` になります。
この違いは、Javaが整数型を持つのに対しJavaScriptは数値を全て `number` 型で統一しているためです。
複数言語を学ぶ際にこの挙動の違いが混乱のもとになりやすく、言語ごとに動作確認する習慣が重要です。

## Example
- Java: `2 / 5` → `0`（整数除算）
- JavaScript: `2 / 5` → `0.4`
- Python 3: `2 / 5` → `0.4`
- Python 3 整数除算: `2 // 5` → `0`

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
