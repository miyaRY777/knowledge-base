---
id: note-insight-cname-record
title: CNAMEレコードはドメイン名を別のドメイン名の別名にするDNSレコード
created: 2026-05-14
source: [[2026-05-14_insight_domain-dns-basics]]
---

## Summary
- CNAMEレコードは、あるドメイン名を別のドメイン名の別名として扱うDNSレコードです。
- サブドメインを別のドメイン名へ向けたいときによく使います。
- 値にはIPアドレスではなく、接続先となるドメイン名を指定します。

## Tags
#network #internet #dns #domain

## Links
- [[note-insight-dns]]
- [[note-insight-dns-settings]]
- [[note-insight-domain-name]]
- [[note-insight-a-record]]
- [[note-insight-subdomain]]

## Body
CNAMEレコードは、あるドメイン名を別のドメイン名の別名として扱うDNSレコードです。たとえば `www.example.com` を `example.com` へ向けるような設定で使えます。

AレコードがIPv4アドレスを指定するのに対して、CNAMEレコードはIPアドレスではなくドメイン名を指定します。サブドメインを外部サービスの指定ドメインへ向ける場合にもよく使われます。

## Example
```txt
www.example.com  CNAME  example.com
```

この例では、`www.example.com` を `example.com` の別名として扱います。

## Action
- [ ] apexドメインでCNAMEを使えない場合の代替を整理する
