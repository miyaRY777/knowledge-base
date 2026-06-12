---
id: note-insight-binary-exact-decimal
title: 分母が2のべき乗になる小数だけが2進数で正確に表せる
created: 2026-06-12
source: [[2026-06-12_insight_js-number-types-and-floating-point]]
---

## Summary
- 10進小数を分数に直して約分したとき、分母が2のべき乗（2・4・8・16…）なら2進数で有限桁に収まります。
- 分母に2以外の素因数（5など）が含まれると、2進数では循環小数になります。

## Tags
#programming #binary #floating-point

## Links
- [[note-insight-binary-fraction]]
- [[note-insight-repeating-binary-fraction]]
- [[note-insight-rounding-error]]

## Body
2進数で正確に表せるかどうかは、分数に変換したときの分母で判断できます。`0.375 = 3/8`、分母8は `2³` なので正確に表せます。`0.1 = 1/10`、分母10は `2×5` で5が含まれるため循環小数になります。

## Example
| 小数 | 分数 | 分母の素因数 | 2進数で表せるか |
|---|---|---|---|
| 0.5 | 1/2 | 2のみ | ✅ |
| 0.375 | 3/8 | 2のみ | ✅ |
| 0.1 | 1/10 | 2と5 | ❌ |
| 0.3 | 3/10 | 2と5 | ❌ |
