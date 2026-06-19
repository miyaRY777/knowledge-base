---
id: note-insight-operator-result-type
title: 演算結果のデータ型はオペランドの型と演算子と言語によって決まる
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
---

## Summary
- 演算結果には値だけでなくデータ型もあります。
- 結果の型はオペランドの型・演算子・言語の仕様によって決まります。

## Tags
#programming #javascript #data-type

## Links
- [[note-insight-operand-type]]
- [[note-insight-arithmetic-operator]]
- [[note-insight-typeof]]

## Body
JavaScriptでは `typeof` で演算結果の型を確認できます。`12 / 3` の結果は `number` 型の `4` です。整数同士の割り算でも `number` 型で返り、Javaのように自動で整数型になることはありません。

## Example
```js
const result = 12 / 3;
console.log(result);        // 4
console.log(typeof result); // number
```
