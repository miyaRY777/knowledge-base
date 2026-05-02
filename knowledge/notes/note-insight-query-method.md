---
id: note-insight-query-method
title: "クエリメソッドの要点"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **「〜か？」を確認するためのメソッド**
- Rubyでは、名前の最後に `?` が付くメソッドは、状態や条件をたずねるためのメソッドとして使うのが慣習です。
- たとえば `empty?` や `nil?` は、「空ですか？」「nilですか？」を確認します。

## Tags
#ruby #insight

## Links
- [[note-insight-current-user-admin]]

## Body
**「〜か？」を確認するためのメソッド**

**解説：**
Rubyでは、名前の最後に `?` が付くメソッドは、状態や条件をたずねるためのメソッドとして使うのが慣習です。
たとえば `empty?` や `nil?` は、「空ですか？」「nilですか？」を確認します。
Rubyの公式ドキュメントでも、`?` で終わるメソッドは慣習として真偽値を返すものと説明されています。 ([Ruby言語ドキュメント](https://docs.ruby-lang.org/en/3.0/syntax/methods_rdoc.html "methods - RDoc Documentation"))

## Example

```ruby
fruits = []

puts fruits.empty?
```

このコードでは、配列が空かどうかを確認するために `クエリメソッド` を使っています。
