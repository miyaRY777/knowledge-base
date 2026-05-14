---
id: note-insight-dns-server
title: DNSサーバーはドメイン名に関する問い合わせへ応答するサーバー
created: 2026-05-14
source: [[2026-05-14_insight_domain-dns-basics]]
---

## Summary
- DNSサーバーは、ドメイン名に関する問い合わせへ応答するサーバーです。
- ドメイン名に対応するIPアドレスや、次に問い合わせるべきDNSサーバーの情報を返します。
- DNSは階層構造になっており、必要な情報を持つサーバーへたどっていきます。

## Tags
#network #internet #dns #domain

## Links
- [[note-insight-dns]]
- [[note-insight-domain-name]]
- [[note-insight-ip-address]]
- [[note-insight-dns-settings]]

## Body
DNSサーバーは、`example.com` のようなドメイン名に関する問い合わせを受け取り、必要な情報を返すサーバーです。問い合わせ内容によって、対応するIPアドレスを返したり、より詳しい情報を持つDNSサーバーを案内したりします。

DNSは階層的に管理されているため、1台のサーバーだけがすべてを知っているわけではありません。問い合わせは、目的のドメイン情報に近いDNSサーバーへ順にたどられます。

## Example
- ブラウザが `example.com` へアクセスしようとする
- DNSサーバーへ対応する情報を問い合わせる
- 返ってきたIPアドレスを使ってWebサーバーへ接続する

## Action
- [ ] 権威DNSサーバーとキャッシュDNSサーバーの違いを整理する
