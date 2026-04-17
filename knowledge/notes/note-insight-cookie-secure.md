---
id: note-insight-cookie-secure
title: Secure属性の要点
created: 2026-04-17
source: [[2026-04-17_insight_rails-cookies-headers-and-attributes.md]]
---

## Summary
- **`Secure` は、HTTPS 通信のときだけ Cookie を送る属性です。**
- 通信中に Cookie が盗み見られるリスクを減らすために使います。
- `HttpOnly` とは役割が違い、こちらは送信経路の安全性に関係します。

## Tags
#http #web #cookie #security

## Links
- [[note-insight-set-cookie-header]]
- [[note-insight-cookie-httponly]]
- [[note-insight-cookie]]

## Body
`Secure` 属性が付いた Cookie は、HTTPS で接続しているときだけブラウザから送信されます。
これにより、暗号化されていない HTTP 通信で Cookie が漏れる危険を減らせます。
Cookie の安全性を高めるときは、`Secure` と `HttpOnly` をそれぞれ別の役割として理解すると整理しやすいです。

## Example
```http
Set-Cookie: user_id=12345; Secure
```

このコードでは、安全な HTTPS 通信のときだけ `user_id` の Cookie を送るようにしています。

## Action
- [ ] SameSite 属性も合わせて整理する
