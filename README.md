# knowledge-base

学習メモを **探せる・信じられる・使える** 状態に育てるためのナレッジベース。
運用の主導線は PREP 形式の学習ノートを保存し、MOC・日誌・quiz へつなげるループ。
`Collect -> Distill -> Connect -> Use` の CODE サイクルは、通常の生メモを扱う補助ループとして使う。

---

## 読む順番

| 目的 | 参照先 |
|------|--------|
| 全体像をつかむ | `README.md` |
| Codex の最重要ルール | `AGENTS.md` |
| 運用ルールの正本 | `.codex/skills/knowledge-base/references/workflows.md` |
| パス・検索対象 | `.codex/skills/knowledge-base/references/paths.md` |
| 出力テンプレート | `.codex/skills/knowledge-base/references/templates.md` |
| Codex skill 入口 | `.codex/skills/knowledge-base/SKILL.md` |
| Claude 互換入口 | `CLAUDE.md` |

詳細な保存フロー、PREPノート、日誌、quiz、月次レビューのルールは `workflows.md` を正本とする。

---

## ディレクトリ構造

```text
knowledge-base/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── BACKLOG.md
├── .codex/       # Codex 用エージェント・スキル
├── .claude/      # Claude 用エージェント・コマンド互換
├── docs/         # 計画・仕様メモ
├── test/         # kb_tool 関連テスト
└── knowledge/
    ├── inbox/      # Collect: 生メモ・日誌
    ├── notes/      # Distill: 1ノート1アイデア
    ├── maps/       # Connect: MOC / テーマ別索引
    ├── projects/   # Use: 案件・プロジェクトノート（ローカル管理）
    ├── resources/  # 参照用ストック
    ├── reference/  # 人間向け運用説明
    ├── templates/  # 学習テンプレート
    └── .obsidian/  # Obsidian 設定（Git 管理外）
```

---

## 主要ループ

```text
PREPノート
-> 重複確認
-> Tags / Links / 保存案
-> notes保存
-> MOC作成・更新
-> 日誌追記
-> quiz
```

MOC は毎回新規作成せず、既存 MOC 更新を基本にする。該当 MOC がなく、関連ノートが複数ある場合だけ新規作成を提案する。

通常の生メモは `capture -> distill -> moc -> ask/search/quiz` の流れで扱う。PREPノートは原則 distill せず、複数の独立した概念が混ざっている場合だけ分解する。

---

## テンプレートの使い分け

| ファイル | 役割 |
|---|---|
| `knowledge/templates/template-prep-prompt.md` | Claude などに PREP 形式の学習ノートを作らせるための指示 |
| `knowledge/templates/template-note.md` | 手動で学習ノートを作るとき、または完成形を確認するときのひな形 |

どちらも `## 言語化` は同じ8項目の理解チェックにそろえる。

---

## よく使うコマンド

```bash
python3 .codex/skills/knowledge-base/scripts/kb_tool.py search callback
python3 .codex/skills/knowledge-base/scripts/kb_tool.py ask "Callbacksの注意点は？"
python3 .codex/skills/knowledge-base/scripts/kb_tool.py quiz --tag rails --count 3
python3 .codex/skills/knowledge-base/scripts/kb_tool.py quiz-answer note-insight-active-record-callbacks "C" --correct-choice C --write
```

コマンドの詳細と運用判断は `.codex/skills/knowledge-base/references/workflows.md` を確認する。
