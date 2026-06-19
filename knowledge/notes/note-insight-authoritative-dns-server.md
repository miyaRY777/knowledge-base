---
id: note-insight-authoritative-dns-server
title: 権威DNSサーバーはそのドメインの正式なDNS情報を持つ
created: 2026-05-15
source: [[2026-05-15_insight_dns-resolution-flow]]
quiz_fail_log: []
---

## Summary
- 権威DNSサーバーは、特定ドメインの正式なDNS情報を管理するサーバーです。
- 対象ドメインのAレコードやCNAMEレコードなど、実際の回答を返します。
- 名前解決では、最終的に正式な接続先情報を返す役割を担います。

## Tags
#network #internet #dns #domain

## Links
- [[note-insight-dns-server]]
- [[note-insight-dns-resolution-flow]]
- [[note-insight-a-record]]
- [[note-insight-cname-record]]
- [[note-insight-tld-dns-server]]

## Body
権威DNSサーバーは、あるドメインについて正式なDNS情報を持つサーバーです。`example.com` を管理している権威DNSサーバーであれば、`www.example.com` の接続先に関する情報を返せます。

ルートDNSサーバーやTLDのDNSサーバーは、主に次の問い合わせ先を案内します。一方、権威DNSサーバーは、そのドメインに対する最終的な回答を返す立場です。

## Example
- `www.example.com` の接続先を知りたい
- `example.com` の権威DNSサーバーへ問い合わせる
- `203.0.113.10` のようなIPアドレスが返る

## Action
- [ ] 権威DNSサーバーとキャッシュDNSサーバーの違いを整理する
