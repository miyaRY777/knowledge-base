---
id: note-insight-cookie-samesite
title: SameSite属性の要点
created: 2026-04-18
source: [[2026-04-18_insight_cookie-basics-and-security.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- **`SameSite` は、クロスサイトのリクエストで Cookie を送るかどうかを制御する属性です。**
- `Lax` や `Strict` は不要なクロスサイト送信を抑え、CSRF 対策に役立ちます。
- `None` を使う場合は `Secure` も必要です。

## Tags
#http #web #cookie #security #privacy #要復習 #要復習

## Links
- [[note-insight-cookie]]
- [[note-insight-cookie-secure]]
- [[note-insight-cookie-httponly]]
- [[note-insight-third-party-cookie]]
- [[note-insight-set-cookie-header]]

## Body
`SameSite` は、別サイトから来たリクエストでもその Cookie を送るかどうかを調整するための属性です。
`Lax` は使いやすさを残しながら多くのクロスサイト送信を抑える設定で、`Strict` はより強く送信を制限します。
一方で `None` はクロスサイトでも送信できるようにする設定で、他サイトに埋め込まれたサービスなどで必要になることがあります。
ただし `None` は広く送れてしまうぶん注意が必要で、利用時には `Secure` も必須です。

## Example
```http
Set-Cookie: session_id=abc123; SameSite=Lax; Secure
```

このコードでは、利便性をある程度保ちながら、不要なクロスサイト送信を減らす設定をしています。

## Action
- [ ] `Lax` `Strict` `None` の違いをリクエスト例でも見比べる

<!-- review_log: 2026-04-18,2026-05-02 -->
