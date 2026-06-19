---
id: note-insight-string-literal
title: 文字列リテラルは文字の並びを直接コードに書いた値
created: 2026-06-11
source: [[2026-06-11_insight_js-data-types-and-literals]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 文字列リテラルは、`"Hello"` のように文字の並びをクォートで囲んで書いた値です。
- JavaScriptではシングルクォート・ダブルクォート・バッククォートの3種類で書けます。

## Tags
#javascript #programming

## Links
- [[note-insight-literal]]
- [[note-insight-string-type]]
- [[note-insight-character-literal]]

## Body
クォートで囲まれた値は文字列リテラルとして扱われます。`"123"` のように数字が入っていても文字列であり、算術演算には使えません。バッククォート（`` ` ``）を使うとテンプレートリテラルとして式の埋め込みが可能です。

## Example
```js
console.log("Hello World");
console.log(typeof "123"); // string
console.log(`1 + 1 = ${1 + 1}`); // テンプレートリテラル
```
