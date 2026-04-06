# Rails管理者・seed基礎マップ

> **このMOCで分かること**: 管理者判定、FactoryBot、seed、DB準備まわりの基本をひとつながりで整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | boolean, default: false, null: false | 真偽値カラムで 3 値状態を避ける指定 | [[note-insight-boolean-default-false-null-false]] |
| 2 | trait :admin | FactoryBot で管理者設定を再利用する方法 | [[note-insight-trait-admin]] |
| 3 | current_user.admin? | ログインユーザーが管理者かを判定する書き方 | [[note-insight-current-user-admin]] |
| 4 | クエリメソッド | `?` 付きメソッドで状態を問う Ruby の慣習 | [[note-insight-query-method]] |
| 5 | db:seed | 初期データを投入するコマンド | [[note-insight-db-seed]] |
| 6 | find_or_create_by! | 見つからなければ作るメソッド | [[note-insight-find-or-create-by-bang]] |
| 7 | find_or_initialize_by + update! | 既存更新と新規作成を同じ流れで扱う方法 | [[note-insight-find-or-initialize-by-update-bang]] |
| 8 | bin/rails db:prepare | DB作成とマイグレーションをまとめて整えるコマンド | [[note-insight-rails-db-prepare]] |

---

## セクション1: 管理者権限の前提

[[note-insight-boolean-default-false-null-false]]
[[note-insight-current-user-admin]]
[[note-insight-query-method]]

**ポイント**:
- 管理者フラグは `nil` を防いで 2 値に寄せると扱いやすい
- `admin?` は boolean カラム由来の判定として読める

---

## セクション2: テストでの管理者表現

[[note-insight-trait-admin]]

**ポイント**:
- FactoryBot の trait で管理者ユーザーを短く表現できる
- テストコードの可読性が上がる

---

## セクション3: seed とデータ投入

[[note-insight-db-seed]]
[[note-insight-find-or-create-by-bang]]
[[note-insight-find-or-initialize-by-update-bang]]
[[note-insight-rails-db-prepare]]

**ポイント**:
- seed は何度も実行される前提で重複しにくく書く
- `find_or_create_by!` と `find_or_initialize_by + update!` は用途で使い分ける
- `db:prepare` は環境構築の入口として便利

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| 管理者権限を enum や role テーブルで持つ場合の設計差分は何か | - | - | [[note-insight-current-user-admin]] |
| seed を冪等に保つ実践パターンはどこまで共通化すべきか | - | - | [[note-insight-db-seed]] |
| `find_or_create_by!` と `find_or_initialize_by + update!` の判断基準をどう言語化するか | - | - | [[note-insight-find-or-create-by-bang]] |

---

## 関連リンク

- [[note-insight-boolean-default-false-null-false]]
- [[note-insight-trait-admin]]
- [[note-insight-current-user-admin]]
- [[note-insight-query-method]]
- [[note-insight-db-seed]]
- [[note-insight-find-or-create-by-bang]]
- [[note-insight-find-or-initialize-by-update-bang]]
- [[note-insight-rails-db-prepare]]
