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
CPU は制御装置と演算装置をまとめた中央処理装置で、コンピュータ全体の処理を進める中核です。
制御装置がメモリから命令を読み取って各装置へ指示を出し、演算装置（ALU）が計算や比較を実行するという役割分担で動きます。
処理速度にはクロック周波数（1秒間に処理できるサイクル数）とコア数（並列処理できる数）が影響し、マルチコアCPUは複数の処理を同時に進められます。

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
