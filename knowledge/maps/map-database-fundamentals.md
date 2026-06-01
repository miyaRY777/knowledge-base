# データベース基礎マップ

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | データベース | アプリのデータを保存・管理して取り出す場所 | [[note-insight-database]] |
| 2 | DBMS | データベースを管理・操作するソフトウェア | [[note-insight-dbms]] |
| 2.1 | DBのリアルタイム共有 | 変更をすぐ全員が参照できる仕組み | [[note-insight-database-realtime-sharing]] |
| 3 | リレーショナルデータベース | テーブル同士の関係でデータを管理する仕組み | [[note-insight-relational-database]] |
| 4 | 表計算ソフトとの違い | 規模や整合性の守りやすさが異なる | [[note-insight-spreadsheet-vs-database]] |
| 5 | テーブル | 同じ種類のデータを行と列で保存する場所 | [[note-insight-database-table]] |
| 6 | レコード | テーブルに保存される1件分のデータ | [[note-insight-database-record]] |
| 7 | カラム | テーブルで保存するデータ項目を表す列 | [[note-insight-database-column]] |
| 8 | SQL | データベースを操作するための言語 | [[note-insight-sql]] |
| 9 | クエリ | データベースに対して実行する命令文 | [[note-insight-database-query]] |
| 10 | CRUD | 作成・取得・更新・削除の基本操作 | [[note-insight-crud-operations]] |
| 11 | SELECT | データベースから行を取得するSQL文 | [[note-insight-sql-select]] |
| 12 | WHERE | 条件に合う行だけを絞り込むSQL句 | [[note-insight-sql-where]] |
| 13 | GROUP BY | 同じ値ごとに行をまとめるSQL句 | [[note-insight-sql-group-by]] |
| 14 | SUM | 数値カラムの合計を計算する集計関数 | [[note-insight-sql-sum]] |
| 15 | 整合性と一貫性 | 矛盾のない状態を守る考え方 | [[note-insight-data-integrity-and-consistency]] |
| 16 | 制約 | 不正なデータを保存しないためのルール | [[note-insight-database-constraint]] |
| 17 | NOT NULL制約 | 値が空の保存を防ぐ制約 | [[note-insight-not-null-constraint]] |
| 18 | 一意性制約 | 同じ値の重複保存を防ぐ制約 | [[note-insight-unique-constraint]] |
| 19 | 外部キー制約 | 存在する関連先だけを参照させる制約 | [[note-insight-foreign-key-constraint]] |
| 20 | トランザクション | 複数のデータ操作をひとまとまりで扱う仕組み | [[note-insight-database-transaction]] |
| 21 | COMMIT / ROLLBACK | トランザクションの確定と取り消し | [[note-insight-database-commit-rollback]] |
| 22 | ロック機構 | 同時更新による競合を防ぐ仕組み | [[note-insight-database-locking]] |
| 23 | インデックス | 検索を速くするための目印 | [[note-insight-database-index]] |
| 24 | 権限管理 | 誰がどのデータを操作できるかを制御する仕組み | [[note-insight-database-permission-control]] |
| 25 | バックアップとリカバリ | 障害時にデータを守り復元する仕組み | [[note-insight-database-backup-and-recovery]] |

## セクション1: DBの基本

[[note-insight-database-realtime-sharing]]

- データベースは、アプリが使う情報を後から扱える形で保存する場所。
- DBMS は、データベースへの保存・検索・更新・削除を実際に管理するソフトウェア。
- DBMSはデータをリアルタイムに共有する仕組みを提供し、複数のアプリやユーザーが同時に最新データを参照できる。
- リレーショナルデータベースでは、データをテーブルに分け、必要に応じて関係でつなぐ。
- 表計算ソフトは人が直接編集する小規模管理に向き、データベースは複数ユーザーや複数機能で一貫したデータ管理をしやすい。

## セクション2: テーブル構造

- テーブルは、同じ種類のデータを保存する単位。
- レコードは、テーブルに保存された1件分のデータ。
- カラムは、各レコードが持つ項目を表す。
- Rails のモデル、migration、Active Record を理解するには、テーブル・レコード・カラムの区別が土台になる。

## セクション3: SQLとCRUD

- SQL は、データベースへ命令を出すための言語。
- クエリは、データベースに対する具体的な命令文。
- CRUD は、データの作成・取得・更新・削除という基本操作。
- `SELECT` と `WHERE` は取得と絞り込み、`GROUP BY` と `SUM` は集計でよく使う。

## セクション4: 制約とデータの正しさ

- 整合性と一貫性は、データに矛盾がなく、システム全体で同じルールが守られている状態。
- 制約は、データベース側で不正な値を防ぐためのルール。
- `NOT NULL`、一意性制約、外部キー制約は、保存されるデータの正しさを守る代表的な仕組み。
- Rails のバリデーションだけでなく、DB 制約も併用すると安全性が上がる。

## セクション5: トランザクションと同時実行

- トランザクションは、複数のデータ操作をまとめて成功または失敗として扱う。
- `COMMIT` は変更の確定、`ROLLBACK` は変更の取り消し。
- ロック機構は、同じデータを複数処理が同時に変更するときの競合を防ぐ。
- 注文、在庫、残高、ポイントのように「片方だけ成功」が困る処理では重要になる。

## セクション6: 性能・権限・運用

- インデックスは、よく検索するカラムからデータを探しやすくする。
- 権限管理は、誰がどのデータを見たり変更したりできるかを制御する。
- バックアップとリカバリは、障害や誤操作が起きてもデータを戻せるようにする運用上の仕組み。

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| Rails の Active Record 操作と SQL の対応を、このマップから別マップへどう接続するか | - | - | [[note-insight-sql]] |
| UNIQUE制約とNULLのようなDB固有の挙動を、制約カテゴリに追加整理するか | - | - | [[note-insight-unique-constraint-null]] |
| インデックスのメリットと書き込みコストを具体例で深掘りするか | - | - | [[note-insight-database-index]] |
