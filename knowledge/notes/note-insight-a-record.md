---
id: note-insight-a-record
title: Aレコードはドメイン名をIPv4アドレスへ向けるDNSレコード
created: 2026-05-14
source: [[2026-05-14_insight_domain-dns-basics]]
quiz_fail_log: []
---

## Summary
- Aレコードは、ドメイン名をIPv4アドレスへ向けるDNSレコードです。
- 特定のWebサーバーのIPアドレスへドメイン名を接続したいときに使います。
- 値にはドメイン名ではなくIPv4アドレスを指定します。

## Tags
#network #internet #dns #domain #ip-address

## Links
- [[note-insight-dns]]
- [[note-insight-dns-settings]]
- [[note-insight-ipv4]]
- [[note-insight-cname-record]]

## Body
Aレコードは、`example.com` のようなドメイン名をIPv4アドレスへ対応づけるDNSレコードです。Webサーバーが固定のIPv4アドレスを持っていて、そのサーバーへドメイン名でアクセスさせたいときに使います。

Aレコードでは、接続先として `203.0.113.10` のようなIPv4アドレスを指定します。別のドメイン名を指定する用途にはCNAMEレコードを使います。

## Example
```txt
example.com  A  203.0.113.10
```

この例では、`example.com` を `203.0.113.10` のIPv4アドレスへ向けています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] AAAAレコードとの違いを整理する
