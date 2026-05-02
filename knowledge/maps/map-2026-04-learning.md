# 2026年4月学習マップ

> **このMOCで分かること**: 2026年4月に学んだ内容の全体像、テーマ別の入口、今月の重要ポイント

---

## 今月のサマリー

| 項目 | 内容 |
|------|------|
| 期間 | 2026-04 |
| 主なテーマ | HTTP / Axios / JavaScriptループ / Stimulus基礎 / Rails管理者とseed / Turboと認可 / Cookie / Session / Webセキュリティ / Active Record Query / データベース基礎 / コンピュータ構成 |
| 入口ノート | [[2026-04-07_insight_knowledge-base.md]] |
| 既存基礎マップ | [[map-rails-basics]] |

---

## テーマ別マップ

| # | テーマ | 概要 | MOC |
|---|--------|------|-----|
| 1 | HTTPクライアント基礎 | Axios、Fetch、Promise、HTTPメソッド、通信設定 | [[map-http-client-basics]] |
| 2 | JavaScriptループ基礎 | `for`、初期化、増減式、無限ループ、配列処理 | [[map-javascript-loop-basics]] |
| 3 | Stimulus基礎 | connect、targets、values、event、dataset、classList | [[map-stimulus-basics]] |
| 4 | Rails管理者・seed基礎 | boolean、trait、admin判定、seed、DB準備 | [[map-rails-admin-and-seed-basics]] |
| 5 | Railsコントローラ安全性とTurbo | Turbo Stream、例外処理、認可、IDOR、Relation | [[map-rails-controller-safety-and-turbo]] |
| 6 | Cookie基礎 | Cookieの役割、送受信、保持期間、セキュリティ属性 | [[map-cookie-basics]] |
| 7 | Session基礎 | セッション、セッションID、ログイン状態、Cookieとの関係 | [[map-session-basics]] |
| 8 | Webセキュリティ基礎 | HTTPS、TLS、SSL、2FA、ファイアウォール、Cookie属性 | [[map-web-security-basics]] |
| 9 | サイバー攻撃基礎 | XSS、DDoS、フィッシング、中間者攻撃、セッションハイジャック | [[map-cyber-attack-basics]] |
| 10 | Active Record Query基礎 | Relation、where.not、N+1、includes、preload、eager_load | [[map-activerecord-query-basics]] |
| 11 | データベース基礎 | DBMS、SQL、テーブル、制約、トランザクション、インデックス | [[map-database-fundamentals]] |
| 12 | コンピュータ構成基礎 | CPU、メモリ、ストレージ、バス、五大装置 | [[map-computer-architecture-basics]] |
| 13 | Ruby / Rails predicate基礎 | blank?、present?、presence、nil?、empty? の使い分け | [[map-ruby-rails-predicate-basics]] |
| 14 | Rails基礎 | 3月末からの既存知識の土台 | [[map-rails-basics]] |
| 15 | Kaminariページネーション基礎 | ページネーションの全体テンプレートと個別パーシャル | [[map-kaminari-pagination-basics]] |

---

## 今月の重要概念

[[note-insight-http-request]]
[[note-insight-promise]]
[[note-insight-stimulus-connect-callback]]
[[note-insight-stimulus-targets]]
[[note-insight-axios-instance]]
[[note-insight-current-user-admin]]
[[note-insight-idor]]
[[note-insight-active-record-relation]]
[[note-insight-cookie]]
[[note-insight-cookie-httponly]]
[[note-insight-session]]
[[note-insight-session-id]]
[[note-insight-https]]
[[note-insight-tls-current-encryption-protocol]]
[[note-insight-xss]]
[[note-insight-session-hijacking]]
[[note-insight-n-plus-one]]
[[note-insight-database]]
[[note-insight-sql]]
[[note-insight-database-transaction]]
[[note-insight-function-method-argument-basics]]
[[note-insight-object-oriented-programming]]
[[note-insight-homebrew]]

**ポイント**:
- JavaScript 側では「通信の基本」と「非同期処理」の理解が土台
- Stimulus では「接続」「要素参照」「イベント処理」の役割分担が理解の土台
- Rails 側では「権限」「例外」「安全な取得」の理解が重要
- Turbo 対応では request 形式ごとの振る舞い分岐を意識する
- Cookie / Session は「HTTPが状態を持たない」前提から理解すると整理しやすい
- Webセキュリティでは、通信の暗号化、Cookie属性、認証情報を狙う攻撃がつながっている
- Active Record Query とデータベース基礎は、SQL発行回数や制約を意識する入口になる

---

## 今月追加した代表ノート

