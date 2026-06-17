---
id: note-insight-operator
title: 演算子はオペランドに特定の処理を行う記号
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
---

## Summary
- 演算子はオペランドに計算・比較・論理演算などを適用し、新しい値を返します。
- `+`（加算）、`-`（減算）、`===`（厳密等価）などが代表例です。

## Tags
#programming #operator #javascript

## Links
- [[note-insight-operand]]
- [[note-insight-arithmetic-operator]]
- [[note-insight-expression]]

## Body
演算子はオペランドに対して計算・比較・論理判定などを行い、新しい値を返す記号や予約語です。
種類ごとに優先順位があり、`2 + 3 * 4` は `*` が先に評価されて `14` になります。同じ記号でもオペランドの型によって動作が変わるものがあります（`+` の加算と文字列連結）。
比較演算子には `==`（緩い等価）と `===`（厳密等価）があり、型変換を伴う `==` の予期しない挙動を避けるため `===` を使うのが基本です。

## Example
```js
console.log(8 + 3);    // 11（加算）
console.log("a" + "b"); // "ab"（文字列連結）
```
