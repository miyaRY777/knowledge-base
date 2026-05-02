---
id: note-insight-https
title: "HTTPSはHTTP通信を暗号化して保護する仕組み"
created: 2026-04-25
source: [[2026-04-25_insight_cookie-session-security-basics.md]]
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

## Body
HTTPS は、HTTP 通信を TLS で暗号化して保護する仕組みです。ブラウザとサーバーの間の内容をそのまま読まれにくくし、途中で書き換えられる危険も下げます。ログイン情報や Cookie のような重要な情報を扱うページでは特に重要ですが、HTTPS を使っていてもアプリの実装上の脆弱性まで自動で防げるわけではありません。通信の保護とアプリケーションの安全性は分けて理解すると整理しやすいです。

## Example
```http
GET /login HTTP/1.1
Host: example.com
```

この例では、HTTPS で保護された通信の中でブラウザがサーバーにリクエストを送るイメージを表しています。

## Action
- [ ] TLS が通信のどこを守るのかも後で整理する
