---
id: note-insight-rails-db-prepare
title: bin/rails db:prepareの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **データベースを「使える状態」にまとめて整えるコマンドのこと**
- `db:prepare` は、データベースが無ければ作成し、マイグレーションを実行し、必要に応じて seed も実行するコマンドです。
- 開発環境やテスト環境を一発で整えるために使います。

## Tags
#rails #database

## Links
- [[関連ノート]]

## Body
**データベースを「使える状態」にまとめて整えるコマンドのこと**

**解説：**
`db:prepare` は、データベースが無ければ作成し、マイグレーションを実行し、必要に応じて seed も実行するコマンドです。
開発環境やテスト環境を一発で整えるために使います。
既にDBがある場合はマイグレーションのみ実行されます。

具体例：

```
bin/rails db:prepare
```

このコードでは、データベースを作成・更新して、アプリがすぐ使える状態にするために db:prepare を使っています。
