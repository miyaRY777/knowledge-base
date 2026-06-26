---
id: note-insight-tls-current-encryption-protocol
title: "TLSは現在のHTTPS通信を保護する暗号化プロトコル"
created: 2026-04-29
source: [[2026-04-29_insight_ssl-tls-security-basics.md]]
review_streak: 1
last_reviewed_on: 2026-04-30
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- TLS は、ブラウザとWebサーバーの通信を暗号化して守る現在のプロトコル。
- 通信内容の盗み見や改ざんを防ぎ、ログイン情報などを安全に送るために使われる。
- 現在は TLS 1.3 や TLS 1.2 が使われ、古い TLS 1.0 や TLS 1.1 は避けるべきものとして扱われる。

## Tags
#web #security #tls #https #encryption

## Links
- [[note-insight-https]]
- [[note-insight-ssl-legacy-encryption-protocol]]
- [[note-insight-cookie-secure]]
- [[note-insight-man-in-the-middle-attack]]
- [[2026-05-08_insight_ssl-tls-basics]]

## Body
TLS は、HTTPS通信の中核になる暗号化プロトコルです。ブラウザとWebサーバーの間でやり取りされる内容を暗号化し、途中で盗み見されたり改ざんされたりするリスクを下げます。

ログインフォームで入力したメールアドレスやパスワードのような重要な情報は、平文のまま送ると危険です。HTTPS では TLS によって通信経路が保護されるため、第三者が内容を読み取りにくくなります。

実務では `SSL/TLS` のようにまとめて呼ばれることがありますが、現在のWeb通信で中心になるのは TLS です。`http://` の通信は暗号化されず、`https://` の通信は TLS によって保護される、と考えると関係を整理しやすいです。

## Example
- ユーザーがログインフォームに認証情報を入力する
- ブラウザが `https://` のWebサイトへ送信する
- TLS によって通信内容が暗号化される
- `http://example.com` は暗号化されず、`https://example.com` は TLS で保護される


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
