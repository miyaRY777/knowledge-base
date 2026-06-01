# ネットワーク基礎マップ

> **このMOCで分かること**: 通信プロトコルの全体像から、IPアドレス・UDP・ネットワークソケットまでの通信の土台を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | 通信プロトコル | コンピューター同士が通信するときの約束ごと | [[note-insight-communication-protocol]] |
| 2 | TCP/IP | インターネット通信の土台となるプロトコル群 | [[note-insight-tcp-ip]] |
| 3 | FTP | ネットワーク経由でファイルを転送するプロトコル | [[note-insight-ftp]] |
| 4 | SMTP | メールを送信・配送するためのプロトコル | [[note-insight-smtp]] |
| 5 | IPアドレス | ネットワーク上の機器を識別する番号 | [[note-insight-ip-address]] |
| 6 | IPアドレスの一意性 | 同じネットワーク内で重複してはいけない理由 | [[note-insight-ip-address-uniqueness]] |
| 7 | IPv4 | 32ビットで構成される従来のIPアドレス形式 | [[note-insight-ipv4]] |
| 8 | IPv6 | 128ビットで構成される新しいIPアドレス形式 | [[note-insight-ipv6]] |
| 9 | ネットワーク識別 | IPアドレスでネットワークと機器を識別する仕組み | [[note-insight-network-identification]] |
| 10 | UDP | 高速な通信を重視する通信プロトコル | [[note-insight-udp]] |
| 11 | ネットワークソケット | プログラムが通信するための窓口 | [[note-insight-network-socket]] |

---

## 通信プロトコルの基礎

[[note-insight-communication-protocol]]
[[note-insight-tcp-ip]]
[[note-insight-ftp]]
[[note-insight-smtp]]

**ポイント**:
- プロトコルはコンピューター同士が通信するための共通の取り決め
- TCP/IP はインターネット全体の土台。IP がアドレス指定、TCP が確実な配送を担う
- FTP はファイル転送、SMTP はメール送信と、用途ごとに専用のプロトコルがある
- HTTP や HTTPS も TCP/IP の上で動くプロトコルの一つ

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
