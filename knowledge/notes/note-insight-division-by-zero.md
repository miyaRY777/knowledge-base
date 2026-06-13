---
id: note-insight-division-by-zero
title: 0除算の動作は言語によって異なりJSではInfinityかNaNになる
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
---

## Summary
- JavaScriptで正の数を `0` で割ると `Infinity`、`0 / 0` は `NaN` になります。
- Javaの整数型で `0` 除算を行うと例外（`ArithmeticException`）が発生します。

## Tags
#programming #javascript #java

## Links
- [[note-insight-infinity]]
- [[note-insight-nan]]
- [[note-insight-division-operator]]

## Body
0除算の結果は言語とデータ型によって大きく異なります。JavaScriptはエラーにならず特別な値を返しますが、Javaの整数型では実行時例外が発生します。意図しない `0` 除算を防ぐために、除数が `0` でないか事前に確認することが重要です。

## Example
```js
console.log(1 / 0);   // Infinity
console.log(-1 / 0);  // -Infinity
console.log(0 / 0);   // NaN
```
```java
int a = 1 / 0; // ArithmeticException: / by zero
```
