---
id: note-insight-api-endpoint
title: APIエンドポイントはAPIにリクエストを送る入口のURL
created: 2026-04-26
source: [[2026-04-26_insight_active-record-loading-and-joins.md]]
---

## Summary
- APIエンドポイントは API にアクセスする具体的な URL や URI。
- Rails 固有の機能名ではなく、Web API 全般の用語。
- どのエンドポイントを持つかはルーティング設計で決まる。

## Tags
#web #api #rails #routing

## Links
- [[note-insight-http-request]]

## Body
APIエンドポイントは、クライアントが API にリクエストを送るときの具体的な URL や入口を指す言葉です。たとえば `/users` や `/api/v1/posts/1` のようなパスがそれにあたります。これは Rails 固有の名前ではなく、Web API 全般で使われる一般的な用語です。Rails では、どの URL を API の入口として使うかは routes の設計で決まります。

## Example
```ruby
namespace :api do
  namespace :v1 do
    resources :posts, only: [:index]
  end
end
```

このコードでは、`/api/v1/posts` という API エンドポイントをルーティングで定義しています。

## Action
- [ ] REST の resource と endpoint の違いも整理する
