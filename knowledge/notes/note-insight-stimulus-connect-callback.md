---
id: note-insight-stimulus-connect-callback
title: Stimulusのconnect()はコントローラ接続時に自動実行される
created: 2026-04-12
source: [[2026-04-12_insight_stimulus-and-javascript-basics]]
---

## Summary
- `connect()` は Stimulus コントローラが画面に接続されたときに自動で呼ばれるメソッドです。
- 初期表示のセットアップや、最初に見せたい状態を整える処理を書く場所として使います。
- 例として、最初のタブを選択したり、初期状態で要素を隠したりするときに使えます。

## Tags
#frontend #stimulus #javascript

## Links
- [[2026-04-08-member-detail-tabs]]
- [[2026-04-12-rooms-ui-improvement]]
- [[map-stimulus-basics]]

## Body
`connect()` は Stimulus のライフサイクルコールバックの1つです。`data-controller` が付いた要素にコントローラが接続されると自動で実行されるので、画面の最初の見た目や値をそろえる処理を置くのに向いています。タブUIなら最初のパネルを開く、折りたたみUIなら最初は閉じた状態にする、といった用途で使います。

## Example
```js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  connect() {
    console.log("接続されました")
  }
}
```

このコードでは、コントローラが画面に接続されたタイミングを確認するために `connect()` を使っています。

## Action
- [ ] `disconnect()` との役割の違いも整理する
