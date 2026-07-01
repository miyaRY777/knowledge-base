---
name: knowledge-base
description: Use when working inside the local knowledge-base repository to answer questions from notes, search the knowledge base, capture inbox memos, distill inbox files into atomic notes, build or update MOCs, run quiz-style review, create or update journals, save PREP learning notes, or generate learning reviews.
---

# Knowledge Base Skill

対象リポジトリ:
- `/Users/miyary777/workspace/miyaRY777/knowledge-base`

この `SKILL.md` は入口です。運用ルールの正本は `references/workflows.md` に置きます。

## 読む順番

1. `references/workflows.md` — CODE、PREPノート、日誌、quiz、レビュー運用
2. `references/paths.md` — パスと検索優先順
3. `references/templates.md` — 出力フォーマット
4. `scripts/kb_tool.py` — 実行時に使う補助 CLI

## 実行ルール

- 推測で埋めない。
- 参照元を必ず示す。
- 書き込み系の操作は保存前に案を見せる。
- `distill`、`moc`、PREPノート保存、日誌作成・更新は `references/workflows.md` に従う。
- PREPノート保存を主導線とし、保存後に関連 MOC の作成・更新、日誌追記、quiz へつなげる。
- PREPノートは原則 distill せず、複数の独立した概念が混ざっている場合だけ分解する。
- 既存ノートとの重複を確認する。
- ノート本文は自分の言葉で要約する。

## 対応する操作

- `capture`
- `distill`
- `moc`
- `ask`
- `search`
- `quiz`
- `quiz-answer`
- `weekly-review`（実装済み・現在は未運用）
- `knowledge-file-audit`
- `monthly-learning-review`
- `journal`
- `prep-note-save`

## 実行例

```bash
python3 .codex/skills/knowledge-base/scripts/kb_tool.py capture rails-study
python3 .codex/skills/knowledge-base/scripts/kb_tool.py search callback
python3 .codex/skills/knowledge-base/scripts/kb_tool.py ask "Callbacksの注意点は？"
python3 .codex/skills/knowledge-base/scripts/kb_tool.py distill 2026-03-31_insight_rails-study.md
python3 .codex/skills/knowledge-base/scripts/kb_tool.py moc rails --write
python3 .codex/skills/knowledge-base/scripts/kb_tool.py quiz --tag rails --count 3 --show-answer
python3 .codex/skills/knowledge-base/scripts/kb_tool.py quiz-answer note-insight-active-record-callbacks "C" --correct-choice C --write
```
