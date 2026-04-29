# Ruby / Rails述語メソッド基礎マップ

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | `nil?` | 値そのものが nil かを見る Ruby のメソッド | [[note-insight-ruby-nil-predicate]] |
| 2 | `empty?` | 文字列や配列などの中身が空かを見る Ruby のメソッド | [[note-insight-ruby-empty-predicate]] |
| 3 | `empty?` の nil リスク | nil に `empty?` を呼ぶと NoMethodError になる | [[note-insight-ruby-empty-predicate-nil-risk]] |
| 4 | nil確認後の `empty?` | 素の Ruby で安全に空判定する書き方 | [[note-insight-ruby-check-nil-before-empty]] |
| 5 | `blank?` | Railsで nil や空文字などをまとめて空扱いする | [[note-insight-rails-blank-predicate]] |
| 6 | `present?` | `blank?` の反対で、中身があるかを見る | [[note-insight-rails-present-predicate]] |
| 7 | `presence` | 空なら nil、空でなければ値を返してフォールバックに使える | [[note-insight-rails-presence]] |
| 8 | `presence` の活用 | 入力値や表示名の代替値を短く書ける | [[note-insight-rails-presence-use-case]] |
| 9 | 使い分け比較 | RubyとRailsの空判定をまとめて比較する | [[note-insight-ruby-rails-presence-predicate-comparison]] |
| 10 | `&.` | nil のときにメソッド呼び出しを避ける safe navigation operator | [[note-insight-ruby-safe-navigation-operator]] |

---

## セクション1: 素のRubyでの存在確認

[[note-insight-ruby-nil-predicate]]
[[note-insight-ruby-empty-predicate]]
[[note-insight-ruby-empty-predicate-nil-risk]]
[[note-insight-ruby-check-nil-before-empty]]

**ポイント**:
- `nil?` は値そのものが存在しないかを見る
- `empty?` はオブジェクトはあるが中身が空かを見る
- `empty?` は nil に使えないため、nil の可能性がある値では事前確認が必要

---

## セクション2: Railsでの空判定

[[note-insight-rails-blank-predicate]]
[[note-insight-rails-present-predicate]]
[[note-insight-rails-presence]]
[[note-insight-rails-presence-use-case]]

**ポイント**:
- `blank?` は nil、空文字、空配列、空ハッシュ、false などをまとめて空扱いできる
- `present?` は `blank?` の反対で、値があるときの条件に向く
- `presence` は空なら nil を返すため、フォールバック値と組み合わせやすい

---

## セクション3: 安全に短く書くための判断

[[note-insight-ruby-rails-presence-predicate-comparison]]
[[note-insight-ruby-safe-navigation-operator]]

**ポイント**:
- Rails では `blank?` / `present?` / `presence` が空判定を短くする
- `&.` は nil の可能性があるメソッド呼び出しを安全にできる
- ただし、`&.` の多用は本来気づくべき nil を見逃すことがある

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| `nil?`、`empty?`、`blank?`、`present?`、`presence` の差分表を作る | - | - | [[note-insight-ruby-rails-presence-predicate-comparison]] |
| `blank?` が false を空扱いする影響をどう説明するか | - | - | [[note-insight-rails-blank-predicate]] |
| `&.` と明示的な nil チェックの使い分けを整理する | - | - | [[note-insight-ruby-safe-navigation-operator]] |
| `presence_in` との違いを追加するか | - | - | [[note-insight-rails-presence-use-case]] |

---

## 関連リンク

- [[map-rails-basics]]
- [[note-insight-ruby-nil-predicate]]
- [[note-insight-ruby-empty-predicate]]
- [[note-insight-ruby-empty-predicate-nil-risk]]
- [[note-insight-ruby-check-nil-before-empty]]
- [[note-insight-rails-blank-predicate]]
- [[note-insight-rails-present-predicate]]
- [[note-insight-rails-presence]]
- [[note-insight-rails-presence-use-case]]
- [[note-insight-ruby-rails-presence-predicate-comparison]]
- [[note-insight-ruby-safe-navigation-operator]]
