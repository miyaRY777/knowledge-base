# 2026年5月学習マップ

> **このMOCで分かること**: 2026年5月に学んだ内容の全体像、テーマ別の入口、今月の重要ポイント

---

## 今月のサマリー

| 項目 | 内容 |
|------|------|
| 期間 | 2026-05 |
| 主なテーマ | ネットワーク・HTTP・DNS / データベース発展 / Docker / CS基礎（データ型・文字コード） |
| inboxファイル数 | 23件 |
| 作成ノート数 | 約100件 |

---

## テーマ別マップ

| # | テーマ | 概要 | MOC |
|---|--------|------|-----|
| 1 | ネットワーク・HTTP・DNS | プロトコル基礎からDNS解決まで | [[map-network-basics]] / [[map-http-status-and-methods]] / [[map-dns-domain-basics]] |
| 2 | データベース発展 | ER図・正規化・ACID・インデックス・ロック・分散DB | [[map-database-advanced]] |
| 3 | Docker | コンテナ技術の基礎概念 | [[map-docker-basics]] |
| 4 | CS基礎（データ型・文字コード） | ビット/バイト、数値型、文字コード、エンコーディング | [[map-data-types-and-binary-basics]] / [[map-character-encoding-basics]] |

---

## 今月の重要概念

[[note-insight-tcp-ip]]
[[note-insight-dns-resolution-flow]]
[[note-insight-acid-properties]]
[[note-insight-database-normalization]]
[[note-insight-docker]]
[[note-insight-character-encoding]]
[[note-insight-integer-data-type]]

**ポイント**:
- TCP/IPはHTTP・SMTP・FTPなどすべてのプロトコルが乗る土台。まず押さえる
- DNS解決フローはドメイン→IPを引く流れ全体を俯瞰できる重要な概念
- ACID特性はトランザクションの信頼性の根拠。4つの性質とそれぞれの意味を整理する
- 正規化（第1〜3正規形）はDB設計の基本方針。重複を減らしデータ整合性を守る
- Dockerはコンテナ単位で環境を統一する仕組み。イメージ・コンテナ・Dockerfileの関係を理解する
- 文字コードはASCII→Unicode→UTF-8の流れで整理すると全体像が見えやすい

---

## 今月追加した代表ノート

| 分野 | ノート |
|------|--------|
| ネットワーク | [[note-insight-communication-protocol]], [[note-insight-tcp-ip]], [[note-insight-ftp]], [[note-insight-smtp]], [[note-insight-udp]] |
| DNS・ドメイン | [[note-insight-dns-resolution-flow]], [[note-insight-authoritative-dns-server]], [[note-insight-root-dns-server]], [[note-insight-a-record]], [[note-insight-cname-record]] |
| DB発展 | [[note-insight-database-normalization]], [[note-insight-acid-properties]], [[note-insight-database-index-types]], [[note-insight-database-lock-types]], [[note-insight-distributed-database]] |
| Docker | [[note-insight-docker]], [[note-insight-dockerfile]], [[note-insight-docker-container]] |
| CS基礎 | [[note-insight-bit]], [[note-insight-character-encoding]], [[note-insight-unicode]], [[note-insight-integer-data-type]], [[note-insight-integer-overflow]] |

---

## 未決事項（Open Questions）

| 項目 | 関連MOC |
|------|---------|
| OSI参照モデルとTCP/IPの対応を整理したい | [[map-network-basics]] |
| インデックスをどの列に付けるべきか判断基準を深掘りしたい | [[map-database-advanced]] |
| Docker Composeの概念・使い方を学ぶ | [[map-docker-basics]] |

---

## 関連リンク

- [[map-network-basics]]
- [[map-http-status-and-methods]]
- [[map-dns-domain-basics]]
- [[map-database-fundamentals]]
- [[map-database-advanced]]
- [[map-docker-basics]]
- [[map-data-types-and-binary-basics]]
- [[map-character-encoding-basics]]
