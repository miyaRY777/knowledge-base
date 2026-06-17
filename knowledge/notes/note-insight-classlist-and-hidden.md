---
id: note-insight-classlist-and-hidden
title: "classListはHTML要素のclassを追加・削除・切り替えするJavaScriptのAPI"
created: 2026-04-12
source: [[2026-04-12_insight_stimulus-and-javascript-basics]]
---

## Summary
- `classList` は HTML 要素の class を追加、削除、切り替えするための仕組みです。
- Tailwind の `hidden` は `display: none` を表すことが多く、要素を画面から消したいときによく使います。
- `classList.toggle("hidden")` を使うと、表示と非表示を簡単に切り替えられます。

## Tags
#frontend #javascript #css #tailwind

## Links
- [[note-insight-stimulus-classes-property-api]]
- [[2026-04-12-rooms-ui-improvement]]
- [[map-stimulus-basics]]

## Body
`classList` は DOM 要素の `class` 属性を扱うための API です。`add`、`remove`、`contains`、`toggle` などが使えるため、UI の状態に応じて見た目を変えるときに向いています。Tailwind CSS でよく出てくる `hidden` は `display: none` に相当し、要素をレイアウトごと非表示にできます。そのため、`classList.toggle("hidden")` は開閉UIやドロップダウンで頻出します。

## Example
```js
const isHidden = this.contentTarget.classList.toggle("hidden")
this.openTextTarget.classList.toggle("hidden", !isHidden)
this.closeTextTarget.classList.toggle("hidden", isHidden)
```

このコードでは、1つの要素の表示状態を切り替え、その結果に合わせて開く文言と閉じる文言の見た目も更新しています。

## Action
- [ ] `invisible` との違いも比較できるようにする
