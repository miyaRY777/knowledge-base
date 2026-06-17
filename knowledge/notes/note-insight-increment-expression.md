---
id: note-insight-increment-expression
title: "増減式はforループごとにカウンタ変数を増減させる部分"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **ループごとに値を増やしたり減らしたりする部分**
- `for (初期化; 条件; 増減式)` の3つ目に書く式です。1回ループが終わるたびに実行され、カウンタを `i++` や `i--` のように変化させます。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration "Loops and iteration - JavaScript | MDN"))
- for (let i = 0; i < 3; i++) {

## Tags
#javascript #loop

## Links

## Body
増減式は各反復の末尾に実行されるため、`i++` であれば処理後に `i` が1増えます。
`i++`（後置）と `++i`（前置）は for ループの増減式としては同じ結果ですが、他の式に組み込む場合は評価タイミングが異なります。
`i--` を使えば逆方向のループ `for (let i = arr.length - 1; i >= 0; i--)` も書けます。


## Example
```js
for (let i = 0; i < 3; i++) {
  console.log(i);
}
```

このコードでは、次のループへ進むたびに `i` を 1 ずつ増やすために増減式の `i++` を使っています。
