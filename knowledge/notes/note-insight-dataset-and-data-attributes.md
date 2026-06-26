---
id: note-insight-dataset-and-data-attributes
title: "datasetはdata属性をJavaScriptから読む仕組み"
created: 2026-04-12
source: [[2026-04-12_insight_stimulus-and-javascript-basics]]
quiz_fail_log: []
---

## Summary
- `dataset` は HTML の `data-*` 属性を JavaScript から読むための仕組みです。
- `data-name` はその具体例で、JavaScript では `dataset.name` として扱えます。
- `dataset` の値は文字列なので、真偽値を見たいときは `"true"` のように文字列として比較します。

## Tags
#frontend #javascript #dom #html

## Links
- [[note-insight-event-and-current-target]]
- [[map-stimulus-basics]]

## Body
`dataset` は、要素に付けた `data-*` 属性へアクセスするためのプロパティです。たとえば `data-name="rails"` は JavaScript では `dataset.name` として読めます。ここで返る値は常に文字列なので、`data-active="true"` を読むときは `clickedTag.dataset.active === "true"` のように比較します。 `data-name` 自体は特別な予約語ではなく、アプリ側で意味を決めるための目印です。

## Example
```js
const clickedTag = event.currentTarget
const wasActive = clickedTag.dataset.active === "true"
const name = clickedTag.dataset.name
```

このコードでは、クリックされた要素の `data-active` と `data-name` を読み取り、選択中かどうかと対応する名前を判定しています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
