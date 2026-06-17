---
id: note-insight-destroy-vs-destroy-bang
title: "destroy!はバリデーション失敗時に例外を出しdestroyはfalseを返す違いがある"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **失敗時に例外を出すかどうかの違い**
- `destroy` は失敗しても false を返します。
- `destroy!` は失敗すると例外を発生させます。

## Tags
#insight

## Links

## Body
`destroy` と `destroy!` の違いは、削除に失敗したときの挙動です。
`destroy` はコールバックで失敗しても `false` を返してアプリを止めませんが、`destroy!` は `ActiveRecord::RecordNotDestroyed` 例外を発生させます。
ユーザー操作で呼ぶ場合はエラーを画面に返したいので `destroy` を使い、スクリプトやシードなど失敗してはいけない処理では `destroy!` を使うのが一般的です。


## Example
```ruby
user.destroy!
```

このコードでは、削除に失敗したときに例外を発生させるために destroy! を使っています。
