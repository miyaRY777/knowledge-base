---
name: knowledge-base
description: Use when working inside the local knowledge-base repository to answer questions from notes, search the knowledge base, capture inbox memos, distill inbox files into atomic notes, build or update MOCs, run quiz-style review, or generate weekly reviews.
---

# Knowledge Base Skill

対象リポジトリ:
- `/Users/miyary777/workspace/miyaRY777/knowledge-base`

読む順番:
- 全体運用は `references/workflows.md`
- パスや検索対象は `references/paths.md`
- 出力フォーマットは `references/templates.md`
- 実行時は `scripts/kb_tool.py` を使う

## 目的

- Claude 用 `.claude/commands` と `.claude/agents` の運用を Codex でも扱えるようにする

## 対応する役割

- `knowledge-qa`
- `note-distiller`
- `moc-builder`

## 対応する操作

- `capture`
- `distill`
- `moc`
- `ask`
- `search`
- `quiz`
- `quiz-answer`
- `weekly-review`

## 実行ルール

- 推測で埋めない
- 参照元を必ず示す
- `distill` と `moc` は保存前に案を見せる
- 既存ノートとの重複を確認する
- ノート本文は自分の言葉で要約する

## 重複ルール

- inbox の重複は許容する
- 重複チェックは `distill` で行う
- 同一概念の補強なら既存ノート更新を優先する
- 別観点の学びなら別ノートを許容し、`Links` でつなぐ
- 完全一致に近い場合は、新規作成ではなく更新提案を返す

## 実行例

- `python3 .codex/skills/knowledge-base/scripts/kb_tool.py capture rails-study`
- `python3 .codex/skills/knowledge-base/scripts/kb_tool.py search callback`
- `python3 .codex/skills/knowledge-base/scripts/kb_tool.py ask "Callbacksの注意点は？"`
- `python3 .codex/skills/knowledge-base/scripts/kb_tool.py distill 2026-03-31_insight_rails-study.md`
- `python3 .codex/skills/knowledge-base/scripts/kb_tool.py moc rails --write`
- `python3 .codex/skills/knowledge-base/scripts/kb_tool.py quiz --tag rails --count 3 --show-answer`
- `python3 .codex/skills/knowledge-base/scripts/kb_tool.py quiz-answer note-insight-active-record-callbacks "C" --correct-choice C --write`
- `python3 .codex/skills/knowledge-base/scripts/kb_tool.py quiz-answer note-insight-active-record-callbacks "保存前後に自動で処理を挟む仕組み" --write`
- `python3 .codex/skills/knowledge-base/scripts/kb_tool.py weekly-review`
