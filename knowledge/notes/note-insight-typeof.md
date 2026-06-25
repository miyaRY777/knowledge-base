---
id: note-insight-typeof
title: typeof演算子は値のデータ型を文字列で返す
created: 2026-06-11
source: [[2026-06-11_insight_js-data-types-and-literals]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- `typeof` は、指定した値のデータ型を文字列で返すJavaScriptの演算子です。
- `typeof null` が `"object"` を返す点は有名な落とし穴です。
- 型の確認や学習時のデバッグによく使います。

## Tags
#javascript #programming

## Links
- [[note-insight-data-type]]
- [[note-insight-primitive-type]]
- [[note-insight-null-check]]

## Body
`typeof` を使うと、値が数値・文字列・真偽値・関数・オブジェクトのどれかを確認できます。ただし `typeof null` は `"object"` を返すため、null チェックには `=== null` を使う必要があります。

## Example
```js
console.log(typeof 10);        // number
console.log(typeof "Hello");   // string
console.log(typeof true);      // boolean
console.log(typeof undefined); // undefined
console.log(typeof null);      // object（注意：バグではなく仕様）
console.log(typeof {});        // object
console.log(typeof function(){}); // function
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
