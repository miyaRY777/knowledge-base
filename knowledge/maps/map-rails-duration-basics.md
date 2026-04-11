# Rails日時計算基礎マップ

> **このMOCで分かること**: `ActiveSupport::Duration` と `.from_now` / `.ago` を中心に、Rails の日時計算の基本を整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | `ActiveSupport::Duration` | 時間量を表すオブジェクト | [[note-insight-activesupport-duration]] |
| 2 | `.from_now` と `.ago` | 現在時刻を基準に Time を作る | [[note-insight-from-now-and-ago]] |

---

## 時間量

[[note-insight-activesupport-duration]]

`1.day` のような値は数値ではなく Duration オブジェクトです。時間の長さそのものを表す材料として使います。

---

## 時刻計算

[[note-insight-from-now-and-ago]]

`.from_now` は未来、`.ago` は過去の時刻を作ります。Duration と Time を分けて考えると、期限計算の意図が読みやすくなります。

---

## 具体例との接続

[[2026-04-11-action-policy-shares-controller]]
[[2026-04-07-regenerate-share-link]]
[[2026-04-06-room-form-improvement]]

これらのプロジェクトノートには、期限計算や `from_now` の実装例があります。

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| Duration の内部構造をどこまで掘るか | - | - | [[note-insight-activesupport-duration]] |
| `.from_now` と `.since` の違いをどう整理するか | - | - | [[note-insight-from-now-and-ago]] |
| 期限切れ判定の実装例を atomic note に切り出すか | - | - | [[note-insight-from-now-and-ago]] |

---

## 関連リンク

- [[map-2026-04-learning]]
