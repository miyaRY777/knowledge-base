---
id: note-insight-database-index-types
title: データベースインデックスは検索目的に合わせて種類を選ぶ
created: 2026-05-21
source: [[2026-05-21_insight_database-index-types.md]]
review_streak: 0
last_reviewed_on: 2026-05-22
---

## Summary
- インデックスには、B-tree、ハッシュ、全文検索など用途の違う種類があります。
- 条件検索、範囲検索、並び替え、文章検索のどれを速くしたいかで向き不向きが変わります。
- DBMS やストレージエンジンによって使える種類や挙動が異なるため、実際の仕様確認が必要です。

## Tags
#database #sql #index #performance #database-design #要復習

## Links
- [[note-insight-database-index]]
- [[note-insight-b-tree-index]]
- [[note-insight-hash-index]]
- [[note-insight-full-text-index]]

## Body
データベースインデックスは、すべて同じ仕組みで検索を速くするわけではありません。よく使われる B-tree インデックスは範囲検索や並び替えにも向き、ハッシュインデックスは完全一致検索に向きます。全文検索インデックスは、文章の中から単語やキーワードを探す用途に向いています。

どのインデックスが有効かは、検索条件や `ORDER BY` の有無、対象カラムの性質、DBMS の実装によって変わります。インデックスを追加すると書き込み時の更新コストも増えるため、クエリの目的に合う種類を選ぶことが大切です。

## Example
- メールアドレスの完全一致検索には B-tree やハッシュを検討する
- 日付や価格の範囲検索には B-tree を検討する
- 記事本文のキーワード検索には全文検索用のインデックスを検討する
