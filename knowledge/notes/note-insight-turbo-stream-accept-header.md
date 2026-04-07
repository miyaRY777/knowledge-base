---
id: note-insight-turbo-stream-accept-header
title: headers: { "Accept" => "text/vnd.turbo-stream.html" }の要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **Turbo Stream形式でレスポンスを受け取るためのHTTPヘッダー**
- リクエスト時に「Turbo Stream形式で返してほしい」とサーバーに伝えるために使います。
- これにより、`format.turbo_stream` が選ばれて部分更新が行われます。

## Tags
#http

## Links
- [[関連ノート]]

## Body
**Turbo Stream形式でレスポンスを受け取るためのHTTPヘッダー**

**解説：**
リクエスト時に「Turbo Stream形式で返してほしい」とサーバーに伝えるために使います。
これにより、`format.turbo_stream` が選ばれて部分更新が行われます。


## Example
```ruby
post room_path(room), headers: { "Accept" => "text/vnd.turbo-stream.html" }
```

このコードでは、Turbo Streamとしてレスポンスを受け取り、画面の一部更新を行うために headers を使っています。
