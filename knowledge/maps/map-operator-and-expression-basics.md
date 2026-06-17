# 演算子・式基礎マップ

> **このMOCで分かること**: 演算子の種類・オペランドの型・式の評価から戻り値・副作用までの基本を整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | 演算子 | オペランドに特定の処理を行う記号 | [[note-insight-operator]] |
| 2 | 算術演算子 | 数値の計算を行う演算子 | [[note-insight-arithmetic-operator]] |
| 3 | 四則演算 | 加算・減算・乗算・除算の4種類の演算 | [[note-insight-four-arithmetic-operations]] |
| 4 | 加算演算子（+） | 数値を足す・文字列では連結になる | [[note-insight-addition-operator]] |
| 5 | 減算演算子（-） | 数値を引く演算子 | [[note-insight-subtraction-operator]] |
| 6 | 乗算演算子（*） | 数値を掛ける演算子 | [[note-insight-multiplication-operator]] |
| 7 | 除算演算子（/） | 数値を割る演算子 | [[note-insight-division-operator]] |
| 8 | ゼロ除算 | 0で割るとエラーや特別な値を返す | [[note-insight-division-by-zero]] |
| 9 | 除算の型変換 | 整数同士の除算で小数が切り捨てられる挙動 | [[note-insight-division-type-cast]] |
| 10 | 整数除算 | 割り算の結果から小数部分を除き整数として扱う計算 | [[note-insight-integer-division]] |
| 11 | 整数除算の結果 | 整数同士の割り算は言語によって小数部分の扱いが異なる | [[note-insight-integer-division-result]] |
| 12 | 整数除算の切り捨て | 整数除算では小数部分が切り捨てられて整数の結果になる | [[note-insight-integer-division-truncation]] |
| 13 | 言語ごとの整数除算の違い | 整数同士の除算の結果は言語によって異なる | [[note-insight-integer-division-language-diff]] |
| 14 | オペランド | 演算子が操作する値や変数 | [[note-insight-operand]] |
| 15 | オペランドの型 | 演算子に渡す値のデータ型 | [[note-insight-operand-type]] |
| 16 | オペランドの型と結果の違い | オペランドの型が違うと演算結果が変わる | [[note-insight-operand-type-result-diff]] |
| 17 | 演算子の結果型 | オペランドの型と演算子の規則で決まる | [[note-insight-operator-result-type]] |
| 18 | 式 | 評価すると1つの値になるコードのまとまり | [[note-insight-expression]] |
| 19 | 評価 | 式を計算して結果の値を決めること | [[note-insight-expression-evaluation]] |
| 20 | 戻り値 | 関数の処理結果として呼び出し元に返される値 | [[note-insight-return-value]] |
| 21 | 関数の副作用 | 戻り値以外で外部の状態を変える処理 | [[note-insight-side-effect-function]] |

---

## セクション1: 演算子の種類と四則演算

[[note-insight-operator]]
[[note-insight-arithmetic-operator]]
[[note-insight-four-arithmetic-operations]]
[[note-insight-addition-operator]]
[[note-insight-subtraction-operator]]
[[note-insight-multiplication-operator]]
[[note-insight-division-operator]]

**ポイント**:
- 演算子は記号、オペランドはその対象（値・変数）
- `+` は数値なら加算、文字列なら連結になる（型によって挙動が変わる）
- 四則演算は `+ - * /` の4つが基本

---

## セクション2: オペランドの型と結果型

[[note-insight-operand]]
[[note-insight-operand-type]]
[[note-insight-operand-type-result-diff]]
[[note-insight-operator-result-type]]
[[note-insight-division-by-zero]]
[[note-insight-division-type-cast]]
[[note-insight-integer-division]]
[[note-insight-integer-division-result]]
[[note-insight-integer-division-truncation]]
[[note-insight-integer-division-language-diff]]

**ポイント**:
- 同じ演算子でもオペランドの型によって結果の型が変わる
- 整数÷整数は「整数除算」となり、小数部が切り捨てられる言語が多い
- ゼロ除算は言語・型によってエラーになる場合とInfinityになる場合がある
- 整数除算の挙動（切り捨て・切り上げ・丸め）は言語によって異なる（Ruby・JS・Javaなど）

---

## セクション3: 式・評価・戻り値・副作用

[[note-insight-expression]]
[[note-insight-expression-evaluation]]
[[note-insight-return-value]]
[[note-insight-side-effect-function]]

**ポイント**:
- 式は評価すると必ず1つの値になる
- 関数は戻り値を返す以外に、外部の状態を変える「副作用」を持つことがある
- 副作用のある関数は呼び出し順序や重複呼び出しに注意が必要

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| 言語ごとの整数除算の挙動の違いをまとめる | - | - | [[note-insight-division-type-cast]] |
| 副作用のある関数を安全に使うパターンは？ | - | - | [[note-insight-side-effect-function]] |
| ゼロ除算が実務で問題になるケースを整理する | - | - | [[note-insight-division-by-zero]] |

---

## 関連リンク

- [[map-type-and-literal-basics]]
- [[map-type-conversion-basics]]
- [[map-float-and-binary-advanced]]
- [[note-insight-operator]]
- [[note-insight-arithmetic-operator]]
- [[note-insight-expression]]
- [[note-insight-return-value]]
