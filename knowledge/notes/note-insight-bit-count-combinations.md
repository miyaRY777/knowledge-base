---
id: note-insight-bit-count-combinations
title: "2^ビット数でそのビット数が表現できる値の総数を求める"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
---

## Summary
- nビットで表現できる値の総数は 2ⁿ 通りです。
- 1ビット増えるごとに表現できる数は2倍になります。
- 8ビット = 256通り、16ビット = 65,536通りです。

## Tags
#computer #binary #data-type

## Links
- [[note-insight-bit]]
- [[note-insight-binary-data]]
- [[note-insight-hexadecimal-literal-0x]]

## Body
ビット数とその組み合わせ数は指数関係にあります。各ビットは0か1の2値をとるため、nビットの組み合わせは 2ⁿ 通りになります。これはデータ型の表現範囲やパスワードの強度を考えるときの基本です。

## Example
- 1ビット → 2¹ = 2通り（0, 1）
- 8ビット → 2⁸ = 256通り（0〜255）
- 16ビット → 2¹⁶ = 65,536通り
- 32ビット → 2³² = 約42億通り
