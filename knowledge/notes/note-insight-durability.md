---
id: note-insight-durability
title: Durabilityは成功したトランザクションの結果を保存し続ける性質
created: 2026-05-20
source: [[2026-05-20_insight_acid-properties.md]]
---

## Summary
- Durability は、トランザクション成功後の変更が失われないようにする性質です。
- COMMIT された結果は、アプリの再起動後もデータベースに残る前提で扱います。
- 保存成功後のデータを信頼できる状態にするための性質です。

## Tags
#database #sql #transaction #acid #durability

## Links
- [[note-insight-acid-properties]]
- [[note-insight-database-transaction]]
- [[note-insight-database-commit-rollback]]
- [[note-insight-database-backup-and-recovery]]

## Body
Durability は、トランザクションが成功して確定した結果が、その後もデータベースに残り続ける性質です。保存が成功したのにアプリケーションを再起動したら変更が消えるようでは、データベースの更新結果を信頼できません。

この性質によって、COMMIT 済みの変更は永続化されたものとして扱えます。実際のデータベースでは、障害に備えたログや復旧の仕組みなども、この考え方を支えます。

## Example
```ruby
user.update!(name: "新しい名前")
```

この更新が成功したあと、ユーザー名はデータベース上の状態として残る前提で扱います。
