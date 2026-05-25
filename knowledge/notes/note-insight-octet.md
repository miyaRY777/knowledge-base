---
id: note-insight-octet
title: オクテットは8ビットをまとめた単位
created: 2026-05-11
source: [[2026-05-11_insight_ip-address-basics]]
review_streak: 0
last_reviewed_on: 2026-05-25
---

## Summary
- オクテットは、8ビットのまとまりを表す単位です。
- IPv4アドレスでは、ドットで区切られた各数字が1オクテットに対応します。
- 1オクテットで表せる値は、10進数では `0` から `255` までです。

## Tags
#network #computer #data #ip-address

## Links
- [[note-insight-bit]]
- [[note-insight-byte]]
- [[note-insight-ipv4]]

## Body
オクテットは、8ビットをひとまとまりとして扱う単位です。ネットワークでは、特にIPv4アドレスを説明するときによく出てきます。

IPv4アドレスの `192.168.1.1` は、ドットで4つの部分に分かれています。この `192`、`168`、`1`、`1` の各部分が1オクテットです。各オクテットは8ビットなので、表せる値は `0` から `255` までになります。

Rails 固有の機能名ではなく、ネットワークやデータ表現で使われる基本用語として理解するとよいです。
