---
id: note-insight-explicit-type-conversion
title: 明示的な型変換はプログラマーが変換先の型を指定して変換すること
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 明示的な型変換は変換用の関数や構文を使って変換先の型をコード上で指定する方法です。
- 自動変換に頼らず意図を明確にしたいときに使います。

## Tags
#programming #javascript #java #data-type

## Links
- [[note-insight-type-conversion]]
- [[note-insight-implicit-type-conversion]]
- [[note-insight-cast]]

## Body
JavaScriptでは `Number()` / `String()` / `Boolean()` などの関数、Javaでは `(double)` のようなキャスト構文で明示的に型変換します。コードを読む人に変換の意図が伝わりやすくなります。

## Example
```js
const input = "10";
const number = Number(input);
console.log(number + 5); // 15
```
