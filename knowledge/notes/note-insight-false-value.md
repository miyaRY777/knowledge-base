---
id: note-insight-false-value
title: falseは「いいえ」と答えた状態でありnullとは別物
created: 2026-06-07
source: [[2026-06-07_insight_null-and-related-values]]
---

## Summary
- `false` はブーリアン型の値で「偽・いいえ」という意味の値が存在している状態です。
- `null` の「値がない・未回答」とは異なります。
- アンケートで「いいえ」と答えた（`false`）と、まだ回答していない（`null`）は別の状態です。

## Tags
#programming #data-type #javascript

## Links
- [[note-insight-null-js]]
- [[note-insight-boolean-type]]
- [[note-insight-zero-value]]

## Body
`false` は「条件が成立しない」「いいえと回答した」という意味を持つ値です。値として存在しているという点で `null` とは根本的に違います。アンケートを例にすると、「回答した結果がいいえ（`false`）」と「まだ回答していない（`null`）」は異なる状態であり、混同するとバグの原因になります。

## Example
```js
const answeredSurvey = false; // 「いいえ」と回答した
const notAnswered = null;     // まだ回答していない

console.log(answeredSurvey === null);  // false（falseは値として存在する）
console.log(answeredSurvey === false); // true
console.log(notAnswered === null);     // true
```
