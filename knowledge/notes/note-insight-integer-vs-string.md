---
id: note-insight-integer-vs-string
title: 整数型と文字列型は計算と文字連結で挙動が異なる
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 1
---

## Summary
- 整数型は数値として演算（加減乗除）に使い、文字列型は文字の連結に使います。
- 見た目が同じ `1` と `"1"` でも型が違うと `+` の挙動が変わります。
- JavaScriptでは `1 + 2 = 3` ですが `"1" + "2" = "12"` になります。

## Tags
#programming #data-type #javascript

## Links
- [[note-insight-string-type]]
- [[note-insight-integer-data-type]]

## Body
整数型と文字列型は見た目が似ていても演算の結果が全く異なります。`1 + 2` は `3` ですが、`"1" + "2"` は文字列の連結になり `"12"` になります。フォームから受け取った数値はデフォルトで文字列として扱われることが多いため、計算に使う前に `parseInt()` や `Number()` で型変換が必要です。型を意識しないとバグの原因になる典型的なケースです。

## Example
```js
console.log(1 + 2);       // 3
console.log("1" + "2");   // "12"
console.log(Number("3") + 4); // 7
```
