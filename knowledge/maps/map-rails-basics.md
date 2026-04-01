# Rails基礎マップ

> **このMOCで分かること**: Rails開発で押さえておくべき基礎概念（モデル・DB・Web一般）の全体像

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | Active Record Callbacks | モデルの処理前後に自動で処理を挟む仕組み | [[note-insight-active-record-callbacks]] |
| 2 | CurrentAttributes | リクエスト単位で共有値をグローバル管理する仕組み | [[note-insight-current-attributes]] |
| 3 | dependent: :restrict_with_error | 関連レコードがある親の削除を安全にブロック | [[note-insight-dependent-restrict-with-error]] |
| 4 | 冪等性 | 同じ操作を何回やっても結果が変わらない性質 | [[note-insight-idempotent]] |
| 5 | UNIQUE制約とNULL | NULLは「不明」なのでUNIQUE制約の対象外 | [[note-insight-unique-constraint-null]] |
| 6 | slug | URLに使う人が読める識別子 | [[note-insight-slug]] |

---

## セクション1: ActiveRecord / モデル層

[[note-insight-active-record-callbacks]]
[[note-insight-current-attributes]]
[[note-insight-dependent-restrict-with-error]]

**ポイント**:
- Callbacksは便利だが多用すると処理の流れが見えにくくなる。複雑なロジックはServiceオブジェクトへ
- CurrentAttributesはリクエストスコープで便利だが、モデルに暗黙の依存を作る点に注意
- dependentオプションで関連レコードの削除制御。:restrict_with_errorはバリデーションに近い挙動

---

## セクション2: データベース / SQL

[[note-insight-unique-constraint-null]]

**ポイント**:
- NULLは「値が不明」であり、比較できないという性質を理解する
- UNIQUE制約の挙動はこの性質に直結する
- 任意入力カラム + UNIQUE制約の組み合わせで注意が必要

---

## セクション3: Web / API の基礎概念

[[note-insight-idempotent]]
[[note-insight-slug]]

**ポイント**:
- 冪等性はHTTPメソッドの設計原則であり、リトライ安全性に直結する
- slugはSEOとユーザビリティの両面でIDより優れたURL設計を実現する
- どちらもRails固有ではなくWeb全般の基礎知識

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

---

## 関連リンク

- [[note-insight-active-record-callbacks]]
- [[note-insight-current-attributes]]
- [[note-insight-dependent-restrict-with-error]]
- [[note-insight-idempotent]]
- [[note-insight-unique-constraint-null]]
- [[note-insight-slug]]
- [[2026-03-30_insight_rails-study.md]]
- [[2026-03-31_insight_rails-study.md]]
