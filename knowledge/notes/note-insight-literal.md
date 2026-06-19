---
id: note-insight-literal
title: リテラルはソースコードに直接書かれた値
created: 2026-06-11
source: [[2026-06-11_insight_js-data-types-and-literals]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
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
リテラルとはソースコードに直接書かれた固定値で、実行時に評価されてその型の値になります。変数と違い、リテラル自体は変更できません。
書き方がデータ型を決定します。クォートなしの数字は数値、クォートで囲むと文字列、`true`/`false` は論理値になります。
リテラルと変数の区別を意識することで「どの値が変化しうるか」をコードから読み取りやすくなります。

## Example
```js
console.log(10);      // 整数リテラル
console.log("Hello"); // 文字列リテラル
console.log(true);    // 論理値リテラル
```
