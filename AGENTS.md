# knowledge-base Agent Guidance

このファイルは Codex が最初に読む入口です。詳細な運用仕様は `.codex/skills/knowledge-base/references/workflows.md` を正本とします。

---

## 最重要ルール

- 推測で埋めない。
- 根拠となるノートやファイルを示す。
- 書き込み系の操作は保存前に案を確認する。
- ノート作成・distill・MOC作成など知識保存に関わる作業では、自律実装モード指定があっても保存前確認を優先する。
- 複数ファイルを一括作成する場合は、まとめて作成してから1回確認する。
- ノート本文はコピペせず、自分の言葉で要約する。
- 重複メモは許容するが、重複ノートは `distill` 時に統合を検討する。
- PREPノート保存を主導線とし、保存後に関連 MOC の作成・更新、日誌追記、quiz へつなげる。
- PREPノートは原則 distill せず、複数の独立した概念が混ざっている場合だけ分解する。

---

## 読む順番

1. `.codex/skills/knowledge-base/SKILL.md`
2. `.codex/skills/knowledge-base/references/workflows.md`
3. `.codex/skills/knowledge-base/references/paths.md`
4. `.codex/skills/knowledge-base/references/templates.md`

---

## 役割分担

- `AGENTS.md`: 最重要ルールと読む順番だけを書く。
- `README.md`: 人間向けの概要を書く。
- `SKILL.md`: Codex skill の入口を書く。
- `references/workflows.md`: CODE、PREPノート、日誌、quiz、月次レビューなどの運用ルールの正本。
- `references/templates.md`: 出力形式の正本。
- `references/paths.md`: パスと検索優先順の正本。
- `CLAUDE.md` / `.claude/`: Claude 互換用。運用の正本ではない。

---

## 対応する主な操作

- `capture`
- `distill`
- `moc`
- `ask`
- `search`
- `quiz`
- `quiz-answer`
- `knowledge-file-audit`
- `monthly-learning-review`
- `journal`
- `prep-note-save`
