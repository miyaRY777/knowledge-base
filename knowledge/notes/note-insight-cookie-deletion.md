---
id: note-insight-cookie-deletion
title: "CookieはSet-Cookieで有効期限を切ることでブラウザから削除できる"
created: 2026-04-18
source: [[2026-04-18_insight_cookie-basics-and-security.md]]
quiz_fail_log: []
---

## Summary
- **Cookie は、不要になったらブラウザ側またはサーバー側の指示で削除できます。**
- サーバーは `Set-Cookie` で有効期限を切ることで削除を指示できます。
- ログアウト時や状態のリセット時によく使われます。

## Tags
#http #web #cookie

## Links
- [[note-insight-cookie]]
- [[note-insight-set-cookie-header]]
- [[note-insight-session-cookie]]

## Body
Cookie を削除したいときは、ブラウザ設定から消す方法だけでなく、サーバー側から削除を指示する方法もあります。
実務では、同じ Cookie 名に対して有効期限を過去にするか `Max-Age=0` を返して、ブラウザに削除させる形がよく使われます。
これはログアウト時や、壊れた状態をリセットしたいときに役立ちます。

## Example
```http
Set-Cookie: session_id=; Max-Age=0; Path=/
```

このコードでは、`session_id` の有効期限を切って、ブラウザに削除させています。

## Action
- [ ] `Path` や `Domain` が違う Cookie を削除するときの注意点も確認する
