---
id: note-insight-soft-delete
title: "論理削除はDBから消さずに削除済みとして扱う方法"
created: 2026-05-02
source: [[2026-05-02_insight_samesite-csrf-soft-delete.md]]
quiz_fail_log: []
---

## Summary
- 論理削除は、レコードをDBに残したまま削除済みとして扱う方法です。
- `deleted_at` や `discarded_at` のようなカラムで削除状態を表すことがあります。
- 復元や履歴保持に向きますが、検索条件や一意性制約の設計に注意が必要です。

## Tags
#rails #database #soft-delete #activerecord

## Links
- [[note-insight-soft-delete-flag]]
- [[note-insight-destroy-vs-destroy-bang]]
- [[note-insight-active-record-callbacks]]
- [[note-insight-database-record]]

## Body
論理削除は、レコードを物理的に削除せず、アプリ上では削除済みとして扱う方法です。`deleted_at` や `discarded_at` のようなカラムに時刻を入れ、「この時刻に削除された」と判断する形がよく使われます。

物理削除と違ってデータが残るため、復元したい場合や履歴として保持したい場合に向いています。一方で、通常の一覧や検索から削除済みデータを除外する必要があります。また、削除済みレコードが残ることで、一意性制約や集計の扱いを考える必要が出ることもあります。

Rails 標準に「論理削除」という専用機能があるわけではないため、自分で実装するか、`discard` のような gem を使ってスコープや復元処理を整理します。

## Example
```ruby
user.update(deleted_at: Time.current)
```

このコードでは、ユーザーのレコードをDBから消さずに、削除された時刻を保存しています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
