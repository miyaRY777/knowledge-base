---
id: note-insight-stimulus-targets
title: "Stimulusのstatic targetsは操作したい要素に名前を付ける仕組み"
created: 2026-04-12
source: [[2026-04-12_insight_stimulus-and-javascript-basics]]
quiz_fail_log: []
---

## Summary
- `static targets = ["panel"]` のように書くと、Stimulus がその名前の要素を扱えるようにします。
- これにより `panelTarget`、`panelTargets`、`hasPanelTarget` のような便利なプロパティが自動で使えるようになります。
- 要素が必ずあるとは限らない場合は、`hasPanelTarget` で存在確認してから触ると安全です。

## Tags
#frontend #stimulus #javascript

## Links
- [[2026-04-08-member-detail-tabs]]
- [[2026-04-09-tabs-controller-css-refactor]]
- [[map-stimulus-basics]]

## Body
`static targets` は、Stimulus で操作したい HTML 要素に名前を付けるための仕組みです。たとえば `panel` を target にすると、最初の1件を表す `this.panelTarget`、複数件を配列で扱う `this.panelTargets`、存在確認用の `this.hasPanelTarget` が自動で生えます。`this.panelTarget` は要素そのものなので、存在しないのに触るとエラーになります。 optional な要素を扱うときは、先に `this.hasPanelTarget` で確認するのが安全です。

## Example
```js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = ["panel"]

  connect() {
    if (this.hasPanelTarget) {
      this.panelTarget.textContent = "こんにちは"
    }
  }
}
```

このコードでは、`panel` という名前で要素を扱えるようにしつつ、存在するときだけ安全に書き換えています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
