---
id: note-insight-ruby-constants
title: "Rubyの定数は先頭大文字の名前で変更しない前提の値を表す"
created: 2026-04-07
source: [[2026-04-07_insight_rails-ruby-terms.md]]
quiz_fail_log: []
---

## Summary
- Ruby の定数は、変更しない前提で名前をつけて持たせる値です。
- 先頭が大文字の名前は定数として扱われます。
- 絶対に変更できない値ではなく、変更しない前提の名前として使います。

## Tags
#ruby #language #design

## Links

## Body
Ruby では、先頭が大文字の名前は定数として扱われます。`EXPIRES_IN_MAP` のような名前は定数です。

ただし、Ruby の定数は完全に不変な値という意味ではなく、変更しない前提で扱う名前です。設定値や対応表のように、コード中で繰り返し使う値をまとめるときに向いています。

## Example
```ruby
EXPIRES_IN_MAP = {
  "1h" => 1.hour,
  "24h" => 24.hours,
  "3d" => 3.days
}.freeze
```

このコードでは、有効期限の対応表を、変更しない前提の値として定数にまとめています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
