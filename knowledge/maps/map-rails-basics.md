# Rails基礎マップ

> **このMOCで分かること**: Rails開発で押さえておくべき基礎概念（モデル・DB・Web一般）の全体像

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | Active Record Callbacks | モデルの処理前後に自動で処理を挟む仕組み | [[note-insight-active-record-callbacks]] |
| 2 | CurrentAttributes | リクエスト単位で共有値をグローバル管理する仕組み | [[note-insight-current-attributes]] |
| 3 | dependent: :restrict_with_error | 関連レコードがある親の削除を安全にブロック | [[note-insight-dependent-restrict-with-error]] |
| 4 | scope | よく使う検索条件をモデルに名前付きで定義する | [[note-insight-active-record-scope]] |
| 5 | ActiveRecord::Relation 遅延評価 | クエリは実際に必要になるまで発行されない | [[note-insight-active-record-relation-lazy-execution-flow]] |
| 6 | presence validation | 値が存在することを検証する | [[note-insight-presence-validation]] |
| 7 | uniqueness validation | 値が一意であることを検証する | [[note-insight-uniqueness-validation]] |
| 8 | inclusion validation | 許可した候補に含まれる値だけを通す検証 | [[note-insight-inclusion-validation]] |
| 9 | allow_nil | nil のときにバリデーションをスキップする指定 | [[note-insight-allow-nil]] |
| 10 | 冪等性 | 同じ操作を何回やっても結果が変わらない性質 | [[note-insight-idempotent]] |
| 11 | UNIQUE制約とNULL | PostgreSQLではデフォルトでNULLは重複扱いされない | [[note-insight-unique-constraint-null]] |
| 12 | slug | URLに使う人が読める識別子 | [[note-insight-slug]] |
| 13 | invariant | 常に守られているべき設計上の条件 | [[note-insight-invariant]] |
| 14 | orchestration | 複数の処理を順序立てて連携させる考え方 | [[note-insight-orchestration]] |
| 15 | Ruby定数 | 変更しない前提の値に名前を付ける仕組み | [[note-insight-ruby-constants]] |
| 16 | SecureRandom.urlsafe_base64 | URL向けの推測されにくいランダム文字列を作る | [[note-insight-securerandom-urlsafe-base64]] |
| 17 | Resendメールサービス | メール送信を担うSaaSサービス | [[note-insight-resend-email-service]] |
| 18 | 論理削除 | DBから消さずに削除済みとして扱う方法 | [[note-insight-soft-delete]] |
| 19 | 論理削除フラグ | 削除済み扱いを表す目印 | [[note-insight-soft-delete-flag]] |
| 20 | モンキーテスト | ランダムな操作で不具合を探すテスト | [[note-insight-monkey-testing]] |

---

## セクション1: ActiveRecord / モデル層

[[note-insight-active-record-callbacks]]
[[note-insight-current-attributes]]
[[note-insight-dependent-restrict-with-error]]
[[note-insight-active-record-scope]]
[[note-insight-active-record-relation-lazy-execution-flow]]
[[note-insight-presence-validation]]
[[note-insight-uniqueness-validation]]
[[note-insight-inclusion-validation]]
[[note-insight-allow-nil]]
[[note-insight-soft-delete]]
[[note-insight-soft-delete-flag]]

**ポイント**:
- Callbacksは便利だが多用すると処理の流れが見えにくくなる。複雑なロジックはServiceオブジェクトへ
- CurrentAttributesはリクエストスコープで便利だが、モデルに暗黙の依存を作る点に注意
- dependentオプションで関連レコードの削除制御。:restrict_with_errorはバリデーションに近い挙動
- scopeはよく使う検索条件をモデルに名前付きで定義する。ActiveRecord::Relationを返すので連鎖できる
- ActiveRecord::Relationは遅延評価。`.to_a` や `.each` など実際にデータが必要になるときにSQLが発行される
- `presence` は nil と空文字を同時に弾く。`uniqueness` はDB制約と組み合わせて確実性を高める
- `inclusion` と `allow_nil` は、保存してよい値の範囲と未入力時の扱いを整理するために使う
- 論理削除はレコードを残す設計なので、通常検索から除外する仕組みもセットで考える

---

## セクション2: データベース / SQL

[[note-insight-unique-constraint-null]]

**ポイント**:
- PostgreSQL のデフォルトでは、UNIQUE制約でも NULL は複数行に入れられる
- `NULLS NOT DISTINCT` を使うと NULL 同士を重複扱いにできる
- 任意入力カラム + UNIQUE制約では、DBごとのNULLの扱いを確認する

---

## セクション3: Web / API の基礎概念

[[note-insight-idempotent]]
[[note-insight-slug]]

**ポイント**:
- 冪等性はHTTPメソッドの設計原則であり、リトライ安全性に直結する
- slugはURLを人が読める形にし、ユーザーや検索エンジンに意味を伝えやすくする
- どちらもRails固有ではなくWeb全般の基礎知識

---

## セクション4: 設計と言語機能

[[note-insight-invariant]]
[[note-insight-orchestration]]
[[note-insight-ruby-constants]]
[[note-insight-securerandom-urlsafe-base64]]
[[note-insight-monkey-testing]]

**ポイント**:
- invariant は、アプリの途中で壊れてはいけない業務ルールとして考える
- orchestration は、複数の処理をどの順序で呼ぶかを整理する考え方
- Ruby定数や SecureRandom は、Railsアプリの設定値やトークン生成を読む土台になる
- モンキーテストは、想定外操作への耐性を見る品質確認として捉える

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| Callbacksの使いどころとServiceオブジェクトの使い分け基準 | - | - | - |
| CurrentAttributesをテスト・バッチ処理で安全に使う方法 | - | - | - |
| dependentオプションの全種類の使い分け整理 | - | - | - |
| NULLを含むカラムでユニーク性を保証する方法 | - | - | - |
| friendly_id gemの導入手順 | - | - | - |
| 冪等性を意識したAPI設計パターン | - | - | - |
| `allow_nil` と `allow_blank` の違いをRailsバリデーションで整理する | - | - | [[note-insight-allow-nil]] |
| token カラムに必要な一意性と推測困難性をどう保証するか | - | - | [[note-insight-securerandom-urlsafe-base64]] |
| 論理削除と物理削除の使い分けをどう判断するか | - | - | [[note-insight-soft-delete]] |

---

## 関連リンク

- [[note-insight-active-record-callbacks]]
- [[note-insight-current-attributes]]
- [[note-insight-dependent-restrict-with-error]]
- [[note-insight-active-record-scope]]
- [[note-insight-active-record-relation-lazy-execution-flow]]
- [[note-insight-presence-validation]]
- [[note-insight-uniqueness-validation]]
- [[note-insight-idempotent]]
- [[note-insight-unique-constraint-null]]
- [[note-insight-slug]]
- [[note-insight-inclusion-validation]]
- [[note-insight-allow-nil]]
- [[note-insight-invariant]]
- [[note-insight-orchestration]]
- [[note-insight-ruby-constants]]
- [[note-insight-securerandom-urlsafe-base64]]
- [[note-insight-resend-email-service]]
- [[note-insight-soft-delete]]
- [[note-insight-soft-delete-flag]]
- [[note-insight-monkey-testing]]
- [[2026-03-30_insight_rails-study.md]]
- [[2026-03-31_insight_rails-study.md]]
