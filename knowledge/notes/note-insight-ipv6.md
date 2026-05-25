---
id: note-insight-ipv6
title: IPv6は128ビットで表すIPアドレス形式
created: 2026-05-11
source: [[2026-05-11_insight_ip-address-basics]]
review_streak: 1
last_reviewed_on: 2026-05-25
---

## Summary
- IPv6は、IPアドレスを128ビットで表す形式です。
- IPv4よりも非常に多くのアドレスを扱えます。
- `2001:db8::1` のように、コロン区切りの16進数で表します。

## Tags
#network #internet #ip-address #ipv6 #要復習

## Links
- [[note-insight-ip-address]]
- [[note-insight-ipv4]]

## Body
IPv6は、IPアドレスを128ビットで表す形式です。32ビットで表すIPv4よりも扱えるアドレス数が大きく、より多くの機器にアドレスを割り当てられます。

表記では、`2001:db8::1` のようにコロンで区切った16進数を使います。`::1` はローカルホストを表すIPv6アドレスとしてよく見かける例です。

IPv6も Rails 固有の機能名ではなく、ネットワーク全般で使われるIPアドレス形式です。
