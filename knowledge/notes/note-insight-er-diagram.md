---
id: note-insight-er-diagram
title: ER図はデータベースの全体像を関係で表す図
created: 2026-05-18
source: [[2026-05-18_insight_er-diagram-basics]]
---

## Summary
- ER図は、データベースの全体像をエンティティ同士の関係で表す図です。
- 管理したいデータと、そのつながりをテーブル設計前に整理できます。
- エンティティ、属性、リレーションを使って設計の見通しをよくします。

## Tags
#database #database-design #er-diagram

## Links
- [[note-insight-entity]]
- [[note-insight-entity-attribute]]
- [[note-insight-entity-relationship]]
- [[note-insight-database-table]]

## Body
ER図は、データベースでどのような対象を管理し、それらがどう関係するかを図にしたものです。テーブルやカラムを実装する前に全体像を整理できるため、必要なデータや関連の抜け漏れを見つけやすくなります。

たとえば、`User` が複数の `Post` を持ち、`Post` が1人の `User` に属するという関係を図で表すと、設計の意図を共有しやすくなります。

## Example
- `User` と `Post` をエンティティとして置く
- `User` が複数の `Post` を持つ関係を線で結ぶ
- 属性として `User.name` や `Post.title` を整理する

## Action
- [ ] 多重度の表し方を整理する
