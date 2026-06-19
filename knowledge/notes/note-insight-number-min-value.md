---
id: note-insight-number-min-value
title: Number.MIN_VALUEはJavaScriptで0より大きい最小の正の値
created: 2026-06-12
source: [[2026-06-12_insight_js-number-types-and-floating-point]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
---

## Summary
- `Number.MIN_VALUE` は最小の負の数ではなく、`0` に最も近い正の数です。
- 「最小値」という名前から負の数と誤解されやすい点に注意が必要です。

## Tags
#javascript #number #data-type

## Links
- [[note-insight-javascript-number-type]]
- [[note-insight-number-max-value]]

## Body
`Number.MIN_VALUE` は約 `5 × 10⁻³²⁴` という非常に小さな正の数です。最小の負の数は `-Number.MAX_VALUE` で表されます。名前の紛らわしさから混同しやすいため注意が必要です。

## Example
```js
console.log(Number.MIN_VALUE);  // 5e-324（0より大きい最小の正の数）
console.log(-Number.MAX_VALUE); // 最小の負の数
```
