---
id: note-insight-format-turbo-stream-flash-now-notice
title: format.turbo_stream { flash.now[:notice] = "部屋から退出しました" }の要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **Turbo通信時にその場でフラッシュメッセージを表示する処理**
- `flash.now` はリダイレクトせず同じリクエスト内で表示するために使います。
- Turbo Streamでは画面遷移しないため、`flash.now` が必要です。

## Tags
#insight

## Links

## Body
**Turbo通信時にその場でフラッシュメッセージを表示する処理**

**解説：**
`flash.now` はリダイレクトせず同じリクエスト内で表示するために使います。
Turbo Streamでは画面遷移しないため、`flash.now` が必要です。


## Example
```ruby
format.turbo_stream { flash.now[:notice] = "削除しました" }
```

このコードでは、画面遷移せずにメッセージを表示するために flash.now を使っています。