| 分野 | ノート |
|------|--------|
| HTTP / JS | [[note-insight-http-request]], [[note-insight-fetch-api]], [[note-insight-request-method-alias]], [[note-insight-jsonplaceholder]] |
| ループ | [[note-insight-for-loop]], [[note-insight-increment-expression]], [[note-insight-infinite-loop]] |
| Stimulus | [[note-insight-stimulus-connect-callback]], [[note-insight-stimulus-targets]], [[note-insight-stimulus-values]] |
| Rails管理 | [[note-insight-boolean-default-false-null-false]], [[note-insight-trait-admin]], [[note-insight-db-seed]] |
| Rails安全性 | [[note-insight-turbo-stream-accept-header]], [[note-insight-rescue]], [[note-insight-idor]], [[note-insight-destroy-vs-destroy-bang]] |
| Cookie / Session | [[note-insight-cookie]], [[note-insight-cookie-httponly]], [[note-insight-cookie-secure]], [[note-insight-session]], [[note-insight-session-id]] |
| Webセキュリティ | [[note-insight-https]], [[note-insight-tls-current-encryption-protocol]], [[note-insight-ssl-legacy-encryption-protocol]], [[note-insight-two-factor-authentication]] |
| サイバー攻撃 | [[note-insight-xss]], [[note-insight-session-hijacking]], [[note-insight-phishing]], [[note-insight-ddos-attack]], [[note-insight-man-in-the-middle-attack]] |
| Active Record / DB | [[note-insight-n-plus-one]], [[note-insight-activerecord-includes]], [[note-insight-activerecord-preload]], [[note-insight-database]], [[note-insight-sql]] |
| データベース基礎 | [[note-insight-dbms]], [[note-insight-database-table]], [[note-insight-database-constraint]], [[note-insight-database-transaction]], [[note-insight-database-index]] |
| コンピュータ構成 | [[note-insight-cpu]], [[note-insight-fetch-decode-execute]], [[note-insight-main-memory]], [[note-insight-storage-device]], [[note-insight-bus]] |
| Rails周辺・基礎用語 | [[note-insight-function-method-argument-basics]], [[note-insight-object-oriented-programming]], [[note-insight-homebrew]] |
| Kaminari | [[note-insight-kaminari-paginator-partial-role]], [[note-insight-kaminari-page-navigation-partials]], [[note-insight-kaminari-gap-and-render]] |

---

## 未決事項（Open Questions）

| 項目 | 関連MOC |
|------|---------|
| Fetch API と Axios の実務での使い分けを言語化したい | [[map-http-client-basics]] |
| `forEach` や `map` と `for` の使い分けも整理したい | [[map-javascript-loop-basics]] |
| Stimulus の `values` と `dataset` の使い分けを整理したい | [[map-stimulus-basics]] |
| seed を冪等に保つ判断基準を自分の言葉でまとめたい | [[map-rails-admin-and-seed-basics]] |
| IDOR 対策を controller 規約として整理したい | [[map-rails-controller-safety-and-turbo]] |
| Cookie属性の `HttpOnly` / `Secure` / `SameSite` を実例で使い分けたい | [[map-cookie-basics]] |
| SSL / TLS / SSL証明書の呼び方と実体を整理したい | [[map-web-security-basics]] |
| N+1対策で `includes` / `preload` / `eager_load` をどう選ぶか整理したい | [[map-activerecord-query-basics]] |
| DB制約とRailsバリデーションの役割分担を整理したい | [[map-database-fundamentals]] |
| Kaminariのカスタムビューの責務分担を整理したい | [[map-kaminari-pagination-basics]] |
| `#要復習` が付いた4月ノートを優先順位つきで復習したい | [[map-2026-04-learning]] |

---

## 運用ルール

- knowledge-base 全体の運用ルールは [[knowledge-base-doc-index]] に集約する

---

## 関連リンク

- [[2026-04-07_insight_knowledge-base.md]]
- [[knowledge-base-doc-index]]
- [[map-http-client-basics]]
- [[map-javascript-loop-basics]]
- [[map-stimulus-basics]]
- [[map-rails-admin-and-seed-basics]]
- [[map-rails-controller-safety-and-turbo]]
- [[map-cookie-basics]]
- [[map-session-basics]]
- [[map-web-security-basics]]
- [[map-cyber-attack-basics]]
- [[map-activerecord-query-basics]]
- [[map-database-fundamentals]]
- [[map-computer-architecture-basics]]
- [[map-ruby-rails-predicate-basics]]
- [[map-kaminari-pagination-basics]]
- [[map-rails-basics]]
