---
id: note-insight-rails-cookies
title: "Railsのcookiesはコントローラでブラウザのデータを読み書きする仕組み"
created: 2026-04-17
source: [[2026-04-17_insight_rails-cookies-headers-and-attributes.md]]
quiz_fail_log: []
---

## Summary
- **`cookies` は、Rails で Cookie を読み書きするための仕組みです。**
- `cookies[:user_id] = current_user.id` は、ユーザーIDをブラウザに保存するコードです。
- このコードを書くと、Rails はレスポンスに `Set-Cookie` ヘッダーを含め、次回以降のリクエストでブラウザがその Cookie を送ります。

## Tags
#rails #http #web #cookie

## Links
- [[note-insight-cookie]]
- [[note-insight-cookie-purpose]]
- [[note-insight-set-cookie-header]]
- [[note-insight-cookie-header]]

## Body
Rails の `cookies` は、コントローラなどから Cookie を扱うためのインターフェースです。
`cookies[:user_id] = current_user.id` と書くと、Rails はレスポンスに `Set-Cookie` ヘッダーを追加し、ブラウザはその値を保存します。
次回以降のリクエストでは、その Cookie が `Cookie` ヘッダーとしてサーバーへ送られるため、アプリ側は同じユーザーとして識別しやすくなります。
ただし Cookie はユーザーのブラウザに保存されるので、値の扱い方には注意が必要です。

## Example
```ruby
cookies[:user_id] = current_user.id
```

このコードでは、ログイン中ユーザーのIDを Cookie としてブラウザに保存し、次回以降の識別に使えるようにしています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
