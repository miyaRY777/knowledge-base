---
id: note-insight-addition-operator
title: 加算演算子（+）は数値を足す演算子だが文字列では連結になる
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
---

## Summary
- `+` は数値同士なら加算、文字列を含む場合は文字列連結になります。
- JavaScriptでは型によって動作が変わるため注意が必要です。

## Tags
#programming #javascript #operator

## Links
- [[note-insight-arithmetic-operator]]
- [[note-insight-operand-type]]

## Body
`+` はオペランドのデータ型によって動作が変わる演算子です。両方が数値なら加算、どちらかが文字列なら文字列連結として機能します。意図しない連結を防ぐには `Number()` で型変換するか、オペランドの型を確認することが重要です。

## Example
```js
console.log(12 + 5);    // 17（加算）
console.log("2" + 5);   // "25"（文字列連結）
console.log(2 + 5);     // 7（加算）
```
