---
id: note-insight-zero-value
title: 0は数値としてのゼロを表す値であり「値がない」ではない
created: 2026-06-07
source: [[2026-06-07_insight_null-and-related-values]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- `0` は数値として存在する値です。「何もない」状態を表す `null` とは異なります。
- 所持金が0円・在庫が0個のように、数値として意味を持ちます。
- falsy な値なので `if (0)` は false になりますが、`null` とは意味が違います。

## Tags
#programming #data-type #javascript

## Links
- [[note-insight-null-js]]
- [[note-insight-empty-string-vs-null]]
- [[note-insight-boolean-type]]

## Body
`0` は「ゼロという値が存在している」状態です。`null` が「値そのものがない」のとは本質的に異なります。たとえばテストの点数が `0` 点の場合、点数という値は存在していて、その結果がゼロです。`null` であれば「まだ採点されていない」ことを意味します。どちらも `if` 文では falsy として扱われるため、意図せず同一視してしまうミスが起きやすいです。

## Example
```js
const score = 0;
const notYetScored = null;

console.log(score === null);       // false（0は値として存在する）
console.log(score === 0);          // true
console.log(notYetScored === null); // true
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
