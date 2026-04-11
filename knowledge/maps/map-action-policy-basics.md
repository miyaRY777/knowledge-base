# ActionPolicy基礎マップ

> **このMOCで分かること**: ActionPolicy による認可の責務分離、ハードブロック / ソフトブロック、`authorize!` と `allowed_to?` の使い分けをまとめて見渡せる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | 認可の責務分離 | 認可をコントローラからポリシーに分ける考え方 | [[note-insight-action-policy-responsibility-separation]] |
| 2 | ハードブロックとソフトブロック | 認可違反時にどこまで止めるかの違い | [[note-insight-hard-block-and-soft-block]] |
| 3 | `authorize!` と `allowed_to?` | 例外で止めるか、真偽値で扱うかの違い | [[note-insight-authorize-and-allowed-to-difference]] |

---

## 認可の責務分離

[[note-insight-action-policy-responsibility-separation]]

認可ロジックをコントローラから切り離してポリシーへ寄せると、責務が整理されて見通しがよくなります。

---

## ブロックの考え方

[[note-insight-hard-block-and-soft-block]]
[[note-insight-authorize-and-allowed-to-difference]]

ハードブロックは処理を止める認可、ソフトブロックは見せ方や操作を制御する認可です。`authorize!` と `allowed_to?` の違いはこの整理に対応しています。

---

## 具体例との接続

[[2026-04-11-action-policy-shares-controller]]

このプロジェクトノートでは、ActionPolicy の導入と `authorize!` / `allowed_to?` の使い分けが実装例つきで整理されています。

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| `authorize!` の内部で例外がどう流れるか | - | - | [[note-insight-authorize-and-allowed-to-difference]] |
| `policy(@post)` がどこで生成されるか | - | - | [[note-insight-action-policy-responsibility-separation]] |
| ハードブロックとソフトブロックの判断基準をどう言語化するか | - | - | [[note-insight-hard-block-and-soft-block]] |

---

## 関連リンク

- [[map-rails-controller-safety-and-turbo]]
- [[map-2026-04-learning]]
