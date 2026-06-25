---
id: note-insight-javascript-number-type
title: "JavaScriptのNumber型は整数も小数も同じ型で扱う"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- JavaScriptでは整数も小数も `Number` 型で統一して扱います。
- C言語やJavaのような `int` / `float` の区別はありません。
- 内部的にはIEEE 754の64ビット浮動小数点数として表現されます。

## Tags
#javascript #data-type #programming

## Links
- [[note-insight-programming-data]]
- [[note-insight-signed-integer-type]]

## Body
JavaScriptの `Number` 型は、整数・小数の両方を1つの型で表現します。他の言語では整数と浮動小数点を別の型で管理しますが、JavaScriptでは区別がありません。内部的にはIEEE 754の64ビット浮動小数点数として扱われるため、非常に大きな整数や特定の小数計算では精度に注意が必要です。

## Example
```js
const age = 20;       // 整数もNumber型
const price = 19.99;  // 小数もNumber型
typeof age;   // "number"
typeof price; // "number"
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
