---
id: note-insight-float-type
title: float型は32ビット単精度の浮動小数点型
created: 2026-06-04
source: [[2026-06-04_insight_floating-point-type-basics]]
---

## Summary
- float型は32ビットで表される単精度浮動小数点型です。
- double型より少ないメモリで扱えますが、精度は低くなります。
- IEEE 754のbinary32形式で、符号1ビット・指数8ビット・仮数23ビットで構成されます。

## Tags
#computer-architecture #data-type

## Links
- [[note-insight-double-type]]
- [[note-insight-floating-point-type]]
- [[note-insight-ieee754]]

## Body
float型はJavaやCなどで使われる32ビット単精度の浮動小数点型です。メモリ使用量が少ない分、double型より精度が低く、扱える数の範囲も狭くなります。JavaScriptにはfloat型がなく、すべての数値はdouble相当のNumber型で扱われます。
