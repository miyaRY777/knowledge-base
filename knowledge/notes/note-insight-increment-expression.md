---
id: note-insight-increment-expression
title: for文における増減式とは何か
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **ループごとに値を増やしたり減らしたりする部分**
- `for (初期化; 条件; 増減式)` の3つ目に書く式です。1回ループが終わるたびに実行され、カウンタを `i++` や `i--` のように変化させます。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration "Loops and iteration - JavaScript | MDN"))
- for (let i = 0; i < 3; i++) {

## Tags
#javascript #http

## Links
- [[関連ノート]]

## Body
**ループごとに値を増やしたり減らしたりする部分**

**解説：**
`for (初期化; 条件; 増減式)` の3つ目に書く式です。1回ループが終わるたびに実行され、カウンタを `i++` や `i--` のように変化させます。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration "Loops and iteration - JavaScript | MDN"))

```js
for (let i = 0; i < 3; i++) {
  console.log(i);
}
```

このコードでは、次のループへ進むたびに `i` を 1 ずつ増やすために増減式の `i++` を使っています。
