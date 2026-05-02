---
id: note-insight-cookie-header
title: "Cookieヘッダーの要点"
created: 2026-04-17
source: [[2026-04-17_insight_rails-cookies-headers-and-attributes.md]]
---

## Summary
- **`Cookie` ヘッダーは、ブラウザが保存済み Cookie をサーバーへ送るための HTTP リクエストヘッダーです。**
- サーバーはこの値を見てユーザーやセッションを識別します。
- `Set-Cookie` が保存指示、`Cookie` ヘッダーが送信、という役割分担です。

## Tags
#http #web #cookie

## Links
- [[note-insight-set-cookie-header]]
- [[note-insight-cookie]]
- [[note-insight-cookie-purpose]]

## Body
`Cookie` ヘッダーは、ブラウザが以前に保存した Cookie を、次のリクエストでサーバーへ送り返すときに使われます。
サーバーはその値を読み取り、「誰からのアクセスか」や「どのセッションか」を判断します。
Cookie の仕組みを理解するときは、サーバーが保存を指示する `Set-Cookie` と、ブラウザが送り返す `Cookie` ヘッダーを分けて考えると分かりやすいです。

## Example
```http
GET /mypage HTTP/1.1
Cookie: session_id=abc123
```

このコードでは、ブラウザが保存していた `session_id` をサーバーに送っています。

## Action
- [ ] 複数Cookieが送られるときの書式も確認する
