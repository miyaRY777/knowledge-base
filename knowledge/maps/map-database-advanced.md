# データベース詳細マップ（ACID・正規化・ER・ロック・インデックス）

> **このMOCで分かること**: ACIDプロパティ・ER図・正規化・インデックス種別・ロック種別など、DB設計と運用の深い部分を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | ACIDプロパティ | トランザクションが満たすべき4つの性質 | [[note-insight-acid-properties]] |
| 2 | 原子性（Atomicity） | トランザクションは全部成功か全部失敗か | [[note-insight-atomicity]] |
| 3 | 一貫性（Consistency） | トランザクション後もデータが整合状態を保つ | [[note-insight-consistency]] |
| 4 | 独立性（Isolation） | トランザクション同士が互いに干渉しない | [[note-insight-isolation]] |
| 5 | 永続性（Durability） | コミットされたデータは失われない | [[note-insight-durability]] |
| 6 | エンティティ | DBで管理する対象（モノや概念） | [[note-insight-entity]] |
| 7 | エンティティの属性 | エンティティが持つ特徴・情報 | [[note-insight-entity-attribute]] |
| 8 | エンティティのリレーション | エンティティ間のつながり | [[note-insight-entity-relationship]] |
| 9 | ER図 | エンティティとリレーションを可視化する図 | [[note-insight-er-diagram]] |
| 10 | データベース正規化 | データの重複・矛盾を減らす設計手法 | [[note-insight-database-normalization]] |
| 11 | 第1正規形 | 繰り返しグループを排除する | [[note-insight-first-normal-form]] |
| 12 | 第2正規形 | 部分関数従属を排除する | [[note-insight-second-normal-form]] |
| 13 | 第3正規形 | 推移関数従属を排除する | [[note-insight-third-normal-form]] |
| 14 | 主キー | レコードを一意に識別するカラム | [[note-insight-primary-key]] |
| 15 | 外部キー | 別テーブルの主キーを参照するカラム | [[note-insight-foreign-key]] |
| 16 | DBキーの種類 | 主キー・外部キー・候補キーなどの総称 | [[note-insight-database-key]] |
| 17 | NULL値 | 値が存在しないことを表す特殊な状態 | [[note-insight-null-value]] |
| 18 | インデックスの種類 | B-tree・Hash・全文などの種別 | [[note-insight-database-index-types]] |
| 19 | B-treeインデックス | 範囲検索に強い最も一般的なインデックス | [[note-insight-b-tree-index]] |
| 20 | ハッシュインデックス | 完全一致検索に特化したインデックス | [[note-insight-hash-index]] |
| 21 | 全文インデックス | 文章の内容で検索するためのインデックス | [[note-insight-full-text-index]] |
| 22 | ロックの種類 | 共有ロック・排他ロックの違い | [[note-insight-database-lock-types]] |
| 23 | 排他ロック | 書き込み中に他の読み書きをブロックするロック | [[note-insight-exclusive-lock]] |
| 24 | 共有ロック | 読み取り中に他の読み取りは許可するロック | [[note-insight-shared-lock]] |
| 25 | DBサーバー | データベースを管理・提供するサーバー | [[note-insight-database-server]] |
| 26 | 分散データベース | データを複数サーバーに分散して管理するDB | [[note-insight-distributed-database]] |
| 27 | 集中管理型データベース | データを1カ所に集めて管理するDB | [[note-insight-centralized-data-management]] |

---

## トランザクションとACID

[[note-insight-acid-properties]]
[[note-insight-atomicity]]
[[note-insight-consistency]]
[[note-insight-isolation]]
[[note-insight-durability]]

**ポイント**:
- ACID は「信頼できるDB操作」の4つの要件の頭文字
- 原子性：途中で失敗したらロールバック。全部か無かの原則
- 一貫性：制約やルールを満たした状態が維持される
- 独立性：並行トランザクションが互いの中間状態を見ない
- 永続性：コミット後はクラッシュしても消えない

---

## ER図と設計の基礎

[[note-insight-entity]]
[[note-insight-entity-attribute]]
[[note-insight-entity-relationship]]
[[note-insight-er-diagram]]
[[note-insight-primary-key]]
[[note-insight-foreign-key]]
[[note-insight-database-key]]
[[note-insight-null-value]]

**ポイント**:
- エンティティ＝テーブルの元になる「モノ」。属性がカラムになる
- ER図はエンティティ間の関係（1対多など）を可視化する設計ツール
- 主キーはレコードを一意に特定する。外部キーは別テーブルへの参照
- NULL値は「値がない」状態。比較・集計で特殊な扱いが必要

---

## 正規化

[[note-insight-database-normalization]]
[[note-insight-first-normal-form]]
[[note-insight-second-normal-form]]
[[note-insight-third-normal-form]]

**ポイント**:
- 正規化は重複・更新異常を防ぐためにテーブルを整理する作業
- 第1正規形：繰り返しグループを排除し、1セルに1値
- 第2正規形：複合主キーがある場合の部分依存を排除
- 第3正規形：非キー列同士の推移依存を排除
- 正規化しすぎると JOIN が増える。パフォーマンスとのトレードオフ

---

## インデックス

[[note-insight-database-index-types]]
[[note-insight-b-tree-index]]
[[note-insight-hash-index]]
[[note-insight-full-text-index]]

**ポイント**:
- B-treeは汎用。範囲検索・ソートに強く、ほとんどのDBのデフォルト
- Hashは完全一致のみ。範囲検索には使えない
- 全文インデックスは文章の単語単位での検索向け

---

## ロック

[[note-insight-database-lock-types]]
[[note-insight-exclusive-lock]]
[[note-insight-shared-lock]]

**ポイント**:
- 共有ロック（読み取りロック）：複数の読み取りは同時OK。書き込みはブロック
- 排他ロック（書き込みロック）：書き込み中は読み書き両方をブロック
- デッドロックはロックの取得順序が逆になると発生する

---

## 構成と分散

[[note-insight-database-server]]
[[note-insight-distributed-database]]
[[note-insight-centralized-data-management]]

**ポイント**:
- 集中管理型はシンプルだが単一障害点になりやすい
- 分散DBはスケールしやすいが整合性・設計が複雑になる

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| デッドロックの具体的な発生パターンを整理する | - | - | [[note-insight-exclusive-lock]] |
| CAP定理と分散DBの関係を整理する | - | - | [[note-insight-distributed-database]] |
| 第4正規形以降が必要なケースをまとめる | - | - | [[note-insight-third-normal-form]] |

---

## 関連リンク

- [[map-database-fundamentals]]
- [[map-rails-basics]]
- [[map-activerecord-query-basics]]
