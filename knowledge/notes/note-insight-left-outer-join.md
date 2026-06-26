---
id: note-insight-left-outer-join
title: "`LEFT OUTER JOIN` は左側の行を残して右側を結び付ける"
created: 2026-04-26
source: [[2026-04-26_insight_active-record-loading-and-joins.md]]
quiz_fail_log: []
---

## Summary
- `LEFT OUTER JOIN` は左側テーブルの行を必ず残す JOIN。
- 右側に一致がなければ右側の列は `NULL` になる。
- 関連がなくても親データを取得したいときに使いやすい。

## Tags
#sql #postgresql #join #rails

## Links
- [[note-insight-activerecord-eager-load]]
- [[note-insight-activerecord-includes]]

## Body
`LEFT OUTER JOIN` は、左側のテーブルを基準にして行を必ず結果へ残しつつ、右側で一致する行があれば結び付ける JOIN です。右側に一致するデータがない場合でも左側の行は消えず、右側の列だけが `NULL` になります。そのため、関連データが存在しない親も含めて一覧を取りたい場面でよく使われます。Rails では `eager_load` や一部の `includes` の内部でも使われます。

## Example
```sql
SELECT users.*, posts.*
FROM users
LEFT OUTER JOIN posts
  ON posts.user_id = users.id;
```

このコードでは、投稿がないユーザーも残したまま、投稿情報を結び付けています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
