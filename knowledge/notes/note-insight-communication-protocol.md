---
id: note-insight-communication-protocol
title: 通信プロトコルはコンピューター同士が通信するときの約束ごと
created: 2026-05-05
source: [[2026-05-05_insight_network-protocol-basics]]
quiz_fail_log: []
---

## Summary
- 通信プロトコルは、データをどの形式で送り、どう受け取り、どう返事するかを決めたルールです。
- このルールを揃えることで、異なるコンピューター同士がデータをやり取りできます。
- HTTP、FTP、SMTP、TCP/IP など、用途ごとに異なるプロトコルが存在します。

## Tags
#network #protocol #internet #basics

## Links
- [[note-insight-http-request]]
- [[note-insight-ftp]]
- [[note-insight-smtp]]
- [[note-insight-tcp-ip]]

## Body
通信プロトコルは、コンピューター同士がデータをやり取りするときに従う約束ごとです。送る側と受け取る側が同じルールに従うことで、異なるOS、異なるメーカーの機器でも通信が成り立ちます。

用途ごとに異なるプロトコルがあります。Webページの取得にはHTTP、ファイル転送にはFTP、メール送信にはSMTP、インターネット通信の基盤にはTCP/IPが使われます。RailsアプリはHTTPリクエストを受け取って処理しており、プロトコルの存在がなければサーバーとブラウザは共通の言葉で話せません。
