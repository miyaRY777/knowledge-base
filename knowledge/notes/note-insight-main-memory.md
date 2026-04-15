---
id: note-insight-main-memory
title: 主記憶装置はCPUがすぐ使う一時領域
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
主記憶装置は、コンピュータが今まさに使っているデータを一時的に置いておく場所です。CPU がすぐ参照できるように高速で設計されていますが、そのぶん電源を切ると内容は保持されません。長期保管ではなく、作業中の情報を広げる作業机のような役割として理解すると分かりやすいです。実際には、プログラムやデータをストレージから主記憶装置へ読み込み、その内容を CPU が処理する流れで動きます。

## Example
```ruby
main_memory = "RAM"

puts "#{main_memory} は一時的にデータを置く場所"
```

このコードでは、主記憶装置が一時的な作業領域であることを確認しています。

## Action
- [ ] キャッシュとの違いも後で整理する
