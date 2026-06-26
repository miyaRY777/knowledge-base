---
id: note-insight-cookie-samesite
title: "SameSite属性はクロスサイトリクエストでCookieを送るかを制御する属性"
created: 2026-04-18
source: [[2026-04-18_insight_cookie-basics-and-security.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- **`SameSite` は、クロスサイトのリクエストで Cookie を送るかどうかを制御する属性です。**
- `Lax` や `Strict` は不要なクロスサイト送信を抑え、CSRF 対策に役立ちます。
- `None` を使う場合は `Secure` も必要です。

## Tags
#http #web #cookie #security #privacy

## Links
- [[note-insight-cookie]]
- [[note-insight-cookie-secure]]
- [[note-insight-cookie-httponly]]
- [[note-insight-third-party-cookie]]
- [[note-insight-set-cookie-header]]
- [[note-insight-csrf]]

## Body
`SameSite` は、別サイトから来たリクエストでもその Cookie を送るかどうかを調整するための属性です。
クロスサイト送信とは、ユーザーが見ているサイトとは別のサイト文脈から、自分のサイトへリクエストが送られることです。

`Lax` は使いやすさを残しながら多くのクロスサイト送信を抑える設定です。外部サイトのリンクから移動するような通常のトップレベル遷移では Cookie が送られることがありますが、クロスサイトの `POST` などでは送られにくくなります。

`Strict` はさらに強く制限し、クロスサイト文脈から来たリクエストでは Cookie を送らない設定です。セキュリティを優先しやすい一方で、外部リンクから来たときにログイン状態が引き継がれないように見えることがあります。

`None` はクロスサイトでも Cookie を送れるようにする設定で、他サイトに埋め込まれたサービスや外部連携で必要になることがあります。ただし広く送れるぶん注意が必要で、利用時には `Secure` も必須です。

## Example
```http
Set-Cookie: session_id=abc123; SameSite=Lax; Secure
```

このコードでは、利便性をある程度保ちながら、不要なクロスサイト送信を減らす設定をしています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
