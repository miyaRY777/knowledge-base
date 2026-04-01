# Rails基礎マップ

> **このMOCで分かること**: Rails開発で押さえておくべき基礎概念（モデル・DB・Web一般）の全体像

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | dependent: :restrict_with_error | 関連レコードがある親の削除を安全にブロック | [[note-insight-dependent-restrict-with-error]] |
| 2 | 冪等性 | 同じ操作を何回やっても結果が変わらない性質 | [[note-insight-idempotent]] |
| 3 | UNIQUE制約とNULL | NULLは「不明」なのでUNIQUE制約の対象外 | [[note-insight-unique-constraint-null]] |
| 4 | slug | URLに使う人が読める識別子 | [[note-insight-slug]] |

---

## セクション1: ActiveRecord / モデル層

[[note-insight-dependent-restrict-with-error]]

**ポイント**:
- 関連レコードの削除制御はdependentオプションで行う
- :restrict_with_error はバリデーションに近い挙動でUIと相性が良い
- :destroy, :nullify, :restrict_with_exception との使い分けが重要

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
| dependentオプションの全種類の使い分け整理 | - | - | - |
| NULLを含むカラムでユニーク性を保証する方法 | - | - | - |
| friendly_id gemの導入手順 | - | - | - |
| 冪等性を意識したAPI設計パターン | - | - | - |

---

## 関連リンク

- [[note-insight-dependent-restrict-with-error]]
- [[note-insight-idempotent]]
- [[note-insight-unique-constraint-null]]
- [[note-insight-slug]]
- [[2026-03-30_insight_rails-study.md]]
