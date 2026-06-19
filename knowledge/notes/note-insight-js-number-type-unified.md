---
id: note-insight-js-number-type-unified
title: JavaScriptでは整数と小数をどちらもnumber型として扱う
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- JavaScriptでは `2` と `2.0` はどちらも `number` 型で同じ値として扱われます。
- JavaやC++のように整数型と浮動小数点型が分かれていません。

## Tags
#javascript #data-type

## Links
- [[note-insight-javascript-number-type]]
- [[note-insight-js-division]]
- [[note-insight-integer-division-language-diff]]

## Body
JavaScriptの `number` 型はIEEE 754倍精度浮動小数点数で、整数と小数を区別しません。そのため `typeof 2` も `typeof 2.0` もどちらも `"number"` を返します。

## Example
```js
console.log(typeof 2);   // number
console.log(typeof 2.0); // number
console.log(2 === 2.0);  // true
```
