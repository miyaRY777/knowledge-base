---
id: note-insight-bit-count-combinations
title: "2^ビット数でそのビット数が表現できる値の総数を求める"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
quiz_fail_log: []
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
各ビットは 0 か 1 の2値をとるため、n ビットの組み合わせは 2ⁿ 通りになります（指数関係）。
1ビット増えるごとに表現できる値が2倍になるため、`unsigned char`（8ビット）は 256 通り、`int`（32ビット）は約42億通りを表現できます。
この関係はデータ型の値域、文字コードのコードポイント数、ハッシュの衝突確率、パスワードの組み合わせ数など幅広い場面で使う基本公式です。

## Example
- 1ビット → 2¹ = 2通り（0, 1）
- 8ビット → 2⁸ = 256通り（0〜255）
- 16ビット → 2¹⁶ = 65,536通り
- 32ビット → 2³² = 約42億通り
