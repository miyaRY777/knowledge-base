---
id: note-insight-dns-resolution
title: 名前解決はドメイン名から対応するIPアドレスを取得すること
created: 2026-05-15
source: [[2026-05-15_insight_dns-resolution-flow]]
quiz_fail_log: []
---

## Summary
- 名前解決は、ドメイン名から対応するIPアドレスを取得する処理です。
- 人間が扱いやすい名前を、通信で使う接続先情報へ変換します。
- Webサイトへアクセスするとき、ブラウザが接続先を見つける前段で必要になります。

## Tags
#network #internet #dns #domain

## Links
- [[note-insight-dns]]
- [[note-insight-domain-name]]
- [[note-insight-ip-address]]
- [[note-insight-dns-resolution-flow]]

## Body
名前解決は、`www.example.com` のようなドメイン名から、それに対応するIPアドレスを取得することです。人間は覚えやすい名前を入力しますが、実際の通信ではIPアドレスが使われるため、その橋渡しが必要になります。

DNSを使った名前解決が終わると、ブラウザは取得したIPアドレスを使って目的のサーバーへ接続できます。

## Example
- `www.example.com` へアクセスしたい
- DNSへ問い合わせる
- 対応するIPアドレスを受け取る


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] 正引きと逆引きの違いを整理する
