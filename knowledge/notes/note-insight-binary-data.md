---
id: note-insight-binary-data
title: "バイナリは0と1だけで表現されたデータ"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
---

## Summary
- バイナリ（Binary）は、0と1だけで構成されたデータです。
- コンピュータ内部では文字・画像・音声もすべてバイナリとして扱われます。
- 2進数とほぼ同義で使われることが多いです。

## Tags
#computer #binary #data-type

## Links
- [[note-insight-transistor]]
- [[note-insight-bit]]
- [[note-insight-byte]]

## Body
バイナリとは、0と1の2値だけで表現されたデータのことです。コンピュータはトランジスタの電気的なON/OFFで情報を処理するため、内部的にはあらゆるデータがバイナリとして扱われます。テキスト・画像・音声・動画も、最終的にはバイナリのビット列として保存・転送されます。

## Example
- `00000001` → 1
- `01000001` → 65（ASCIIの'A'）
- `11110000` → 240
