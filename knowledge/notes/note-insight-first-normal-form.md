---
id: note-insight-first-normal-form
title: 第一正規形は1つのカラムに1つの値だけを持たせる形
created: 2026-05-19
source: [[2026-05-19_insight_database-normalization.md]]
review_streak: 0
last_reviewed_on: 2026-05-22
quiz_fail_log: []
---

## Summary
- 第一正規形は、1つのカラムに複数の値をまとめて入れない状態です。
- カンマ区切りや配列のような保存を避けると、検索や更新を行いやすくなります。
- 複数値を扱う場合は、行や関連テーブルに分けて表現します。

## Tags
#database #sql #normalization #1nf #database-design

## Links
- [[note-insight-database-normalization]]
- [[note-insight-database-column]]
- [[note-insight-database-table]]

## Body
第一正規形は、各カラムの値をそれ以上分解しなくてよい単位にする基本ルールです。たとえば `hobbies` カラムに `game,movie,music` のような文字列を入れると、特定の趣味で検索したり、1つだけ削除したりする処理が面倒になります。

複数の値を持つ情報は、1セルに押し込むのではなく、行を分けるか、別テーブルとして切り出します。こうすると、SQL の検索・集計・更新をデータベースらしい形で扱いやすくなります。

## Example
```sql
-- 1つのセルに複数値を詰めるのではなく
-- user_hobbies のようなテーブルで1行1値にする
user_id | hobby
--------|-------
1       | game
1       | movie
1       | music
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
