---
id: note-insight-ipv6
title: IPv6は128ビットで表すIPアドレス形式
created: 2026-05-11
source: [[2026-05-11_insight_ip-address-basics]]
review_streak: 1
last_reviewed_on: 2026-05-25
quiz_streak: 0
quiz_fail_log: []
---

## Summary
- IPv6は、IPアドレスを128ビットで表す形式です。
- IPv4よりも非常に多くのアドレスを扱えます。
- `2001:db8::1` のように、コロン区切りの16進数で表します。

## Tags
#network #internet #ip-address #ipv6

## Links
- [[note-insight-ip-address]]
- [[note-insight-ipv4]]

## Body
IPv6は128ビットで表すIPアドレス形式で、32ビットの IPv4（約43億通り）に対して、約340澗通りのアドレスを表現できます。
表記は `2001:db8::1` のようにコロン区切りの16進数8グループで、`::` は連続する 0 のグループを省略する記法です。`::1` はループバックアドレス（自分自身）を表します。
IoT機器の普及でIPv4アドレスが枯渇しつつあるため IPv6 への移行が進んでいますが、現在は両方が混在するデュアルスタック構成が多いです。

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
