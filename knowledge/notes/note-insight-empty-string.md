---
id: note-insight-empty-string
title: 空の文字列は中身がゼロ文字の文字列
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
---

## Summary
- 空の文字列 `""` は、文字列型として存在しているが中身の文字が0個の状態です。
- `null` とは異なり、値そのものは存在しています。
- `length` が `0` になり、falsyな値として扱われます（JavaScriptの場合）。

## Tags
#programming #data-type #javascript

## Links
- [[note-insight-string-type]]
- [[note-insight-null-js]]
- [[note-insight-empty-string-vs-null]]

## Body
`""` は文字列として存在しているが中身が空の状態を表します。フォーム入力で何も入力せずに送信した場合などに現れます。`null` は「値が存在しない」ことを表すのに対し、空文字は「値はあるが空」という違いがあります。バリデーションでは `null` と空文字を別々にチェックすることがあるため、この区別は実務で重要です。

## Example
```js
const text = "";
console.log(text.length); // 0
console.log(text === null); // false
```
