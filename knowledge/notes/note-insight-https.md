---
id: note-insight-https
title: "HTTPSはHTTP通信を暗号化して保護する仕組み"
created: 2026-04-25
source: [[2026-04-25_insight_cookie-session-security-basics.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- HTTPS は HTTP を TLS で保護した通信方式。
- 通信内容の盗み見や改ざんのリスクを下げる。
- Cookie やログイン情報を扱うページでは特に重要。

## Tags
#http #web #security #https

## Links
- [[note-insight-cookie-secure]]
- [[note-insight-session]]
- [[note-insight-tls-current-encryption-protocol]]
- [[note-insight-ssl-legacy-encryption-protocol]]
- [[2026-05-08_insight_ssl-tls-basics]]

## Body
HTTPS は、HTTP 通信を TLS で暗号化して保護する仕組みです。ブラウザとサーバーの間の内容をそのまま読まれにくくし、途中で書き換えられる危険も下げます。ログイン情報や Cookie のような重要な情報を扱うページでは特に重要ですが、HTTPS を使っていてもアプリの実装上の脆弱性まで自動で防げるわけではありません。通信の保護とアプリケーションの安全性は分けて理解すると整理しやすいです。

説明では「HTTP通信を SSL/TLS で安全にしたもの」と言われることもあります。ただし現在のWebでは、実際には主に TLS が使われます。`http://example.com` は通信が暗号化されていない一方、`https://example.com` は TLS によってブラウザとサーバー間の通信が保護されます。

## Example
```http
GET /login HTTP/1.1
Host: example.com
```

この例では、HTTPS で保護された通信の中でブラウザがサーバーにリクエストを送るイメージを表しています。

- ログイン画面でパスワードを送る
- 決済画面でカード情報を送る
- HTTPS によって通信経路の盗み見や改ざんリスクを下げる


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
