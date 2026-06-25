---
id: note-insight-js-void-operator
title: JSのvoid演算子は式を評価してundefinedを返す
created: 2026-06-08
source: [[2026-06-08_insight_void-null-return-values]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- JavaScript の `void` 演算子は、式を実行したあとに必ず `undefined` を返します。
- Java や TypeScript の戻り値の型としての `void` とは別の概念です。
- 同じ `void` という名前でも言語・文脈によって意味が異なるため混同に注意が必要です。
- 現代のJSでは自分から書く機会はほぼなく、古いコードや圧縮済みコードで見かける程度。

## Tags
#javascript #void #undefined #operator #programming

## Links
- [[note-insight-void]]
- [[note-insight-null-js]]

## Body
JavaScript の `void` は演算子であり、後ろに続く式を評価しつつ、その結果を捨てて `undefined` を返します。型としての `void`（Java・TypeScript）が「返す値がないことの宣言」であるのに対し、JS の `void` 演算子は「式を実行して結果を undefined に差し替える」という動作をします。同じ単語でも役割がまったく異なるため、文脈に注意して読み分けることが大切です。

### なぜ使うのか（歴史的背景）

**1. `undefined` の書き換え対策（ES5以前）**
ES5以前は `undefined` が書き換え可能な変数だったため、`void 0` で確実に `undefined` を得る手段として使われた。現代のJSでは `undefined` は書き換え不可のため不要。

**2. リンクの無効化（古い書き方）**
`<a href="javascript:void(0)">` でクリック時のページ遷移を防ぐために使われた。現代では `event.preventDefault()` で代替するのが一般的。

**3. ミニファイアが生成するコード**
バンドラーや圧縮ツールが出力するコードで `void` が使われることがある。

## Example
```js
const result = void console.log("Hello"); // "Hello" と表示される
console.log(result); // undefined

// 古いリンク無効化の書き方
// <a href="javascript:void(0)">クリック</a>

// void 0 で確実に undefined を得る（古い手法）
console.log(void 0); // undefined
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
