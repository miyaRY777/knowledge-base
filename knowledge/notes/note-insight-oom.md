---
id: note-insight-oom
title: "OOMはメモリ不足でプロセスが強制終了される状態"
created: 2026-06-24
source: [[2026-06-24_insight_ruby-memory-and-gc-basics.md]]
quiz_fail_log: []
---

## Summary
- OOM（Out Of Memory）は、使えるメモリが足りなくなった状態です。
- OSや実行環境がメモリを使いすぎたプロセスを強制終了することがあります。
- Railsでは大量データを一括処理するバッチなどで注意が必要です。

## Tags
#memory #os #performance #rails

## Links
- [[note-insight-memory-overuse-risk]]
- [[note-insight-swap]]
- [[note-insight-gc]]

## Body
OOM（Out Of Memory）は、物理メモリもスワップも使い切った状態です。この状態になると、OSのOOMキラーがメモリを大量消費しているプロセスを強制終了します。

Railsアプリでは、大量の画像データやユーザーデータを一度に処理するバッチ処理で発生しやすいです。バッチ処理やサーバープロセスが途中で落ちる原因になります。

## Example
```ruby
# 数百万件を一括で処理するとOOMのリスクがある
User.all.each { |u| heavy_process(u) }
```


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
