---
id: note-insight-cookie-httponly
title: HttpOnly属性の要点
created: 2026-04-17
source: [[2026-04-17_insight_rails-cookies-headers-and-attributes.md]]
---

## Summary
- **`HttpOnly` は、JavaScript から Cookie を参照できなくする属性です。**
- XSS による Cookie 盗難リスクを下げる目的で使われます。
- サーバーとの HTTP 通信では引き続き Cookie を送れます。

## Tags
#http #web #cookie #security

## Links
- [[note-insight-set-cookie-header]]
- [[note-insight-cookie-secure]]
- [[note-insight-cookie]]
- [[note-insight-cookie-samesite]]

## Body
`HttpOnly` 属性を付けた Cookie は、ブラウザ内の JavaScript から読み取れなくなります。
これにより、悪意あるスクリプトが Cookie を盗み出すリスクを減らせます。
ただし、JavaScript から見えないだけで、ブラウザが HTTP リクエストでサーバーへ送る動作はそのまま行われます。

## Example
```http
Set-Cookie: user_id=12345; HttpOnly
```

このコードでは、`user_id` の Cookie を JavaScript から参照できないようにしています。

## Action
- [ ] XSS と Cookie 盗難の関係を別ノートで整理する
