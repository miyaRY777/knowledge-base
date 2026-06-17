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
JavaScriptでは同じ演算子でもオペランドの型によって処理が変わります。`+` は両方数値なら加算ですが、片方でも文字列なら連結になります。
一方 `-`・`*`・`/` には文字列の特別扱いがなく、文字列のオペランドを数値に暗黙変換しようとします（`"5" - 2 = 3`、変換できない場合は `NaN`）。
この非対称な挙動のため、`+` を使う前にオペランドの型を明示的に確認するか、数値であることを保証しておくのが安全です。

## Example
```js
console.log(2 + 5);    // 7（数値の加算）
console.log("2" + 5);  // "25"（文字列連結）
console.log("5" - 2);  // 3（-は文字列を数値に変換して減算）
```
