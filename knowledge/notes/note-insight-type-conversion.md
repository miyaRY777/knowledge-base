---
id: note-insight-type-conversion
title: 型変換はデータを別のデータ型として扱えるように変換すること
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
---

## Summary
- 型変換は値のデータ型を別の型に変換する処理です。
- 暗黙的（自動）と明示的（コードで指定）の2種類があります。

## Tags
#programming #data-type #javascript #java

## Links
- [[note-insight-implicit-type-conversion]]
- [[note-insight-explicit-type-conversion]]
- [[note-insight-cast]]

## Body
型変換には、言語が自動で行う暗黙的変換と、`Number("5")` のようにコードで明示する明示的変換があります。
JavaScriptは暗黙変換が多く、`[] + {}` が `"[object Object]"` になるなど直感に反する挙動があるため、変換が必要な場面では `Number()`・`String()`・`Boolean()` を明示的に使うのが安全です。
入力値や外部データは文字列として受け取ることが多いため、計算前に型変換するのが基本パターンです。

## Example
```js
const number = Number("5");
console.log(number + 2); // 7
```
