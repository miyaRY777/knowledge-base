---
id: note-insight-integer-division
title: 整数除算は割り算の結果から小数部分を除き整数として扱う計算
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
---

## Summary
- 整数除算は割り切れない場合に小数部分を除いた整数を返します。
- 丸め方向や演算子は言語によって異なります。

## Tags
#programming #java

## Links
- [[note-insight-integer-division-result]]
- [[note-insight-division-operator]]

## Body
Javaでは `int` 型同士の `/` 演算が整数除算になり、小数部分は切り捨てられます（ゼロ方向への丸め）。JavaScriptには整数除算演算子はなく、`Math.trunc()` などで代用します。

## Example
```java
int result = 12 / 5;
System.out.println(result); // 2
```
```js
// JavaScriptで整数除算に相当する処理
console.log(Math.trunc(12 / 5)); // 2
```
