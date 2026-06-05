---
id: note-insight-fixed-point-type
title: 固定小数点型は小数点位置を固定して数値を表す方式
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 1
---

## Summary
- 固定小数点型は、小数点の位置をあらかじめ決めて数値を扱う方式です。
- 整数部と小数部のビット数が固定されるため、扱える範囲と精度が決まります。
- 金額のように桁数を固定したい場面で使われることがあります。

## Tags
#programming #data-type #binary

## Links
- [[note-insight-binary-fixed-point]]
- [[note-insight-binary-data]]
- [[note-insight-signed-integer-type]]

## Body
固定小数点型は、小数点の位置を仕様として決めてしまう数値表現方式です。たとえば「整数部8ビット・小数部8ビット」と決めると、`12345` という整数を内部的に `123.45` として解釈できます。浮動小数点型（float/double）が小数点の位置を動的に変えるのに対し、固定小数点は安定した精度を保てる反面、扱える数値の範囲が狭くなります。

## Example
- 整数部8bit・小数部8bitの場合
  - 表現できる整数部の範囲：0〜255
  - 小数精度：1/256 ≈ 0.0039
