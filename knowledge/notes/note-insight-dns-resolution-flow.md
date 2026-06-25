---
id: note-insight-dns-resolution-flow
title: DNSのフローはドメイン名入力からWebサーバー接続までの流れ
created: 2026-05-15
source: [[2026-05-15_insight_dns-resolution-flow]]
quiz_fail_log: []
---

## Summary
- DNSのフローは、入力したドメイン名からIPアドレスを得て、Webサーバーへ接続するまでの流れです。
- キャッシュがあれば保存済みの結果を返し、なければ階層的に問い合わせます。
- キャッシュがない場合は、ルートDNSサーバー、TLDのDNSサーバー、権威DNSサーバーの順にたどります。

## Tags
#network #internet #dns #domain

## Links
- [[note-insight-dns]]
- [[note-insight-dns-resolution]]
- [[note-insight-root-dns-server]]
- [[note-insight-tld-dns-server]]
- [[note-insight-authoritative-dns-server]]

## Body
DNSのフローは、ユーザーがドメイン名を入力してから、ブラウザがWebサーバーへ接続するまでの名前解決の流れです。まずDNSへ問い合わせ、キャッシュに対応する情報が残っていれば、そのIPアドレスをすぐ返せます。

キャッシュがなければ、問い合わせはDNSの階層に沿って進みます。最初にルートDNSサーバーが次の手がかりを示し、次にTLDのDNSサーバーが対象ドメインを管理するサーバーを案内し、最後に権威DNSサーバーが正式な情報を返します。ブラウザは得られたIPアドレスでWebサーバーへ接続します。

## Example
1. `www.example.com` を入力する
2. キャッシュがなければDNS階層を順にたどる
3. `203.0.113.10` のようなIPアドレスを受け取る
4. ブラウザがそのWebサーバーへ接続する


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] キャッシュDNSサーバーとTTLの関係を整理する
