---
id: note-insight-empty-string-vs-null
title: 空文字は文字列が存在する状態、nullは値が存在しない状態
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- `""` は文字列型として存在しているが中身が空の状態、`null` は値そのものがない状態です。
- フォーム入力では空送信で `""` が来ることが多く、DBでは未入力を `null` で保存することがあります。
- バリデーションや条件分岐でこの違いを意識しないと意図しない挙動になります。

## Tags
#programming #javascript #data-type

## Links
- [[note-insight-empty-string]]
- [[note-insight-null-js]]
- [[note-insight-null-value]]

## Body
`""` と `null` はどちらも「何もない」ように見えますが、型と意味が異なります。`""` は文字列として存在していて `length` が `0` の状態です。`null` は「値が割り当てられていない」という状態を示します。Webアプリでは、フォームが空で送信されると `""` が届き、DBのカラムに値を入れなかった場合は `NULL` になるなど、場所によって使われ方が違います。`value === null` と `value === ""` を別々にチェックする必要があるケースを覚えておくと実務で役立ちます。

## Example
```js
const fromForm = "";      // 空送信
const notSelected = null; // 未選択

console.log(fromForm === null);  // false
console.log(fromForm === "");    // true
```
