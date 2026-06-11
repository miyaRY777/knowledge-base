---
id: note-insight-literal
title: リテラルはソースコードに直接書かれた値
created: 2026-06-11
source: [[2026-06-11_insight_js-data-types-and-literals]]
---

## Summary
- リテラルは、変数を介さずコードに直接書かれた値のことです。
- `10`・`"Hello"`・`true` などがリテラルです。
- 書き方によって数値・文字列・真偽値などのデータ型として解釈されます。

## Tags
#javascript #programming

## Links
- [[note-insight-data-type]]
- [[note-insight-integer-literal]]
- [[note-insight-floating-point-literal]]
- [[note-insight-string-literal]]
- [[note-insight-boolean-literal]]

## Body
リテラルはデータ型ごとに書き方が決まっています。数値はそのまま、文字列はクォートで囲む、真偽値は `true`/`false` と書くなど、書き方がそのままデータ型を決定します。

## Example
```js
console.log(10);      // 整数リテラル
console.log("Hello"); // 文字列リテラル
console.log(true);    // 論理値リテラル
```
