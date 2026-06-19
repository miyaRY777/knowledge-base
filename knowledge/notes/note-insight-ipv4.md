---
id: note-insight-ipv4
title: IPv4は32ビットを4つのオクテットで表すIPアドレス形式
created: 2026-05-11
source: [[2026-05-11_insight_ip-address-basics]]
review_streak: 1
last_reviewed_on: 2026-05-25
quiz_fail_log: []
---

## Summary
- IPv4は、IPアドレスを32ビットで表す形式です。
- 32ビットを8ビットずつ4つに分け、ドット区切りの10進数で表します。
- `192.168.1.1` のような表記では、各区切りが1オクテットです。

## Tags
#network #internet #ip-address #ipv4

## Links
- [[note-insight-ip-address]]
- [[note-insight-octet]]
- [[note-insight-byte]]
- [[note-insight-network-identification]]

## Body
IPv4は、ネットワーク上の機器や通信相手を識別するためのIPアドレス形式のひとつです。アドレス全体は32ビットで構成されます。

人間が読む表記では、32ビットを8ビットずつ4つに分け、各部分を10進数にしてドットで区切ります。たとえば `192.168.1.1` は4つのオクテットで構成されたIPv4アドレスです。各オクテットは1バイトなので、それぞれの値は `0` から `255` の範囲になります。

IPv4は Rails 固有の用語ではなく、ネットワーク全般で使われる基本的なアドレス形式です。
