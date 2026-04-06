# JavaScriptループ基礎マップ

> **このMOCで分かること**: JavaScript の繰り返し処理を、構文・各パーツ・配列操作の視点で整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | for文 | 回数が決まった繰り返しの基本構文 | [[note-insight-for-loop]] |
| 2 | 初期化 | ループ開始前の最初の値の設定 | [[note-insight-initialization]] |
| 3 | 増減式 | ループごとに値を増減させる部分 | [[note-insight-increment-expression]] |
| 4 | 無限ループ | 終了条件がなく止まらない状態 | [[note-insight-infinite-loop]] |
| 5 | 配列とループ処理 | 配列を順番に取り出して処理する方法 | [[note-insight-array-loop-processing]] |

---

## セクション1: ループの骨組み

[[note-insight-for-loop]]
[[note-insight-initialization]]
[[note-insight-increment-expression]]

**ポイント**:
- `for` は初期化、条件、増減式の 3 要素で構成される
- 配列は 0 番目から始まることを前提に考える

---

## セクション2: ミスしやすいところ

[[note-insight-infinite-loop]]

**ポイント**:
- 条件や増減式を誤ると終了しない
- 逆順ループでは開始位置と終了条件の両方を確認する

---

## セクション3: 配列処理への応用

[[note-insight-array-loop-processing]]

**ポイント**:
- `length` を使えば先頭から末尾まで順番に処理できる
- 文字列メソッドとの組み合わせで実用的な変換もできる

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| `for` と `forEach` と `map` の使い分けは何か | - | - | [[note-insight-for-loop]] |
| 逆順ループが必要になる典型例は何か | - | - | [[note-insight-array-loop-processing]] |

---

## 関連リンク

- [[note-insight-for-loop]]
- [[note-insight-initialization]]
- [[note-insight-increment-expression]]
- [[note-insight-infinite-loop]]
- [[note-insight-array-loop-processing]]
