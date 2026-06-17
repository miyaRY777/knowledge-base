---
id: note-insight-main-memory
title: "主記憶装置はCPUがすぐ使う一時領域"
created: 2026-04-10
source: [[2026-04-10_insight_computer-five-major-units]]
---

## Summary
- 主記憶装置はCPUがすぐ使うデータを一時的に置く場所です。
- 一般的にはメモリやRAMと呼ばれます。
- 高速ですが、電源を切ると内容が消えます。
- ストレージから読み込んだプログラムやデータを展開して、CPU が処理に使います。

## Tags
#computer #hardware #memory

## Links
- [[note-insight-storage-device]]
- [[note-insight-cpu]]
- [[note-insight-secondary-storage]]

## Body
主記憶装置（RAM）は、CPU が現在処理中のプログラムやデータを一時的に置く場所です。
ストレージ（SSD/HDD）より読み書きが高速ですが、電源を切ると内容が消える揮発性の特性があります。
プログラムを実行すると、まずストレージから主記憶装置へ読み込まれ、CPU はそのデータを参照・処理します。メモリ容量が不足すると処理の遅延や強制終了につながります。

## Example
```ruby
main_memory = "RAM"

puts "#{main_memory} は一時的にデータを置く場所"
```

このコードでは、主記憶装置が一時的な作業領域であることを確認しています。

## Action
- [ ] キャッシュとの違いも後で整理する
