---
id: note-insight-smtp
title: SMTPはメールを送信・配送するためのプロトコル
created: 2026-05-05
source: [[2026-05-05_insight_network-protocol-basics]]
quiz_fail_log: []
---

## Summary
- SMTP（Simple Mail Transfer Protocol）は、メールを送信したり、メールサーバー同士で配送したりするためのプロトコルです。
- 「送る・届ける」ための仕組みであり、メールを受信して読む機能は持ちません。
- Railsアプリではパスワード再設定メールや通知メールなどを送るときにSMTPが使われます。

## Tags
#network #protocol #email #smtp

## Links
- [[note-insight-communication-protocol]]
- [[note-insight-http-request]]

## Body
SMTPは、送信者のメールクライアントからメールサーバーへメールを渡したり、メールサーバー同士でメールを中継・配送したりする役割を担うプロトコルです。受信して読むためのプロトコル（IMAPやPOPなど）とは別物です。

Railsアプリでは、Action Mailerを使ってユーザーへメールを送るときにSMTPを経由します。SendGridやResendのようなメール配信サービスも、内部的にSMTPを使ってメールを届けています。
