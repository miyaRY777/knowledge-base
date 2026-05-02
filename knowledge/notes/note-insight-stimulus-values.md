---
id: note-insight-stimulus-values
title: "Stimulusのstatic valuesはdata属性を型付きで受け取る仕組み"
created: 2026-04-12
source: [[2026-04-12_insight_stimulus-and-javascript-basics]]
---

## Summary
- `static values = { bio: String }` のように書くと、HTML の `data-*-value` をコントローラで読めます。
- `this.bioValue` のような getter と setter が自動で使えるようになります。
- HTML から渡した設定値や初期値を、JavaScript 側で明示的に扱いたいときに便利です。

## Tags
#frontend #stimulus #javascript

## Links
- [[map-stimulus-basics]]

## Body
`static values` は、Stimulus で `data-controller-name-xxx-value` のような属性を型付きで受け取る仕組みです。`String` や `Number` などの型を宣言しておくと、コントローラ内では `this.xxxValue` として読み書きできます。初期表示で使うメッセージ、件数上限、状態フラグなどを HTML から渡したいときに向いています。

## Example
```js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static values = { bio: String }

  connect() {
    console.log(this.bioValue)
  }
}
```

このコードでは、HTML の data 属性に入れた自己紹介文を JavaScript で受け取るために `static values` を使っています。

## Action
- [ ] `hasBioValue` のような存在確認アクセサも整理する
