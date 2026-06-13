---
id: note-insight-expression-evaluation
title: 評価は式を計算して結果の値を決めること
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
---

## Summary
- 評価とは、プログラムが式を処理して結果の値を求めることです。
- 評価された結果が変数への代入や次の処理で使われます。

## Tags
#programming #javascript

## Links
- [[note-insight-expression]]

## Body
コードを実行するとき、プログラムは式を左から右へ評価し、値に置き換えていきます。`8 + 3` なら演算子 `+` の処理が行われ、結果 `11` が得られます。この「値を決める過程」が評価です。

## Example
```js
const result = 8 + 3; // 8+3を評価した結果11をresultに代入
console.log(result);  // 11
```
