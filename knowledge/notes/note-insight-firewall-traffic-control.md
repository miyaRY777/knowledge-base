---
id: note-insight-firewall-traffic-control
title: "ファイアウォールは通信を許可またはブロックする仕組み"
created: 2026-04-29
source: [[2026-04-29_insight_ssl-tls-security-basics.md]]
review_streak: 0
last_reviewed_on: 2026-05-13
---

## Summary
- ファイアウォールは、ネットワーク通信を通すか止めるかを判断するセキュリティの仕組み。
- IPアドレス、ポート番号、アプリケーションなどの条件に基づいて通信を制御する。
- 必要な通信だけを許可し、不要または危険な通信を減らすために使われる。

## Tags
#network #security #firewall #internet-security #要復習

## Links
- [[note-insight-internet-security]]
- [[note-insight-cyber-attack]]

## Body
ファイアウォールは、ネットワークに入ってくる通信や外へ出ていく通信を確認し、条件に合うものだけを許可する仕組みです。通信の入口でルールを適用することで、不要なアクセスや危険な通信を減らします。

たとえばWebサーバーでは、Webアクセスに必要なポートは開き、管理用のポートは特定のIPアドレスからだけ使えるように制限します。すべての通信を通すのではなく、必要な通信だけを通すことが重要です。

## Example
- Webアクセス用の `80` 番や `443` 番ポートを許可する
- 管理用ポートは特定IPアドレスだけに制限する
- 不審な通信や不要な通信をブロックする

## Action
- [ ] ポート番号とファイアウォールルールの関係を整理する

<!-- review_log: 2026-05-02 -->
