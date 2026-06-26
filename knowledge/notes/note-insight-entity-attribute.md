---
id: note-insight-entity-attribute
title: 属性はエンティティが持つデータ項目
created: 2026-05-18
source: [[2026-05-18_insight_er-diagram-basics]]
review_streak: 0
last_reviewed_on: 2026-05-22
quiz_fail_log: []
---

## Summary
- 属性は、エンティティが持つ具体的なデータ項目です。
- `User` の `name` や `email` のように、対象の特徴を表します。
- Rails では、実装段階でテーブルのカラムになることが多いです。

## Tags
#database #database-design #entity #attribute

## Links
- [[note-insight-er-diagram]]
- [[note-insight-entity]]
- [[note-insight-database-column]]

## Body
属性は、エンティティに含まれる個々の情報です。`User` という対象を考えたときの `name` や `email`、`Post` の `title` や `body` のように、その対象がどんな情報を持つかを整理します。

設計段階では属性として考え、実装段階では多くの場合テーブルのカラムとして表れます。属性とカラムをつなげて理解すると、設計から実装への移り変わりが見えやすくなります。

## Example
- `User`: `name`, `email`, `password_digest`
- `Post`: `title`, `body`, `user_id`
- `Comment`: `body`, `user_id`, `post_id`


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
