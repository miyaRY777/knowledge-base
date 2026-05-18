---
id: note-insight-entity
title: エンティティはデータベースで管理したい対象や概念
created: 2026-05-18
source: [[2026-05-18_insight_er-diagram-basics]]
---

## Summary
- エンティティは、システムで管理したい対象や概念です。
- `User`、`Post`、`Comment` のように、後でテーブルになる候補を表します。
- ER図では、まずどのエンティティが必要かを洗い出します。

## Tags
#database #database-design #entity

## Links
- [[note-insight-er-diagram]]
- [[note-insight-entity-attribute]]
- [[note-insight-entity-relationship]]
- [[note-insight-database-table]]

## Body
エンティティは、アプリケーションで管理したい重要な対象や概念です。ユーザー、投稿、コメントのように、データとして保存し続けたいものを設計段階で切り出します。

Rails アプリでは、エンティティが後でテーブルやモデルとして実装されることが多いですが、エンティティ自体は実装より前の設計上の考え方です。

## Example
- ユーザーを管理したいので `User` を置く
- 投稿を管理したいので `Post` を置く
- コメントを管理したいので `Comment` を置く

## Action
- [ ] エンティティとテーブルの違いを整理する
