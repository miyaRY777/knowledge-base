---
id: note-insight-integer-division-result
title: 整数同士の割り算は言語によって小数部分の扱いが異なる
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- JavaScriptは整数同士を割っても小数を返しますが、Javaでは小数部分が切り捨てられます。
- オペランドのデータ型と言語の仕様を確認することが重要です。

## Tags
#programming #javascript #java

## Links
- [[note-insight-division-operator]]
- [[note-insight-integer-division]]
- [[note-insight-operand-type]]

## Body
同じ `12 / 5` でも、JavaScriptでは `2.4`、Javaの `int` 型同士では `2` になります。JavaでもオペランドをDoubleにすると小数が返ります。言語とデータ型によって結果が変わることを常に意識する必要があります。

## Example
```js
// JavaScript
console.log(12 / 5); // 2.4
```
```java
// Java
int a = 12, b = 5;
System.out.println(a / b);     // 2（切り捨て）
System.out.println(12.0 / 5.0); // 2.4
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
