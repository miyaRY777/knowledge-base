---
id: note-insight-fetch-decode-execute
title: フェッチ・デコード・実行はCPUの基本サイクル
created: 2026-04-14
source: [[2026-04-14_insight_cpu-basic-terms]]
---

## Summary
- CPU はフェッチ、デコード、実行の順で命令を処理します。
- この流れを高速に繰り返すことでプログラムが動作します。
- 命令処理の基本的な仕組みを理解する土台になります。

## Tags
#computer #hardware #cpu #execution-cycle

## Links
- [[note-insight-cpu]]
- [[note-insight-instruction]]
- [[note-insight-control-unit]]

## Body
フェッチ・デコード・実行は、CPU が命令を処理するときの基本サイクルです。まずメモリから命令を取り出し、次にその内容を解読し、最後に実際の処理を実行します。この流れを止まらず繰り返すことで、プログラム全体が順番に進んでいきます。CPU の動きは、この小さな処理の連続として捉えると理解しやすいです。

## Example
```text
Fetch -> Decode -> Execute -> Fetch -> ...
```

この例では、CPU が命令を取り出し、意味を解釈し、実行する流れを繰り返していることを表しています。

## Action
- [ ] メモリやプログラムカウンタとの関係も後で補足する
