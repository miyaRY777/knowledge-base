---
id: note-insight-integer-division
title: 整数除算は割り算の結果から小数部分を除き整数として扱う計算
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
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
Javaの整数除算はゼロ方向への丸めで切り捨てられます。`-7 / 2` は `-3.5` → `-3`（floor の `-4` とは異なる）。
JavaScriptに整数除算演算子はなく、`Math.trunc()` がゼロ方向丸め、`Math.floor()` が負の無限大方向丸めと使い分けが必要です。
整数除算を意図せず行ってしまうバグはJavaで頻出なので、除算前にオペランドの型を確認する習慣が重要です。

## Example
```java
int result = 12 / 5;
System.out.println(result); // 2
```
```js
// JavaScriptで整数除算に相当する処理
console.log(Math.trunc(12 / 5)); // 2
```
