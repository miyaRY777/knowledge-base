# DNS・ドメイン基礎マップ

> **このMOCで分かること**: ドメイン名の構造からDNS解決の仕組み、各種レコードの役割までを俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | DNS | ドメイン名をIPアドレスに変換する仕組み | [[note-insight-dns]] |
| 2 | DNSサーバー | ドメインとIPの対応を管理するサーバー | [[note-insight-dns-server]] |
| 3 | DNS解決 | ドメイン名からIPアドレスを取得するプロセス | [[note-insight-dns-resolution]] |
| 4 | DNS解決の流れ | ブラウザからIPアドレスを得るまでの順序 | [[note-insight-dns-resolution-flow]] |
| 5 | ルートDNSサーバー | DNS階層の最上位にあるサーバー | [[note-insight-root-dns-server]] |
| 6 | TLDのDNSサーバー | .comや.jpなどのTLDを管理するサーバー | [[note-insight-tld-dns-server]] |
| 7 | 権威DNSサーバー | ドメインの正式な情報を持つサーバー | [[note-insight-authoritative-dns-server]] |
| 8 | ドメイン名 | ウェブサイトの住所を人が読める形で表したもの | [[note-insight-domain-name]] |
| 9 | トップレベルドメイン | ドメインの最末尾（.com / .jp など） | [[note-insight-top-level-domain]] |
| 10 | セカンドレベルドメイン | TLDのひとつ手前の部分 | [[note-insight-second-level-domain]] |
| 11 | サブドメイン | ドメインの先頭に付く区分け用の部分 | [[note-insight-subdomain]] |
| 12 | ドメイン登録 | ドメイン名を取得して使えるようにする手続き | [[note-insight-domain-registration]] |
| 13 | ドメインレジストラ | ドメイン登録を仲介する事業者 | [[note-insight-domain-registrar]] |
| 14 | DNS設定 | ドメインに対してDNSレコードを設定すること | [[note-insight-dns-settings]] |
| 15 | Aレコード | ドメインをIPv4アドレスに対応付けるレコード | [[note-insight-a-record]] |
| 16 | CNAMEレコード | ドメインを別のドメイン名に対応付けるレコード | [[note-insight-cname-record]] |

---

## ドメインの構造

[[note-insight-domain-name]]
[[note-insight-top-level-domain]]
[[note-insight-second-level-domain]]
[[note-insight-subdomain]]

**ポイント**:
- ドメインは右から読む：`www.example.com` → TLD(`.com`) → SLD(`example`) → サブドメイン(`www`)
- TLDは `.com`・`.jp` などの種別。SLDはサービス固有の名前
- サブドメインはひとつのドメイン配下を目的別に分けるために使う（`api.`・`mail.`など）

---

## DNS解決の仕組み

[[note-insight-dns]]
[[note-insight-dns-resolution]]
[[note-insight-dns-resolution-flow]]
[[note-insight-root-dns-server]]
[[note-insight-tld-dns-server]]
[[note-insight-authoritative-dns-server]]
[[note-insight-dns-server]]

**ポイント**:
- DNS解決はブラウザ → キャッシュ → フルリゾルバ → ルートDNS → TLD DNS → 権威DNS の順で進む
- 権威DNSサーバーが最終的なIPアドレスを返す
- キャッシュが有効な間は上位サーバーへの問い合わせをスキップできる

---

## ドメイン取得と設定

[[note-insight-domain-registration]]
[[note-insight-domain-registrar]]
[[note-insight-dns-settings]]
[[note-insight-a-record]]
[[note-insight-cname-record]]

**ポイント**:
- ドメイン取得はレジストラを通して行う
- 取得後、AレコードやCNAMEレコードなどのDNSレコードを設定してサービスと紐付ける
- Aレコードは直接IPアドレスを指定。CNAMEは別のドメイン名へ委ねる

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| MXレコード・TXTレコードの役割を整理する | - | - | - |
| TTLとDNSキャッシュの関係を整理する | - | - | [[note-insight-dns-resolution]] |

---

## 関連リンク

- [[map-network-basics]]
- [[map-http-client-basics]]
