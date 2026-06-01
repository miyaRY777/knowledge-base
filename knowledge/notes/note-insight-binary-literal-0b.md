---
id: note-insight-binary-literal-0b
title: "0b表記はJavaScriptで2進数リテラルを書く方法"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
---

## Summary
- 数値の先頭に `0b` を付けると2進数として解釈されます。
- 内部的には通常の `Number` 型として扱われます。
- `0x`（16進数）、`0o`（8進数）と同じリテラル記法の仲間です。

## Tags
#javascript #binary #programming

## Links
- [[note-insight-binary-data]]
- [[note-insight-hexadecimal-literal-0x]]
- [[note-insight-javascript-number-type]]

## Body
JavaScriptでは `0b` プレフィックスを使うことで、ソースコード上に2進数リテラルを直接書けます。ビット演算やフラグ管理のコードで可読性を上げるために使われます。実行時には通常の数値として扱われるため、計算や比較もそのまま行えます。

## Example
```js
const value = 0b1010;
console.log(value);        // 10
console.log(0b1010 === 10); // true
```
