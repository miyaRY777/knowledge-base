# ネットワーク基礎マップ

> **このMOCで分かること**: IPアドレスの役割・種類から、UDP・ネットワークソケットまでの通信の土台を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | IPアドレス | ネットワーク上の機器を識別する番号 | [[note-insight-ip-address]] |
| 2 | IPアドレスの一意性 | 同じネットワーク内で重複してはいけない理由 | [[note-insight-ip-address-uniqueness]] |
| 3 | IPv4 | 32ビットで構成される従来のIPアドレス形式 | [[note-insight-ipv4]] |
| 4 | IPv6 | 128ビットで構成される新しいIPアドレス形式 | [[note-insight-ipv6]] |
| 5 | ネットワーク識別 | IPアドレスでネットワークと機器を識別する仕組み | [[note-insight-network-identification]] |
| 6 | UDP | 高速な通信を重視する通信プロトコル | [[note-insight-udp]] |
| 7 | ネットワークソケット | プログラムが通信するための窓口 | [[note-insight-network-socket]] |

---

## IPアドレスの基礎

[[note-insight-ip-address]]
[[note-insight-ip-address-uniqueness]]
[[note-insight-ipv4]]
[[note-insight-ipv6]]
[[note-insight-network-identification]]

**ポイント**:
- IPアドレスはネットワーク上の「住所」。同一ネットワーク内で重複できない
- IPv4は `192.168.0.1` の形式（32ビット）。枯渇問題からIPv6へ移行が進んでいる
- IPv6は `2001:db8::1` の形式（128ビット）。ほぼ無限のアドレス数を確保
- ネットワーク部とホスト部に分かれており、どのネットワークのどの機器かを表す

---

## 通信プロトコルとソケット

[[note-insight-udp]]
[[note-insight-network-socket]]

**ポイント**:
- UDPは到達確認なしの高速通信。リアルタイムゲーム・動画配信に向いている（TCPと対比で覚える）
- ネットワークソケットはアプリとネットワークをつなぐ通信口。IPアドレス + ポート番号で識別
- クライアントソケット（接続側）とサーバーソケット（待機側）の2種類がある

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| TCPとUDPの使い分け基準を整理する | - | - | [[note-insight-udp]] |
| ポート番号の役割・予約ポート番号を整理する | - | - | [[note-insight-network-socket]] |
| サブネットマスクの概念を別ノートにするか | - | - | - |

---

## 関連リンク

- [[map-dns-domain-basics]]
- [[map-http-client-basics]]
- [[map-web-security-basics]]
