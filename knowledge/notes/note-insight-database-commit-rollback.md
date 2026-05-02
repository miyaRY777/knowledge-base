---
id: note-insight-database-commit-rollback
title: "COMMITとROLLBACKはトランザクションの確定と取り消し"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- `COMMIT` は、トランザクション中の変更を確定する操作。
- `ROLLBACK` は、トランザクション中の変更を取り消す操作。
- どちらもトランザクションを安全に終えるための重要な命令。

## Tags
#database #sql #transaction #要復習

## Links
- [[note-insight-database-transaction]]
- [[note-insight-data-integrity-and-consistency]]

## Body
`COMMIT` は、トランザクション内で行った変更を正式にデータベースへ反映する操作です。一方で `ROLLBACK` は、途中まで行った変更を破棄して、トランザクション開始前の状態へ戻します。

この2つを理解すると、トランザクションが「まとめて成功」か「まとめて失敗」を実現する仕組みとして見えやすくなります。

<!-- review_log: 2026-05-02 -->
