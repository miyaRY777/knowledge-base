---
id: note-insight-operand-type
title: オペランドのデータ型によって演算子の動作や結果が変わる
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
---

## Summary
- 同じ演算子でもオペランドのデータ型によって処理内容と結果が変わります。
- JavaScriptの `+` は数値なら加算、文字列を含む場合は文字列連結になります。

## Tags
#programming #javascript #data-type

## Links
- [[note-insight-operator]]
- [[note-insight-addition-operator]]
- [[note-insight-operator-result-type]]
- [[note-insight-data-type]]

## Body
演算を行うときは値だけでなく型も確認する必要があります。`"2" + 5` は `7` でなく `"25"` になります。型を意識しないと予期しない結果やバグの原因になります。

## Example
```js
console.log(2 + 5);    // 7（数値の加算）
console.log("2" + 5);  // "25"（文字列連結）
console.log("5" - 2);  // 3（-は文字列を数値に変換して減算）
```
