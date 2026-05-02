---
id: note-insight-cpu
title: "CPUは制御装置と演算装置をまとめた中心装置"
created: 2026-04-10
source: [[2026-04-10_insight_computer-five-major-units]]
---

## Summary
- CPU は制御装置と演算装置をまとめた中央処理装置です。
- コンピュータ全体の処理の中心としてメモリから命令を読み取って実行します。
- クロック周波数やコア数は処理性能に影響します。

## Tags
#computer #hardware #cpu

## Links
- [[note-insight-control-unit]]
- [[note-insight-arithmetic-unit]]
- [[note-insight-main-memory]]
- [[note-insight-instruction]]
- [[note-insight-fetch-decode-execute]]

## Body
CPU は、制御装置と演算装置の働きをまとめて持つ中心的な装置です。メモリから命令を読み取り、処理の流れを管理しながら、必要な計算や比較を進めます。コンピュータ全体の処理を前に進める中核として動くため、頭脳と表現されることが多いです。処理の速さにはクロック周波数やコア数も関わるので、CPU の性能を見るときの基本的な観点になります。

## Example
```ruby
cpu = {
  control_unit: "命令を読み取って指示を出す",
  alu: "計算や比較を行う"
}

puts cpu
```

このコードでは、CPU が制御装置と演算装置で構成されることを整理しています。

## Action
- [ ] CPU とメモリの関係も別ノートで整理する
