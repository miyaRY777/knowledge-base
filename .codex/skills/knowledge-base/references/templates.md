# knowledge-base Templates

## ask

```markdown
## 結論
1〜2文で回答

## 根拠
- [[note-xxx]]: このノートから分かること

## 補足
追加文脈

## 次アクション
推奨ステップ
```

## search

```markdown
## 「キーワード」の検索結果（X件）

| ノート | タイトル | マッチ箇所 |
|--------|---------|-----------|
| [[note-...]] | タイトル | Body |
```

## capture

```markdown
# タイトル

**日時**: YYYY-MM-DD
**情報源**: Raycast学習メモ

---
ここにメモを貼る
```

## distill

```markdown
---
id: note-{category}-{short-name}
title: タイトル
created: YYYY-MM-DD
source: [[inbox-file-name]]
---

## Summary
- 要点1
- 要点2
- 要点3

## Tags
#tag1 #tag2

## Links
- [[関連ノート]]

## Body
要点と背景を自分の言葉で要約する
```

## moc

```markdown
# テーママップ

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | ... | ... | [[note-...]] |

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| ... | ... | ... | [[note-open-...]] |
```
