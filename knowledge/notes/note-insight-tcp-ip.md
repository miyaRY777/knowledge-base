---
id: note-insight-tcp-ip
title: TCP/IPはインターネット通信の土台となるプロトコル群
created: 2026-05-05
source: [[2026-05-05_insight_network-protocol-basics]]
quiz_fail_log: []
---

## Summary
- TCP/IPは、インターネット上でデータを正しい相手へ届けるための基本的なプロトコルの組み合わせです。
- IPはどこへ届けるかを担い、TCPはデータが順番どおり・確実に届くようにする役割を持ちます。
- HTTPやSMTPなど、多くのアプリケーションプロトコルはTCP/IPを土台として動きます。

## Tags
#network #protocol #tcp #ip

## Links
- [[note-insight-communication-protocol]]
- [[note-insight-http-request]]
- [[note-insight-smtp]]

## Body
TCP/IPは、インターネット通信を支える2つのプロトコルを組み合わせた呼び方です。IPがデータをどこへ届けるかという「アドレス指定と経路」を担い、TCPがデータの分割・順序管理・再送を行って確実な配送を担います。

WebブラウザでWebサイトを見るときも、Railsアプリが外部APIと通信するときも、メールやファイル転送でも、TCP/IPが通信の土台として機能しています。HTTP、SMTP、FTPなどのアプリケーション層のプロトコルは、TCP/IPの上で動く仕組みです。
