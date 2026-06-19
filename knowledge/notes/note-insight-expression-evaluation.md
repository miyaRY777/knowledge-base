---
id: note-insight-expression-evaluation
title: 評価は式を計算して結果の値を決めること
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 評価とは、プログラムが式を処理して結果の値を求めることです。
- 評価された結果が変数への代入や次の処理で使われます。

## Tags
#programming #javascript

## Links
- [[note-insight-expression]]

## Body
評価とは、式の各部分を計算して最終的な1つの値に解決する過程です。
演算子に優先順位があるため、`2 + 3 * 4` は左から順に処理されるのではなく `*` が先に評価されて `14` になります。
評価された値は変数への代入や別の式のオペランドとして使われるため、式の入れ子（ネスト）が可能です。

## Example
```js
const result = 8 + 3; // 8+3を評価した結果11をresultに代入
console.log(result);  // 11
```
