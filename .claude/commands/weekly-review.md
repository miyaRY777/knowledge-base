---
description: 週次の学習棚卸しと振り返りを生成
argument-hint: ""
---

# /weekly-review コマンド

今週の学習を振り返り、inbox の棚卸し・新規ノートの確認・Open Questionsの進捗をまとめます。

## 処理手順

### Step 1: inbox の棚卸し

`knowledge/inbox/` を確認し、以下に分類してください:

| 分類 | 説明 |
|------|------|
| **Distill候補** | まだアトミックノート化していないファイル |
| **完了済み** | `inbox/done/` に移動すべきファイル |

出力形式:
```markdown
## inbox 棚卸し

### Distill候補（要処理）
- [ ] YYYY-MM-DD_insight_xxx.md

### 完了済み（done/ に移動してよいもの）
- [x] YYYY-MM-DD_insight_xxx.md
```

### Step 2: 今週の新規ノートを集計

`knowledge/notes/` から今週（直近7日）作成されたノートを抽出:

```markdown
## 今週覚えた概念（X件）

| 日付 | 概念 | タグ | ノート |
|------|------|------|--------|
| MM/DD | {概念名} | #tag | [[note-...]] |
```

### Step 3: Open Questions の確認

`knowledge/maps/` の各MOCにある「未決事項」セクションから未解決項目を抽出:

```markdown
## 未解決のOpen Questions

| 項目 | MOC |
|------|-----|
| {項目} | [[map-...]] |
```

### Step 4: 週次サマリーの生成

```markdown
# 週次レビュー（YYYY-MM-DD）

## 今週のサマリー
- 新規ノート: X件
- distill済みinbox: X件
- 未解決Open Questions: X件

## 今週よく出たタグ
- #rails: X件
- #database: X件

## 来週やること
- [ ] inbox に溜まったメモを /distill する
- [ ] Open Questions のうち {項目} を調べる
- [ ] /moc を更新する（対象: {テーマ}）
```

### Step 5: 提案

```markdown
## 提案
- `/distill YYYY-MM-DD_xxx.md` を実行しますか？
- `/moc {テーマ} --update` を実行しますか？
```
