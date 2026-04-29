# ActiveRecord / DBクエリ基礎マップ

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | データベース | アプリのデータを保存・管理して取り出す場所 | [[note-insight-database]] |
| 2 | ActiveRecord::Relation | クエリ条件を保持し、必要になるまで実行を遅らせるオブジェクト | [[note-insight-active-record-relation]] |
| 3 | where.not | 条件に一致しないレコードを取得する検索方法 | [[note-insight-where-not]] |
| 4 | N+1 | 関連データ取得でSQLが増えすぎる問題 | [[note-insight-n-plus-one]] |
| 5 | includes | 状況に応じて関連の読み込み方法を切り替える | [[note-insight-activerecord-includes]] |
| 6 | preload | 関連データを別クエリで先に読み込む | [[note-insight-activerecord-preload]] |
| 7 | eager_load | 関連データを LEFT OUTER JOIN でまとめて読み込む | [[note-insight-activerecord-eager-load]] |
| 8 | LEFT OUTER JOIN | 左側の行を残して右側テーブルを結び付ける | [[note-insight-left-outer-join]] |

---

## セクション1: DBとActive Recordの基本

[[note-insight-database]]
[[note-insight-active-record-relation]]

**ポイント**:
- データベースは、アプリで使う情報を保存・検索・更新・削除する場所
- Rails では Active Record を通してデータベースを操作することが多い
- `ActiveRecord::Relation` は条件を積み上げ、実際に必要になるまでSQL実行を遅らせる

---

## セクション2: 条件で絞り込む

[[note-insight-where-not]]
[[note-insight-left-outer-join]]

**ポイント**:
- `where.not` は指定条件を除外して検索する
- `LEFT OUTER JOIN` は関連がない行も残したいときに使える
- Rails のクエリメソッドと実際の SQL の関係を意識すると理解しやすい

---

## セクション3: N+1と関連データの先読み

[[note-insight-n-plus-one]]
[[note-insight-activerecord-includes]]
[[note-insight-activerecord-preload]]
[[note-insight-activerecord-eager-load]]

**ポイント**:
- N+1 は一覧取得後に関連データを1件ずつ追加取得してしまう問題
- `preload` は関連ごとに別クエリで先読みする
- `eager_load` は JOIN を使って関連先をまとめて読み込む
- `includes` は状況に応じて読み込み方法が変わるため、生成SQLを確認する意識が必要

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| `includes`、`preload`、`eager_load` の使い分けを実例で比較する | - | - | [[note-insight-n-plus-one]] |
| `joins` と `left_joins` をこのマップに追加するか | - | - | [[note-insight-left-outer-join]] |
| `ActiveRecord::Relation` が実行されるタイミングを実コードで整理する | - | - | [[note-insight-active-record-relation]] |
| DBのテーブル、カラム、レコードの違いを別ノートで整理する | - | - | [[note-insight-database]] |

---

## 関連リンク

- [[map-rails-basics]]
- [[map-rails-admin-and-seed-basics]]
- [[map-rails-controller-safety-and-turbo]]
- [[note-insight-database]]
- [[note-insight-active-record-relation]]
- [[note-insight-where-not]]
- [[note-insight-n-plus-one]]
- [[note-insight-activerecord-includes]]
- [[note-insight-activerecord-preload]]
- [[note-insight-activerecord-eager-load]]
- [[note-insight-left-outer-join]]
