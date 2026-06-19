---
id: note-insight-primitive-type
title: プリミティブ型はプログラミング言語が基本として持つシンプルなデータ型
created: 2026-06-11
source: [[2026-06-11_insight_js-data-types-and-literals]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
---

## Summary
- プリミティブ型は、数値・文字列・真偽値など、言語が標準で持つ基本的なデータ型です。
- JavaScriptでは `string`・`number`・`bigint`・`boolean`・`undefined`・`symbol`・`null` がプリミティブ値です。
- 言語によってプリミティブ型の種類は異なります。

## Tags
#javascript #programming #data-type

## Links
- [[note-insight-data-type]]
- [[note-insight-javascript-number-type]]
- [[note-insight-string-type]]
- [[note-insight-boolean-type]]
- [[note-insight-null-js]]

## Body
プリミティブ型は、オブジェクトではなくシンプルな値を直接表すデータ型です。JavaScriptでは `typeof` 演算子でプリミティブ型を確認できます。オブジェクト型（配列・関数など）と対比して使われる概念です。

## Example
```js
console.log(typeof 10);      // number
console.log(typeof "Hello"); // string
console.log(typeof true);    // boolean
```
