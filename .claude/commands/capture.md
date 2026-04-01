---
description: 30秒でinboxに日付ファイルを生成
argument-hint: "<title-or-context>"
---

# /capture コマンド

Raycastなどで書いたメモを inbox に素早く取り込むためのファイルを生成します。

## 入力
- `$ARGUMENTS`: メモのタイトルまたは文脈（例: `rails-study`, `idea-new-feature`, `mtg-weekly`）

## 処理手順

### Step 1: ファイル名を生成する

形式: `YYYY-MM-DD_insight_{short-title}.md`

例:
- `2026-04-01_insight_rails-study.md`
- `2026-04-01_insight_new-feature-idea.md`

### Step 2: ファイルを生成する

```markdown
# {タイトル}

**日時**: YYYY-MM-DD
**情報源**: Raycast学習メモ

---

（ここにRaycastのメモをペーストしてください）
```

### Step 3: 出力

```markdown
## /capture 結果

### 保存先
`knowledge/inbox/YYYY-MM-DD_insight_{title}.md`

ファイルを作成しました。Raycastのメモをペーストしてください。
distillする準備ができたら `/distill YYYY-MM-DD_insight_{title}.md` を実行してください。
```

## 制約
- **シンプルに**: テンプレートは最小限。詳細は後でDistillする
- **日付は今日**: ファイル名の日付は実行日を使う
