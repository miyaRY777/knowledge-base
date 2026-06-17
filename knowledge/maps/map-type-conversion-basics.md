# 型変換基礎マップ

> **このMOCで分かること**: 暗黙・明示的な型変換の仕組みと、型変換によるバグのパターンを整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | 型変換 | データを別のデータ型として扱えるように変換すること | [[note-insight-type-conversion]] |
| 2 | 暗黙的な型変換 | 言語が自動的に型を変換すること | [[note-insight-implicit-type-conversion]] |
| 3 | 明示的な型変換 | プログラマーが変換先の型を指定して変換すること | [[note-insight-explicit-type-conversion]] |
| 4 | キャスト | 値を指定したデータ型として扱う明示的な型変換 | [[note-insight-cast]] |
| 5 | 型の昇格 | 狭い範囲の型をより広い範囲の型へ変換すること | [[note-insight-type-promotion]] |
| 6 | 混合型演算 | 異なるデータ型の値を含む演算 | [[note-insight-mixed-type-expression]] |
| 7 | 異型演算の型変換 | 異なる型同士の演算で一方の型が変換されることがある | [[note-insight-mixed-type-arithmetic]] |
| 8 | 計算結果の型 | オペランドの型と演算子と言語の規則で決まる | [[note-insight-calculation-result-type]] |
| 9 | 型変換バグ | 想定外の型変換で発生するプログラムの不具合 | [[note-insight-type-conversion-bug]] |
| 10 | typeof | 値のデータ型を文字列で返す演算子 | [[note-insight-typeof]] |
| 11 | 整数型 vs 文字列型 | 計算と文字連結で挙動が異なる | [[note-insight-integer-vs-string]] |

---

## セクション1: 型変換の種類

[[note-insight-type-conversion]]
[[note-insight-implicit-type-conversion]]
[[note-insight-explicit-type-conversion]]
[[note-insight-cast]]

**ポイント**:
- 暗黙的変換は言語が自動でやる（気づかないとバグになる）
- 明示的変換はプログラマーが意図して書く（キャスト）
- JavaScriptは暗黙的変換が多いため特に注意が必要

---

## セクション2: 混合型演算と結果型

[[note-insight-type-promotion]]
[[note-insight-mixed-type-expression]]
[[note-insight-mixed-type-arithmetic]]
[[note-insight-calculation-result-type]]
[[note-insight-integer-vs-string]]

**ポイント**:
- 整数と小数を混ぜると型が昇格して結果が小数になることがある
- `+` は数値なら加算、文字列なら連結。型が混在すると予期しない動作になる
- 計算結果の型はオペランドの型と言語の規則で決まる

---

## セクション3: 型変換バグと確認方法

[[note-insight-type-conversion-bug]]
[[note-insight-typeof]]

**ポイント**:
- 型変換バグは「なぜか計算が合わない」「文字列が連結された」といった形で現れる
- `typeof` で実際の型を確認することがデバッグの第一歩

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| JavaScriptの暗黙的変換の主なパターンをまとめる | - | - | [[note-insight-implicit-type-conversion]] |
| 型変換バグを防ぐためのlint設定は何か | - | - | [[note-insight-type-conversion-bug]] |
| Rubyの型変換の仕組みをJSと比較する | - | - | [[note-insight-type-conversion]] |

---

## 関連リンク

- [[map-type-and-literal-basics]]
- [[map-null-and-falsy-basics]]
- [[map-operator-and-expression-basics]]
- [[map-float-and-binary-advanced]]
