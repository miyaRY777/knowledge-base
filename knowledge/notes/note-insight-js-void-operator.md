---
id: note-insight-js-void-operator
title: JSのvoid演算子は式を評価してundefinedを返す
created: 2026-06-08
source: [[2026-06-08_insight_void-null-return-values]]
---

## Summary
- JavaScript の `void` 演算子は、式を実行したあとに必ず `undefined` を返します。
- Java や TypeScript の戻り値の型としての `void` とは別の概念です。
- 同じ `void` という名前でも言語・文脈によって意味が異なるため混同に注意が必要です。

## Tags
#javascript #void #undefined #operator #programming

## Links
- [[note-insight-void]]
- [[note-insight-null-js]]

## Body
JavaScript の `void` は演算子であり、後ろに続く式を評価しつつ、その結果を捨てて `undefined` を返します。型としての `void`（Java・TypeScript）が「返す値がないことの宣言」であるのに対し、JS の `void` 演算子は「式を実行して結果を undefined に差し替える」という動作をします。同じ単語でも役割がまったく異なるため、文脈に注意して読み分けることが大切です。

## Example
```js
const result = void console.log("Hello"); // "Hello" と表示される
console.log(result); // undefined
```
