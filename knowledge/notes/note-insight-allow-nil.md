---
id: note-insight-allow-nil
title: "allow_nilはnilのときにバリデーションをスキップする指定"
created: 2026-04-07
source: [[2026-04-07_insight_rails-ruby-terms.md]]
quiz_fail_log: []
---

## Summary
- `allow_nil` は値が `nil` のときにバリデーションをスキップする指定です。
- 未入力は許可しつつ、入力されたときだけ検証したい場合に使います。
- 空文字 `""` とは扱いが異なることがあります。

## Tags
#rails #validation #model

## Links
- [[note-insight-inclusion-validation]]

## Body
`allow_nil` は、値が `nil` ならそのバリデーションを実行しないようにする指定です。未入力は許可しつつ、値が入ったときだけ内容をチェックしたい場面で使います。

ただし、`nil` と空文字は同じではありません。`allow_nil` は `nil` を対象にした指定なので、空文字 `""` をどう扱うかは別途確認が必要です。

## Example
```ruby
validates :expires_in, inclusion: { in: %w[1h 24h 3d 7d] }, allow_nil: true
```

このコードでは、`expires_in` が `nil` のときは通しつつ、値が入っているときだけ候補の中に含まれているか確認しています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
