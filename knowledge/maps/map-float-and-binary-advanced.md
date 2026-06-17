# 浮動小数点・2進数詳細マップ

> **このMOCで分かること**: IEEE754の仕組みから2進小数の変換・丸め誤差・JavaScriptの数値の特殊値までを整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | IEEE 754 | 浮動小数点数の表現と計算を定めた標準規格 | [[note-insight-ieee754]] |
| 2 | 仮数 | 指数表記における数字の本体部分 | [[note-insight-mantissa]] |
| 3 | 指数 | 小数点をどれだけ動かすかを表す数 | [[note-insight-exponent]] |
| 4 | 指数表記 | 大きな数を仮数×基数^指数で短く表す書き方 | [[note-insight-scientific-notation]] |
| 5 | E表記 | 指数表記をプログラムで書きやすくした記法 | [[note-insight-e-notation]] |
| 6 | 有効数字 | 数値の中で信頼できる桁数 | [[note-insight-significant-figures]] |
| 7 | 正規化 | 指数表記の形を一定ルールにそろえること | [[note-insight-normalization]] |
| 8 | 基数 | 何進数かを示す土台の数 | [[note-insight-radix]] |
| 9 | 2進数→10進数 | 各桁の2の累乗を足して変換する | [[note-insight-binary-to-decimal]] |
| 10 | 2進小数 | 小数部分を2のマイナス乗で表した数 | [[note-insight-binary-fraction]] |
| 11 | 10進小数→2進小数 | 小数部に2を掛けて整数部を取り出す変換方法 | [[note-insight-decimal-to-binary-fraction]] |
| 12 | 正確に表せる小数 | 分母が2のべき乗の小数だけが2進数で正確に表せる | [[note-insight-binary-exact-decimal]] |
| 13 | 循環小数 | 同じ数字の並びが無限に繰り返される小数 | [[note-insight-repeating-binary-fraction]] |
| 14 | 丸め誤差 | 有限ビットで数値を表すときに生じる誤差 | [[note-insight-rounding-error]] |
| 15 | 浮動小数点の比較 | 誤差を考慮して差が十分小さいか確認する | [[note-insight-float-comparison]] |
| 16 | 浮動小数点の除算 | 小数部分を含む結果が得られる | [[note-insight-float-division]] |
| 17 | NaN | 数値として有効な結果を表せないときに返る特別な値 | [[note-insight-nan]] |
| 18 | Infinity | JavaScriptで無限大を表すnumber型の特別な値 | [[note-insight-infinity]] |
| 19 | -Infinity | JavaScriptで負の無限大を表すnumber型の特別な値 | [[note-insight-negative-infinity]] |
| 20 | Number.MAX_VALUE | JavaScriptのnumber型で表現できる最大の有限値 | [[note-insight-number-max-value]] |
| 21 | Number.MIN_VALUE | JavaScriptで0より大きい最小の正の値 | [[note-insight-number-min-value]] |
| 22 | JSの除算 | 整数同士でも小数を含む結果を返す | [[note-insight-js-division]] |
| 23 | JSのnumber型統一 | 整数と小数をどちらもnumber型として扱う | [[note-insight-js-number-type-unified]] |

---

## セクション1: 浮動小数点の仕組み

[[note-insight-ieee754]]
[[note-insight-mantissa]]
[[note-insight-exponent]]
[[note-insight-scientific-notation]]
[[note-insight-e-notation]]
[[note-insight-significant-figures]]
[[note-insight-normalization]]
[[note-insight-radix]]

**ポイント**:
- 浮動小数点数は「仮数 × 基数^指数」の形で表現する（IEEE 754準拠）
- 正規化により仮数の形を統一することで、表現の一意性を保つ
- E表記（例：`1.5e3` = 1500）はコードで指数表記を書く方法

---

## セクション2: 2進小数と変換

[[note-insight-binary-to-decimal]]
[[note-insight-binary-fraction]]
[[note-insight-decimal-to-binary-fraction]]
[[note-insight-binary-exact-decimal]]
[[note-insight-repeating-binary-fraction]]

**ポイント**:
- 2進小数は各桁が `2^-1`（0.5）、`2^-2`（0.25）… を表す
- `0.1` は2進数で循環小数になるため、正確に表現できない
- 分母が2のべき乗の小数（例：0.5、0.25）だけが2進数で正確に表せる

---

## セクション3: 誤差と注意点

[[note-insight-rounding-error]]
[[note-insight-float-comparison]]
[[note-insight-float-division]]

**ポイント**:
- `0.1 + 0.2 === 0.3` は多くの言語でfalseになる（丸め誤差）
- 浮動小数点数の比較は `===` ではなく差の絶対値が十分小さいかで判定する
- 浮動小数点数が混じると除算結果も小数になる

---

## セクション4: JavaScriptの特殊な数値

[[note-insight-js-division]]
[[note-insight-js-number-type-unified]]
[[note-insight-nan]]
[[note-insight-infinity]]
[[note-insight-negative-infinity]]
[[note-insight-number-max-value]]
[[note-insight-number-min-value]]

**ポイント**:
- JavaScriptはintとfloatを区別せずすべて`number`型（IEEE 754のdouble）
- 整数同士の除算でも小数が返る（例：`5 / 2 = 2.5`）
- `NaN`、`Infinity`、`-Infinity` は数値型の特殊な値として存在する
- `Number.MAX_VALUE` を超えると `Infinity` になる

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| 金融計算で浮動小数点を避けるべき理由をまとめる | - | - | [[note-insight-rounding-error]] |
| NaNの判定方法（isNaN vs Number.isNaN）を整理する | - | - | [[note-insight-nan]] |
| Rubyの小数型とJSのnumber型の違いを比較する | - | - | [[note-insight-js-number-type-unified]] |

---

## 関連リンク

- [[map-data-types-and-binary-basics]]
- [[map-type-and-literal-basics]]
- [[map-type-conversion-basics]]
- [[map-operator-and-expression-basics]]
