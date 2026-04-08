# 2026年4月学習マップ

> **このMOCで分かること**: 2026年4月に学んだ内容の全体像、テーマ別の入口、今月の重要ポイント

---

## 今月のサマリー

| 項目 | 内容 |
|------|------|
| 期間 | 2026-04 |
| 主なテーマ | HTTP / Axios / JavaScriptループ / Rails管理者とseed / Turboと認可 |
| 入口ノート | [[2026-04-07_insight_knowledge-base.md]] |
| 既存基礎マップ | [[map-rails-basics]] |

---

## テーマ別マップ

| # | テーマ | 概要 | MOC |
|---|--------|------|-----|
| 1 | HTTPクライアント基礎 | Axios、Fetch、Promise、HTTPメソッド、通信設定 | [[map-http-client-basics]] |
| 2 | JavaScriptループ基礎 | `for`、初期化、増減式、無限ループ、配列処理 | [[map-javascript-loop-basics]] |
| 3 | Rails管理者・seed基礎 | boolean、trait、admin判定、seed、DB準備 | [[map-rails-admin-and-seed-basics]] |
| 4 | Railsコントローラ安全性とTurbo | Turbo Stream、例外処理、認可、IDOR、Relation | [[map-rails-controller-safety-and-turbo]] |
| 5 | Rails基礎 | 3月末からの既存知識の土台 | [[map-rails-basics]] |

---

## 今月の重要概念

[[note-insight-http-request]]
[[note-insight-promise]]
[[note-insight-axios-instance]]
[[note-insight-current-user-admin]]
[[note-insight-idor]]
[[note-insight-active-record-relation]]

**ポイント**:
- JavaScript 側では「通信の基本」と「非同期処理」の理解が土台
- Rails 側では「権限」「例外」「安全な取得」の理解が重要
- Turbo 対応では request 形式ごとの振る舞い分岐を意識する

---

## 今月追加した代表ノート

| 分野 | ノート |
|------|--------|
| HTTP / JS | [[note-insight-http-request]], [[note-insight-fetch-api]], [[note-insight-request-method-alias]], [[note-insight-jsonplaceholder]] |
| ループ | [[note-insight-for-loop]], [[note-insight-increment-expression]], [[note-insight-infinite-loop]] |
| Rails管理 | [[note-insight-boolean-default-false-null-false]], [[note-insight-trait-admin]], [[note-insight-db-seed]] |
| Rails安全性 | [[note-insight-turbo-stream-accept-header]], [[note-insight-rescue]], [[note-insight-idor]], [[note-insight-destroy-vs-destroy-bang]] |

---

## 未決事項（Open Questions）

| 項目 | 関連MOC |
|------|---------|
| Fetch API と Axios の実務での使い分けを言語化したい | [[map-http-client-basics]] |
| `forEach` や `map` と `for` の使い分けも整理したい | [[map-javascript-loop-basics]] |
| seed を冪等に保つ判断基準を自分の言葉でまとめたい | [[map-rails-admin-and-seed-basics]] |
| IDOR 対策を controller 規約として整理したい | [[map-rails-controller-safety-and-turbo]] |

---

## 運用ルール

- knowledge-base 全体の運用ルールは [[knowledge-base-operations]] に集約する

---

## 関連リンク

- [[2026-04-07_insight_knowledge-base.md]]
- [[knowledge-base-operations]]
- [[map-http-client-basics]]
- [[map-javascript-loop-basics]]
- [[map-rails-admin-and-seed-basics]]
- [[map-rails-controller-safety-and-turbo]]
- [[map-rails-basics]]
