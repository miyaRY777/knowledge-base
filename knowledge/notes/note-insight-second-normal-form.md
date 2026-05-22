---
id: note-insight-second-normal-form
title: 第二正規形は複合主キーの一部だけで決まる情報を分離する形
created: 2026-05-19
source: [[2026-05-19_insight_database-normalization.md]]
review_streak: 0
last_reviewed_on: 2026-05-22
---

## Summary
- 第二正規形は、第一正規形を満たした上で部分関数従属を取り除く形です。
- 複合主キーの一部だけで決まるカラムは、別テーブルに分けます。
- 同じ情報の繰り返しを減らし、更新漏れを起こしにくくします。

## Tags
#database #sql #normalization #2nf #database-design #primary-key #要復習

## Links
- [[note-insight-database-normalization]]
- [[note-insight-first-normal-form]]
- [[note-insight-primary-key]]
- [[note-insight-database-key]]

## Body
第二正規形は、複合主キーを使うテーブルで特に意識する正規化です。複合主キー全体ではなく、その一部だけで決まる情報が同じテーブルにあると、同じ値を何度も保存することになります。

たとえば `student_id` と `subject_id` の組み合わせで成績を表すテーブルに `student_name` も入れると、同じ学生名が科目ごとに繰り返されます。学生名は `student_id` だけで決まるため、学生テーブルへ分けるほうが自然です。

## Example
```sql
students
student_id | student_name
-----------|-------------
1          | Tanaka

scores
student_id | subject_id
-----------|-----------
1          | 101
1          | 102
```
