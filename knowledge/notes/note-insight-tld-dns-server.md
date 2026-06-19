---
id: note-insight-tld-dns-server
title: TLDのDNSサーバーは次に聞くべき権威DNSサーバーを案内する
created: 2026-05-15
source: [[2026-05-15_insight_dns-resolution-flow]]
quiz_fail_log: []
---

## Summary
- TLDのDNSサーバーは、`.com` や `.jp` などのTLDごとの情報を扱います。
- 対象ドメインについて、次に問い合わせるべき権威DNSサーバーを案内します。
- ルートDNSサーバーと権威DNSサーバーの間をつなぐ役割です。

## Tags
#network #internet #dns #domain

## Links
- [[note-insight-top-level-domain]]
- [[note-insight-root-dns-server]]
- [[note-insight-authoritative-dns-server]]
- [[note-insight-dns-resolution-flow]]

## Body
TLDのDNSサーバーは、`.com` や `.jp` のようなトップレベルドメインごとに管理されるDNSサーバーです。`example.com` を調べるときは、`.com` を扱うDNSサーバーが、`example.com` の正式な情報を持つDNSサーバーを案内します。

このサーバー自身が最終的なIPアドレスを返すのではなく、問い合わせを対象ドメインの権威DNSサーバーへ進める役割を持ちます。

## Example
- ルートDNSサーバーから `.com` のDNSサーバーを案内される
- `.com` のDNSサーバーへ問い合わせる
- `example.com` の権威DNSサーバーを教えてもらう

## Action
- [ ] ccTLD と gTLD の違いを整理する
