---
id: note-insight-set-cookie-header
title: "Set-CookieはサーバーがブラウザにCookieを保存させるHTTPレスポンスヘッダー"
created: 2026-04-17
source: [[2026-04-17_insight_rails-cookies-headers-and-attributes.md]]
---

## Summary
- **`Set-Cookie` は、サーバーがブラウザに Cookie を保存させるための HTTP レスポンスヘッダーです。**
- ログイン後のユーザー識別やセッション管理でよく使われます。
- `expires` や `HttpOnly` などの属性も一緒に指定できます。

## Tags
#http #web #cookie

## Links
- [[note-insight-cookie-header]]
- [[note-insight-cookie]]
- [[note-insight-cookie-httponly]]
- [[note-insight-cookie-expires]]
- [[note-insight-cookie-secure]]
- [[note-insight-cookie-samesite]]
- [[note-insight-session-cookie]]
- [[note-insight-persistent-cookie]]
- [[note-insight-cookie-deletion]]

## Body
`Set-Cookie` は HTTP レスポンスで使われ、サーバーがブラウザに対して「この Cookie を保存してください」と伝えるためのヘッダーです。
ログイン成功時にユーザー識別用の値やセッションIDを保存したいときによく使われます。
また、保存期間や送信条件を制御するために `expires`、`HttpOnly`、`Secure` などの属性を一緒に付けられます。

## Example
```http
Set-Cookie: session_id=abc123; path=/; HttpOnly
```

このコードでは、サーバーが `session_id` をブラウザに保存し、JavaScript からは参照できないようにしています。

## Action
- [ ] path 属性と domain 属性の違いも整理する
