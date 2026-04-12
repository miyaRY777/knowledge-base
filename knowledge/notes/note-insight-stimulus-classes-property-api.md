---
id: note-insight-stimulus-classes-property-api
title: StimulusのClassesプロパティAPIはHTMLからclass名を受け取れる
created: 2026-04-09
source: [[2026-04-09_insight-entry-point-css-entry-build-output-stimulus-classes]]
---

## Summary
- Stimulus の ClassesプロパティAPI は、HTML 側で渡した class 名をコントローラから扱いやすくする仕組みです。
- `static classes = [...]` で宣言すると、JavaScript 側で決まった名前の class を参照できます。
- HTML 側に必要な class 指定がないと、使い方によってはエラーになるため注意が必要です。

## Tags
#frontend #stimulus #javascript #css #要復習 #要復習 #要復習

## Links
- [[2026-04-09-tabs-controller-css-refactor]]
- [[note-insight-entry-point]]

## Body
Stimulus の ClassesプロパティAPI は、class 名を JavaScript に直書きせず、HTML 側から受け取って使うための仕組みです。これにより、JS は class 名の具体値を知らなくてもよくなり、見た目の変更を HTML 側に寄せやすくなります。表示状態やエラー状態など、意味のある class を安全に扱いたいときに便利です。

## Example
```js
// controllers/toggle_controller.js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static classes = ["hidden"]

  hide() {
    this.element.classList.add(this.hiddenClass)
  }
}
```

```erb
<div data-controller="toggle"
     data-toggle-hidden-class="hidden">
  メニュー
</div>
```

このコードでは、HTML 側で渡した `hidden` という class 名を JavaScript 側で安全に使うために StimulusのClassesプロパティAPI を使っています。

## Action
- [ ] `hasHiddenClass` など関連アクセサも整理する

<!-- review_log: 2026-04-09,2026-04-12,2026-04-12 -->
