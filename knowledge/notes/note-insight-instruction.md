---
id: note-insight-instruction
title: "命令はCPUに実行内容を伝えるためのデータ"
created: 2026-04-14
source: [[2026-04-14_insight_cpu-basic-terms]]
review_streak: 0
---

## Summary
- 命令は CPU に実行内容を伝えるためのデータです。
- プログラムは複数の命令が並んだ集合として成り立ちます。
- 命令には計算、分岐、データ移動などの指示が含まれます。

## Tags
#computer #hardware #instruction

## Links
- [[note-insight-cpu]]
- [[note-insight-control-unit]]
- [[note-insight-fetch-decode-execute]]

## Body
命令は、コンピュータに何をしてほしいかを表す最小単位の指示です。CPU はプログラム中に並んだ命令を順番に読み取り、内容に応じて計算したり、データを移動したり、処理の分岐を行ったりします。プログラム全体は命令の集まりとして動いていると考えると理解しやすいです。

## Example
```ruby
a = 1 + 2
```

このコードでは、「1 と 2 を足して結果を代入する」という命令を CPU が実行するイメージを表しています。

## Action
- [ ] 命令セットと機械語の関係も後で整理する
