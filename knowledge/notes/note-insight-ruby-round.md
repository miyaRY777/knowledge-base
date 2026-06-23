---
id: note-insight-ruby-round
title: "Rubyのroundメソッドは数値を指定桁数で四捨五入する"
created: 2026-06-23
source: [[2026-06-23_insight_ruby-rounding-methods.md]]
quiz_fail_log: []
---

## Summary
- `round` は数値を近い値に丸めるメソッドです。
- 引数で小数点以下の桁数を指定できます。
- 引数なしの場合は整数に四捨五入されます。

## Tags
#ruby #numeric #method

## Links
- [[note-insight-ruby-ceil]]
- [[note-insight-ruby-floor]]

## Body
`round` は、数値を指定した桁数で四捨五入するメソッドです。引数に整数を渡すと、小数点以下その桁数に丸めます。引数を省略すると整数に四捨五入されます。

## Example
```ruby
num = 100.3383
puts num.round(2)
# => 100.34
```

## Action
