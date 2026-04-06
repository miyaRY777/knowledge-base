---
id: note-insight-initialization
title: 初期化の要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **ループを始める前に最初の値を用意すること**
- `for` 文の最初の部分に書く式です。多くの場合、`let i = 0` のようにループ用の変数を作って、開始位置を決めます。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for "for - JavaScript | MDN"))
- for (let i = 0; i < 5; i++) {

## Tags
#javascript #http

## Links
- [[関連ノート]]

## Body
**ループを始める前に最初の値を用意すること**

**解説：**
`for` 文の最初の部分に書く式です。多くの場合、`let i = 0` のようにループ用の変数を作って、開始位置を決めます。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for "for - JavaScript | MDN"))

具体例：

```js
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

このコードでは、ループを 0 から始めるために `let i = 0` で初期化しています。
