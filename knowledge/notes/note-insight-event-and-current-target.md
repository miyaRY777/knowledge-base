---
id: note-insight-event-and-current-target
title: eventとevent.currentTargetの要点
created: 2026-04-12
source: [[2026-04-12_insight_stimulus-and-javascript-basics]]
---

## Summary
- `event` はクリックや入力などが起きたときの情報が入ったオブジェクトです。
- `event.currentTarget` は、そのイベントハンドラーが取り付けられている要素を表します。
- Stimulus の `toggle(event)` のようなメソッドでは、どの要素から呼ばれたかを判断するためによく使います。

## Tags
#frontend #stimulus #javascript #dom

## Links
- [[2026-04-08-member-detail-tabs]]
- [[2026-04-12-rooms-ui-improvement]]
- [[map-stimulus-basics]]

## Body
`event` は、ブラウザ上で何かの出来事が起きたときに渡される情報オブジェクトです。中には `type`、`target`、`currentTarget` などの情報が入っています。`event.currentTarget` は、イベントハンドラーが今まさに結びついている要素を指すので、「どのボタンが押されたか」「どのタグが操作されたか」を安定して取りたいときに便利です。Stimulus の `toggle(event)` の `toggle` という名前自体は特別なものではなく、イベントを受け取るために自分で付けたメソッド名です。

## Example
```js
toggle(event) {
  console.log(event.type)
  console.log(event.currentTarget.tagName)
}
```

このコードでは、発生したイベントの種類と、イベント処理を受け持っている要素を確認するために `event` と `event.currentTarget` を使っています。

## Action
- [ ] `event.target` との違いも1ノートで説明できるようにする
