---
id: note-insight-cookie-httponly
title: "HttpOnly属性はJavaScriptからCookieを参照できなくする属性"
created: 2026-04-17
source: [[2026-04-17_insight_rails-cookies-headers-and-attributes.md]]
review_streak: 1
last_reviewed_on: 2026-04-30
quiz_streak: 1
quiz_fail_log: []
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
ただし、JavaScript から見えないだけで、ブラウザが HTTP リクエストでサーバーへ送る動作はそのまま行われます。また、通信経路を HTTPS に限定する役割は持たないため、必要に応じて `Secure` と組み合わせて使うことが重要です。

## Example
```http
Set-Cookie: session_id=abc123; HttpOnly
```

このコードでは、`session_id` の Cookie を JavaScript から参照できないようにしています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] XSS と Cookie 盗難の関係を別ノートで整理する

<!-- review_log: 2026-05-02 -->
