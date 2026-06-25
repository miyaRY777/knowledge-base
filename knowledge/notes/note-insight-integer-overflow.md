---
id: note-insight-integer-overflow
title: "オーバーフローは表現できる範囲を超えて値があふれる現象"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- データ型の最大値を超えると、値が意図しない数値になります。
- 8ビット符号なし整数では 255 + 1 = 0 になる場合があります。
- セキュリティ上の脆弱性につながることもある重要な概念です。

## Tags
#programming #data-type #computer #security

## Links
- [[note-insight-signed-integer-type]]
- [[note-insight-unsigned-integer-type]]
- [[note-insight-bit-count-combinations]]

## Body
オーバーフローは、変数が保持できる最大値を超えた結果、値が「あふれて」意図しない数になる現象です。多くの言語では最大値の次が最小値に戻る「ラップアラウンド」が起きます。バグやセキュリティ脆弱性の原因になるため注意が必要です。

## Example
- 8ビット符号なし整数の最大値: 255（= `11111111`）
- 255 + 1 → ビットが溢れて `00000000` = 0 になる
- 意図せず 0 になってしまう

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
