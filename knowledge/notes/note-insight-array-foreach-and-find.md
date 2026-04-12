---
id: note-insight-array-foreach-and-find
title: forEachは全件処理、findは最初の1件検索に向く
created: 2026-04-12
source: [[2026-04-12_insight_stimulus-and-javascript-basics]]
---

## Summary
- `forEach` は配列の要素を1つずつ順番に処理するときに使います。
- `find` は条件に合う最初の1件だけを探して返すときに使います。
- 全件更新と1件検索で役割が違うので、目的に応じて使い分けると読みやすくなります。

## Tags
#javascript #array

## Links
- [[map-javascript-loop-basics]]

## Body
`forEach` は配列のすべての要素に対して同じ処理を順番に行いたいときに便利です。一方 `find` は、条件に合う最初の要素を1件だけ取りたいときに向いています。たとえばタブ一覧の見た目を全部更新するなら `forEach`、名前が一致する説明文を1つ探すなら `find` が自然です。

## Example
```js
const descriptions = [
  { name: "rails", text: "Webアプリを作るフレームワーク" },
  { name: "ruby", text: "プログラミング言語" }
]

descriptions.forEach((item) => {
  console.log(item.name)
})

const desc = descriptions.find((item) => item.name === "rails")
console.log(desc.text)
```

このコードでは、配列の全件を順番に処理する部分に `forEach` を使い、条件に合う最初の1件を探す部分に `find` を使っています。

## Action
- [ ] `map` や `filter` との使い分けも追記する
