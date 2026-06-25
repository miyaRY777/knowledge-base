---
id: note-insight-invariant
title: "不変条件はシステムの処理の前後で常に守られているべき条件"
created: 2026-04-07
source: [[2026-04-07_insight_rails-ruby-terms.md]]
quiz_fail_log: []
---

## Summary
- invariant は常に守られているべき条件やルールです。
- Rails 固有の機能名ではなく、設計やレビューで使う言葉です。
- 例として「1つの部屋に共有リンクは1つだけ」があります。

## Tags
#design #domain-model #invariant

## Links

## Body
`invariant` は、プログラムの途中でも壊れてはいけない前提やルールを指します。Rails の機能名ではなく、設計やレビューで「この条件は常に成り立つべき」と表現するときに使う言葉です。

たとえば「1つの部屋に共有リンクは1つだけ」のようなルールは invariant の例です。こうした条件は、バリデーションや DB 制約などで守る対象になります。

## Example
たとえば「1つの部屋に共有リンクは1つだけ」のようなルールが invariant の具体例です。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] アプリ内で守るべき invariant を具体例で洗い出す
