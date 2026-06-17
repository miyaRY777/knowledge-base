# null・偽値基礎マップ

> **このMOCで分かること**: null・undefined・void・false・空文字の違いと、nullチェックの基本を整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | false | 「いいえ」の状態を表す値。nullとは別物 | [[note-insight-false-value]] |
| 2 | 0（ゼロ） | 数値としてのゼロ。「値がない」ではない | [[note-insight-zero-value]] |
| 3 | void | 「返す値がない」を表す型・キーワード | [[note-insight-void]] |
| 4 | null（JS） | 値が存在しないことを表すプリミティブ値 | [[note-insight-null-js]] |
| 5 | null vs void | nullは「値がない」、voidは「戻り値がない」 | [[note-insight-null-vs-void]] |
| 6 | nullable | 値がnullになる可能性があることを示す | [[note-insight-nullable]] |
| 7 | nullチェック | nullかどうかを確認してから処理する | [[note-insight-null-check]] |
| 8 | ??演算子 | null/undefinedのときだけ代替値を返す | [[note-insight-nullish-coalescing]] |
| 9 | 空文字 | 中身がゼロ文字の文字列 | [[note-insight-empty-string]] |
| 10 | 空文字 vs null | 空文字は文字列が存在する状態、nullは値が存在しない状態 | [[note-insight-empty-string-vs-null]] |
| 11 | 整数型 vs 文字列型 | 計算と文字連結で挙動が異なる | [[note-insight-integer-vs-string]] |

---

## セクション1: 「偽」に見える値の違い

[[note-insight-false-value]]
[[note-insight-zero-value]]
[[note-insight-empty-string]]

**ポイント**:
- `false` / `0` / `""` はどれも「偽値（falsy）」だが、意味が違う
- `false` は論理的な「いいえ」、`0` は数値、`""` は空の文字列
- 「値がない」のは `null` や `undefined`。`0` や `""` は「値がある」

---

## セクション2: null・void・undefined の使い分け

[[note-insight-null-js]]
[[note-insight-void]]
[[note-insight-null-vs-void]]
[[note-insight-nullable]]

**ポイント**:
- `null` は「値が存在しない」を明示的に示す
- `void` は「戻り値がない」関数に使う型・キーワード
- `nullable` は変数がnullになり得ることを型レベルで示す概念

---

## セクション3: nullの安全な扱い方

[[note-insight-null-check]]
[[note-insight-nullish-coalescing]]
[[note-insight-empty-string-vs-null]]
[[note-insight-integer-vs-string]]

**ポイント**:
- nullを使う前に必ずnullチェックする
- `??` 演算子はnull / undefinedのときだけ右辺を返す（`||` との違いに注意）
- 空文字とnullは別物。DBや入力フォームではどちらが来るか意識する
- 整数と文字列で `+` の挙動が変わるため、型確認が重要

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| `??` と `||` の使い分け基準を整理する | - | - | [[note-insight-nullish-coalescing]] |
| Railsで空文字とnilをどう統一するか | - | - | [[note-insight-empty-string-vs-null]] |
| nullableとOptional型の対応関係をまとめる | - | - | [[note-insight-nullable]] |

---

## 関連リンク

- [[map-type-and-literal-basics]]
- [[map-type-conversion-basics]]
- [[map-ruby-rails-predicate-basics]]
