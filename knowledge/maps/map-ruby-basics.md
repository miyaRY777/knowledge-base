# Ruby基礎マップ

> **このMOCで分かること**: Rubyのnil・空文字・述語メソッド・安全航法演算子など、よく使う基礎を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | nil?メソッド | 値がnilかどうかを確認する述語メソッド | [[note-insight-ruby-nil-predicate]] |
| 2 | empty?メソッド | 文字列・配列が空かどうかを確認する述語メソッド | [[note-insight-ruby-empty-predicate]] |
| 3 | empty?のnilリスク | nilに対してempty?を呼ぶとエラーになる | [[note-insight-ruby-empty-predicate-nil-risk]] |
| 4 | nil確認後にempty?を使う | nilチェックをしてからempty?を呼ぶ安全な書き方 | [[note-insight-ruby-check-nil-before-empty]] |
| 5 | 安全航法演算子（&.） | nilのときにメソッド呼び出しをスキップする演算子 | [[note-insight-ruby-safe-navigation-operator]] |
| 6 | Rubyの定数 | 大文字始まりで定義する変更不可の値 | [[note-insight-ruby-constants]] |
| 7 | Rails presenceとの比較 | nil?・empty?・blank?・present?の使い分け | [[note-insight-ruby-rails-presence-predicate-comparison]] |

---

## nilと空の判定

[[note-insight-ruby-nil-predicate]]
[[note-insight-ruby-empty-predicate]]
[[note-insight-ruby-empty-predicate-nil-risk]]
[[note-insight-ruby-check-nil-before-empty]]
[[note-insight-ruby-safe-navigation-operator]]

**ポイント**:
- `nil?` はnilのときだけtrueを返す。空文字や空配列ではfalse
- `empty?` は文字列・配列・ハッシュが空のときtrueを返す。nilに呼ぶと `NoMethodError`
- nilの可能性があるときは `value.nil? || value.empty?` か `value&.empty?` と書く
- 安全航法演算子 `&.` はレシーバがnilのとき、メソッドを呼ばずにnilを返す

---

## 述語メソッドの使い分け

[[note-insight-ruby-rails-presence-predicate-comparison]]

**ポイント**:
- `nil?` → nilのみ判定
- `empty?` → 空文字・空配列・空ハッシュを判定（nilは不可）
- `blank?`（Rails）→ nil・空文字・空白文字列・空コレクションをまとめて判定
- `present?`（Rails）→ blankでないときtrueを返す。`blank?` の逆
- Railsでは `blank?` / `present?` を使うとnilチェックが不要になり安全に書ける

---

## Rubyの定数

[[note-insight-ruby-constants]]

**ポイント**:
- 定数は大文字始まりで定義する（例: `MAX_SIZE = 100`）
- クラス名・モジュール名も定数の一種
- Rubyの定数は再代入しても警告が出るだけでエラーにはならない（不変ではない）

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| Rubyのブロック・Proc・lambdaを整理する | - | - | - |
| Enumerableメソッド（map・select・reduceなど）をまとめる | - | - | - |
| Rubyの例外処理（rescue・raise）をまとめる | - | - | - |

---

## 関連リンク

- [[map-ruby-rails-predicate-basics]]
- [[map-null-and-falsy-basics]]
- [[map-rails-basics]]
