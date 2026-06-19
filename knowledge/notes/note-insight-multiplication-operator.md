---
id: note-insight-multiplication-operator
title: 乗算演算子（*）は2つの値を掛ける演算子
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- `*` は2つのオペランドの積を返します。
- 算数の `×` に相当しますが、プログラミングでは `*` を使います。

## Tags
#programming #javascript #operator

## Links
- [[note-insight-arithmetic-operator]]

## Body
`*` は2つのオペランドの積を返す二項演算子です。数値同士の掛け算に使いますが、JavaScriptでは文字列や配列に `*` を使っても数値変換が試みられ意図しない結果になります。
`**` は累乗演算子（ES2016以降）で `2 ** 10 = 1024` のように書けます。乗算とは優先順位が異なり、`**` の方が高い優先順位を持ちます。

## Example
```js
console.log(12 * 5);  // 60
console.log(2 ** 3);  // 8（累乗：2の3乗）
```
