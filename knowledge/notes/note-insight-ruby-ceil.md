---
id: note-insight-ruby-ceil
title: "Rubyのceilメソッドは数値を指定桁数で切り上げる"
created: 2026-06-23
source: [[2026-06-23_insight_ruby-rounding-methods.md]]
quiz_fail_log: []
---

## Summary
- `ceil` は数値を上方向に丸めるメソッドです。
- 引数で小数点以下の桁数を指定できます。
- 引数なしの場合は整数に切り上げられます。

## Tags
#ruby #numeric #method

## Links
- [[note-insight-ruby-round]]
- [[note-insight-ruby-floor]]

## Body
`ceil` は、数値を指定した桁数で切り上げるメソッドです。「自分自身以上の最小の数」を返します。引数に整数を渡すと、小数点以下その桁数に切り上げます。引数を省略すると整数に切り上げられます。

## Example
```ruby
num = 100.3333
puts num.ceil(1)
# => 100.4
```


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
