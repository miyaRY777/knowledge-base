---
id: note-insight-destroy-vs-destroy-bang
title: destroy! と destroy の違いの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **失敗時に例外を出すかどうかの違い**
- `destroy` は失敗しても false を返します。
- `destroy!` は失敗すると例外を発生させます。

## Tags
#insight

## Links
- [[関連ノート]]

## Body
**失敗時に例外を出すかどうかの違い**

**解説：**
`destroy` は失敗しても false を返します。
`destroy!` は失敗すると例外を発生させます。

```ruby
user.destroy!
```

このコードでは、削除に失敗したときに例外を発生させるために destroy! を使っています。
