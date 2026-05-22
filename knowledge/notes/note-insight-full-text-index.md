---
id: note-insight-full-text-index
title: 全文検索インデックスは文章中の単語やキーワード検索に向いたインデックス
created: 2026-05-21
source: [[2026-05-21_insight_database-index-types.md]]
review_streak: 0
last_reviewed_on: 2026-05-22
---

## Summary
- 全文検索インデックスは、長い文章から単語やキーワードを探しやすくするためのインデックスです。
- 通常の部分一致検索より、文章検索向けの仕組みを使える場合があります。
- PostgreSQL では GIN や GiST、MySQL では FULLTEXT など、DBMS ごとに仕組みが異なります。

## Tags
#database #sql #index #full-text-search #performance #要復習

## Links
- [[note-insight-database-index-types]]
- [[note-insight-database-index]]
- [[note-insight-sql-where]]

## Body
全文検索インデックスは、記事本文や説明文のような長いテキストから、単語やキーワードを効率よく探すためのインデックスです。`LIKE '%keyword%'` のような検索は単純ですが、大量の文章を対象にすると重くなりやすいため、全文検索用の仕組みが役立ちます。

実装は DBMS によって異なります。PostgreSQL では `to_tsvector` と GIN / GiST インデックスを組み合わせることがあり、MySQL では `FULLTEXT` インデックスを使う場面があります。どの言語や検索方法に対応するかも DBMS の仕様確認が必要です。

## Example
```sql
CREATE INDEX index_articles_on_content
ON articles USING GIN (to_tsvector('simple', content));
```
