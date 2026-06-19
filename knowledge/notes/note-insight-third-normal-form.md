---
id: note-insight-third-normal-form
title: 第三正規形は主キー以外のカラム同士の依存を分離する形
created: 2026-05-19
source: [[2026-05-19_insight_database-normalization.md]]
review_streak: 0
last_reviewed_on: 2026-05-22
quiz_fail_log: []
---

## Summary
- 第三正規形は、第二正規形を満たした上で推移的な依存を取り除く形です。
- 主キーではないカラムから別のカラムが決まる場合、その組み合わせを別テーブルに分けます。
- マスターデータを切り出すことで、名前変更などの更新を一か所に集めやすくなります。

## Tags
#database #sql #normalization #3nf #database-design

## Links
- [[note-insight-database-normalization]]
- [[note-insight-second-normal-form]]
- [[note-insight-foreign-key]]
- [[note-insight-centralized-data-management]]

## Body
第三正規形は、主キーではないカラム同士の依存をテーブルから取り除く考え方です。ある行の主キーではなく、別の通常カラムによって決まる情報を一緒に持つと、同じ対応関係が複数行に繰り返されます。

たとえば `users` に `prefecture_code` と `prefecture_name` の両方を持たせると、都道府県コードから都道府県名が決まる関係をユーザー行ごとに重複して保存することになります。この場合は都道府県マスタを作り、ユーザー側にはコードだけを持たせると更新箇所を集約できます。

## Example
```sql
prefectures
prefecture_code | prefecture_name
----------------|----------------
13              | Tokyo
27              | Osaka

users
user_id | prefecture_code
--------|----------------
1       | 13
2       | 27
```
