---
id: note-insight-ssl-certificate-name-for-tls
title: "SSL証明書は現在のTLS通信で使う証明書を指すことが多い"
created: 2026-04-29
source: [[2026-04-29_insight_ssl-tls-security-basics.md]]
review_streak: 1
last_reviewed_on: 2026-04-30
quiz_streak: 1
---

## Summary
- SSL証明書という名前は残っているが、現在のHTTPS通信では主に TLS のための証明書として使われる。
- 証明書は、接続先サーバーが信頼できる相手かを確認するために使われる。
- ブラウザが証明書を確認し、問題がなければ HTTPS の暗号化通信を始められる。

## Tags
#web #security #ssl #tls #certificate #https #要復習

## Links
- [[note-insight-https]]
- [[note-insight-tls-current-encryption-protocol]]
- [[note-insight-ssl-legacy-encryption-protocol]]
- [[note-insight-man-in-the-middle-attack]]

## Body
実務では「SSL証明書」という呼び方がよく使われますが、現在のHTTPS通信で実際に使われる仕組みは基本的に TLS です。そのため、SSL証明書という言葉は、昔から残っている名前として理解すると混乱しにくくなります。

証明書は、ブラウザが接続先サーバーを確認し、安全な通信を始めるために使われます。証明書に問題がなければ、ブラウザとサーバーは HTTPS で通信できます。

## Example
- サーバーに証明書を設定する
- ブラウザが証明書を確認する
- 問題がなければ `https://` で通信できる

## Action
- [ ] SSL証明書、TLS証明書、HTTPS の関係を図で整理する

<!-- review_log: 2026-05-02 -->
