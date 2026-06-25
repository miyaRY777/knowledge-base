---
id: note-insight-ruby-floor
title: "Rubyのfloorメソッドは数値を指定桁数で切り捨てる"
created: 2026-06-23
source: [[2026-06-23_insight_ruby-rounding-methods.md]]
quiz_fail_log: []
---

## Summary
- `floor` は数値を下方向に丸めるメソッドです。
- 引数で小数点以下の桁数を指定できます。
- 引数なしの場合は整数に切り捨てられます。

## Tags
#ruby #numeric #method

## Links
- [[note-insight-ruby-round]]
- [[note-insight-ruby-ceil]]

## Body
`floor` は、数値を指定した桁数で切り捨てるメソッドです。「自分自身以下の最大の数」を返します。引数に整数を渡すと、小数点以下その桁数に切り捨てます。引数を省略すると整数に切り捨てられます。

## Example
```ruby
num = 100.3383
puts num.floor(3)
# => 100.338
```


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
