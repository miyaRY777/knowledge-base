---
id: note-insight-js-division
title: JavaScriptの除算は整数同士でも小数を含む結果を返す
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- JavaScriptでは `2 / 5` が `0.4` になります（Javaの `0` とは異なる）。
- すべての数値が `number` 型のため整数除算は発生しません。

## Tags
#javascript #data-type

## Links
- [[note-insight-js-number-type-unified]]
- [[note-insight-integer-division-language-diff]]
- [[note-insight-division-operator]]

## Body
JavaScriptには整数型がないため、`/` 演算は常に浮動小数点数の結果を返します。`2 / 5` は `0.4`、`10 / 2` は `5`（整数に見えますが `number` 型）です。
`0 / 0` は `NaN`、正の数を `0` で割ると `Infinity`、負の数を `0` で割ると `-Infinity` になります。
整数除算が必要な場合は `Math.trunc()`（ゼロ方向）か `Math.floor()`（負の無限大方向）を目的に合わせて使います。

## Example
```js
console.log(2 / 5);   // 0.4
console.log(2.0 / 5); // 0.4
console.log(Math.trunc(2 / 5)); // 0（整数除算が必要なとき）
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
