---
id: note-insight-hexadecimal-literal-0x
title: "0x表記はJavaScriptで16進数リテラルを書く方法"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- 数値の先頭に `0x` を付けると16進数として解釈されます。
- 内部的には通常の `Number` 型として扱われます。
- 16進数の1桁は4ビットに対応するため、3桁 = 12ビットです。

## Tags
#javascript #binary #programming

## Links
- [[note-insight-binary-literal-0b]]
- [[note-insight-bit-count-combinations]]
- [[note-insight-javascript-number-type]]

## Body
JavaScriptでは `0x` プレフィックスで16進数リテラルを書けます。色コード（`#FF0000`）やビットマスクなど、16進数が自然な文脈で使われます。16進数の1桁は0〜F（16種類）を表し、16種類 = 2⁴ = 4ビット必要なため、桁数×4でビット数を計算できます。

## Example
```js
const value = 0x11;
console.log(value); // 17（1×16 + 1 = 17）

// 3桁の16進数 = 12ビット
// 0xABC → A(1010) B(1011) C(1100) → 12ビット
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
