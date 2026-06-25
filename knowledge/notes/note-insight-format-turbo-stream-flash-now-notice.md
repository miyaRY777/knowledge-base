---
id: note-insight-format-turbo-stream-flash-now-notice
title: "format.turbo_streamブロックでflash.nowを使うとTurbo通信時にその場でメッセージを表示できる"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_fail_log: []
---

## Summary
- **Turbo通信時にその場でフラッシュメッセージを表示する処理**
- `flash.now` はリダイレクトせず同じリクエスト内で表示するために使います。
- Turbo Streamでは画面遷移しないため、`flash.now` が必要です。

## Tags
#insight

## Links

## Body
`flash` は次のリクエストまでメッセージを保持する仕組みで、リダイレクト後の画面に表示するために使います。
`flash.now` は現在のリクエスト内だけで有効で、リダイレクトしない Turbo Stream レスポンスではこちらを使わないとメッセージが表示されません。
`format.turbo_stream` ブロックで `flash.now` にセットし、ビューの flash 表示部分を `turbo_stream.replace` で更新するのが Hotwire でのフラッシュメッセージの典型的なパターンです。


## Example
```ruby
format.turbo_stream { flash.now[:notice] = "削除しました" }
```

このコードでは、画面遷移せずにメッセージを表示するために flash.now を使っています。

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
