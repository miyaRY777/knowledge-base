# SQL基礎マップ

> **このMOCで分かること**: SQLの基本構文・CRUD操作・制約・JOINまでのデータベース操作の基礎を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | SQL | リレーショナルデータベースを操作する言語 | [[note-insight-sql]] |
| 2 | リレーショナルデータベース | 表形式でデータを管理するデータベース | [[note-insight-relational-database]] |
| 3 | テーブル | 行と列で構成されるデータの格納単位 | [[note-insight-database-table]] |
| 4 | カラム | テーブルの列。データの属性を定義する | [[note-insight-database-column]] |
| 5 | レコード | テーブルの1行。1件のデータ | [[note-insight-database-record]] |
| 6 | CRUD操作 | 作成・読取・更新・削除の基本操作 | [[note-insight-crud-operations]] |
| 7 | SELECT文 | テーブルからデータを取得するSQL | [[note-insight-sql-select]] |
| 8 | WHERE句 | 条件を指定して絞り込むSQL | [[note-insight-sql-where]] |
| 9 | WHERE NOT | 条件を否定して絞り込むSQL | [[note-insight-where-not]] |
| 10 | GROUP BY | 集計処理でデータをグループ化するSQL | [[note-insight-sql-group-by]] |
| 11 | SUM関数 | グループ内の合計値を計算する集計関数 | [[note-insight-sql-sum]] |
| 12 | LEFT OUTER JOIN | 左テーブルを基準に結合するSQL | [[note-insight-left-outer-join]] |
| 13 | プライマリキー | 各レコードを一意に識別するキー | [[note-insight-primary-key]] |
| 14 | 外部キー | 別テーブルのプライマリキーを参照するキー | [[note-insight-foreign-key]] |
| 15 | 外部キー制約 | 参照先に存在しない値を拒否する制約 | [[note-insight-foreign-key-constraint]] |
| 16 | データベースキー | テーブルで使われる各種キーの種類 | [[note-insight-database-key]] |
| 17 | データベース制約 | データの整合性を保つためのルール | [[note-insight-database-constraint]] |
| 18 | NOT NULL制約 | NULLを禁止する制約 | [[note-insight-not-null-constraint]] |
| 19 | UNIQUE制約 | 重複値を禁止する制約 | [[note-insight-unique-constraint]] |
| 20 | UNIQUE制約とNULL | NULL はUNIQUE制約の対象外になる挙動 | [[note-insight-unique-constraint-null]] |
| 21 | データベースクエリ | データを取得・操作するSQL全般 | [[note-insight-database-query]] |

---

## SQLとリレーショナルデータベースの基礎

[[note-insight-sql]]
[[note-insight-relational-database]]
[[note-insight-database-table]]
[[note-insight-database-column]]
[[note-insight-database-record]]

**ポイント**:
- SQLはStructured Query Language。データの取得・追加・更新・削除をすべてSQL文で行う
- リレーショナルDBは表（テーブル）でデータを管理し、テーブル間を関係（リレーション）でつなぐ
- テーブルは列（カラム）と行（レコード）で構成される。1行が1件のデータ

---

## データの取得と絞り込み

[[note-insight-crud-operations]]
[[note-insight-sql-select]]
[[note-insight-sql-where]]
[[note-insight-where-not]]
[[note-insight-database-query]]

**ポイント**:
- `SELECT カラム名 FROM テーブル名` が基本形
- `WHERE 条件` で絞り込む。`WHERE NOT 条件` で否定の絞り込みができる
- CRUD = Create（INSERT）/ Read（SELECT）/ Update（UPDATE）/ Delete（DELETE）

---

## 集計とグループ化

[[note-insight-sql-group-by]]
[[note-insight-sql-sum]]

**ポイント**:
- `GROUP BY カラム名` で同じ値のレコードをまとめて集計できる
- `SUM(カラム名)` でグループ内の合計を計算する。`COUNT`・`AVG`・`MAX`・`MIN` も同様
- `GROUP BY` を使う場合、SELECTに書けるのはGROUP BYのカラムか集計関数のみ

---

## テーブルの結合

[[note-insight-left-outer-join]]

**ポイント**:
- `LEFT OUTER JOIN` は左テーブルの全レコードを残しつつ、右テーブルを結合する
- 右テーブルに対応レコードがない場合はNULLが入る
- INNER JOIN は両方に存在するレコードのみ取得する（交差部分のみ）

---

## キーと制約

[[note-insight-primary-key]]
[[note-insight-foreign-key]]
[[note-insight-foreign-key-constraint]]
[[note-insight-database-key]]
[[note-insight-database-constraint]]
[[note-insight-not-null-constraint]]
[[note-insight-unique-constraint]]
[[note-insight-unique-constraint-null]]

**ポイント**:
- プライマリキー（PK）は各レコードを一意に識別する。NULLは不可、重複不可
- 外部キー（FK）は別テーブルのPKを参照する。参照先に存在しない値を登録しようとするとエラー
- NOT NULL制約: そのカラムへのNULL挿入を禁止する
- UNIQUE制約: 同じ値の重複を禁止する。ただしNULLは複数レコードで許容される（DB依存）

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| INNER JOIN と LEFT JOIN の使い分けを整理する | - | - | - |
| サブクエリの使い方をまとめる | - | - | - |
| インデックスの効果と設計方針をまとめる | - | - | [[note-insight-database-index]] |

---

## 関連リンク

- [[map-database-fundamentals]]
- [[map-database-advanced]]
- [[map-activerecord-query-basics]]
