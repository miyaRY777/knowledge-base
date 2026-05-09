---
id: note-insight-dns
title: "DNSはドメイン名をIPアドレスに変換する仕組み"
created: 2026-05-09
source: [[2026-05-09_insight_dns-domain-ip-address]]
---

## Summary
- DNS は Domain Name System の略です。
- `example.com` のようなドメイン名を、対応するIPアドレスへ変換します。
- 人間が入力した名前で、コンピューターが通信先を見つけられるようにします。

## Tags
#network #internet #dns #domain

## Links
- [[note-insight-domain-name]]
- [[note-insight-ip-address]]

## Body
DNS は、ドメイン名とIPアドレスを結びつける仕組みです。よく「インターネットの電話帳」のように説明されます。人間は `example.com` のような名前を入力し、DNS がそれに対応するIPアドレスを探すことで、コンピューターが通信できる相手を見つけられます。

Webサイトにアクセスするとき、ブラウザはまず入力されたドメイン名に対応するIPアドレスを調べます。見つかったIPアドレスを使って、実際のサーバーへ接続します。

## Example
- ブラウザに `example.com` と入力する
- DNS が `example.com` に対応するIPアドレスを探す
- 見つかったIPアドレスのサーバーへアクセスする

## Action
- [ ] DNSレコードの種類を整理する
