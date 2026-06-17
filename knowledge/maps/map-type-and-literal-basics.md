# 型・リテラル基礎マップ

> **このMOCで分かること**: データ型の分類・リテラルの書き方・浮動小数点型と整数型の違いを整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | データ型 | 値の種類を表す分類 | [[note-insight-data-type]] |
| 2 | プリミティブ型 | 言語が基本として持つシンプルなデータ型 | [[note-insight-primitive-type]] |
| 3 | 文字列型 | 複数の文字をまとめて扱うデータ型 | [[note-insight-string-type]] |
| 4 | float型 | 32ビット単精度の浮動小数点型 | [[note-insight-float-type]] |
| 5 | double型 | 64ビット倍精度の浮動小数点型 | [[note-insight-double-type]] |
| 6 | 固定小数点型 | 小数点位置を固定して数値を表す方式 | [[note-insight-fixed-point-type]] |
| 7 | 浮動小数点型 | 小数を扱うプログラミングのデータ型 | [[note-insight-floating-point-type]] |
| 8 | 32ビット整数 | 2³²通りのビットパターンで整数を表す | [[note-insight-32bit-integer]] |
| 9 | 整数型の範囲 | ビット数によって決まる整数型の値の範囲 | [[note-insight-integer-range]] |
| 10 | リテラル | ソースコードに直接書かれた値 | [[note-insight-literal]] |
| 11 | 整数リテラル | 整数を直接コードに書いた値 | [[note-insight-integer-literal]] |
| 12 | 浮動小数点リテラル | 小数を直接コードに書いた値 | [[note-insight-floating-point-literal]] |
| 13 | 文字列リテラル | 文字の並びを直接コードに書いた値 | [[note-insight-string-literal]] |
| 14 | 論理値リテラル | trueまたはfalseを直接書いた値 | [[note-insight-boolean-literal]] |
| 15 | 文字リテラル | 1文字を表すリテラル | [[note-insight-character-literal]] |

---

## セクション1: データ型の分類

[[note-insight-data-type]]
[[note-insight-primitive-type]]
[[note-insight-string-type]]

**ポイント**:
- データ型は「どんな値か」を示す分類。型によって使える操作が決まる
- プリミティブ型は言語の最小単位（整数・小数・真偽値・文字列など）
- 文字列型は文字の集まりを1つのデータとして扱う

---

## セクション2: 小数型の種類

[[note-insight-float-type]]
[[note-insight-double-type]]
[[note-insight-fixed-point-type]]
[[note-insight-floating-point-type]]

**ポイント**:
- 浮動小数点型は小数点の位置を動かして表現する方式（float / double）
- float（32bit）より double（64bit）のほうが精度が高い
- 固定小数点型は小数点位置が固定されており、金融計算など誤差を避けたい場面で使う

---

## セクション3: 整数型のビット幅と範囲

[[note-insight-32bit-integer]]
[[note-insight-integer-range]]

**ポイント**:
- 整数型が扱える値の範囲はビット数で決まる（32bit整数は約±21億）
- ビット数を超えると「オーバーフロー」が起きる

---

## セクション4: リテラルの書き方

[[note-insight-literal]]
[[note-insight-integer-literal]]
[[note-insight-floating-point-literal]]
[[note-insight-string-literal]]
[[note-insight-boolean-literal]]
[[note-insight-character-literal]]

**ポイント**:
- リテラルはコードに直接書いた値（変数や式ではない）
- `42` は整数リテラル、`3.14` は浮動小数点リテラル、`"hello"` は文字列リテラル
- `true` / `false` は論理値リテラル。`'a'` は文字リテラル（言語によっては文字列と同じ）

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| float と double の使い分けをどう判断するか | - | - | [[note-insight-float-type]] |
| 固定小数点型を使うべき場面を具体例で整理する | - | - | [[note-insight-fixed-point-type]] |
| 各言語のプリミティブ型の対応表を作るか | - | - | [[note-insight-primitive-type]] |

---

## 関連リンク

- [[map-data-types-and-binary-basics]]
- [[map-type-conversion-basics]]
- [[map-null-and-falsy-basics]]
- [[map-float-and-binary-advanced]]
- [[map-operator-and-expression-basics]]
