---
id: note-insight-udp
title: "UDPは高速な通信を重視する通信プロトコル"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
---

## Summary
- UDP（User Datagram Protocol）は、データの到達確認をせずに送信する通信方式です。
- TCPと比べて速いが、信頼性は低くなります。
- オンラインゲームや動画配信などリアルタイム性が重要な場面で使われます。

## Tags
#network #protocol

## Links
- [[note-insight-network-socket]]
- [[note-insight-ip-address]]

## Body
UDPは、送信したデータが相手に届いたかを確認しないプロトコルです。確認処理がない分、オーバーヘッドが少なく高速に通信できます。一部データが欠けても継続できるリアルタイム通信（FPSゲームの位置情報、ライブ配信など）に向いています。信頼性が必要な場面はTCPを使います。

## Example
- FPSゲームでプレイヤーの位置情報を毎秒大量に送る
- 一部パケットが欠けてもゲームは継続できる
- 遅延を最小限に抑えることが優先される
