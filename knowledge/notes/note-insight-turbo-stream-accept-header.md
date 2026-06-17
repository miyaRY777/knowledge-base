---
id: note-insight-turbo-stream-accept-header
title: "Acceptヘッダーにtext/vnd.turbo-stream.htmlを指定してTurbo Streamレスポンスを受け取る"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **Turbo Stream形式でレスポンスを受け取るためのHTTPヘッダー**
- リクエスト時に「Turbo Stream形式で返してほしい」とサーバーに伝えるために使います。
- これにより、`format.turbo_stream` が選ばれて部分更新が行われます。

## Tags
#http

## Links

## Body
HTTP の `Accept` ヘッダーはクライアントが「どの形式でレスポンスを受け取れるか」をサーバーに伝えるためのものです。
Rails の `respond_to` ブロックはこのヘッダーを見てフォーマットを選択するため、`Accept: text/vnd.turbo-stream.html` を付けると `format.turbo_stream` ブロックが実行されます。
テストで `headers:` を指定するのは、ブラウザが Turbo Drive 経由でリクエストする際に自動で付与するヘッダーを手動で再現するためです。


## Example
```ruby
post room_path(room), headers: { "Accept" => "text/vnd.turbo-stream.html" }
```

このコードでは、Turbo Streamとしてレスポンスを受け取り、画面の一部更新を行うために headers を使っています。
