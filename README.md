# knowledge-base

Claude Code を活用した「外部脳」ナレッジベース。
情報を **探せる・信じられる・使える** 状態に整理する。

---

## ディレクトリ構造

```
knowledge-base/
├── knowledge/
│   ├── inbox/       # 🧲 COLLECT: 生の議事録・メモ
│   ├── notes/       # 📝 DISTILL: アトミックノート
│   ├── maps/        # 🔗 CONNECT: MOC（索引）
│   └── projects/    # 🎯 USE: 案件フォルダ
└── .claude/
    ├── commands/    # Slash Commands
    └── agents/      # Subagents
```

---

## 使い方（CODE サイクル）

### 1. Collect — 情報を集める
```
/capture MTG    → 議事録テンプレートを inbox に生成
/capture idea   → アイデアメモを inbox に生成
```

### 2. Distill — 要点を抽出する
```
/distill 2025-01-01_meeting.md    → アトミックノートに分割
```

### 3. Connect — つなぐ
```
/moc decisions        → 意思決定の索引を生成・更新
/moc risks            → リスクの索引を生成・更新
/moc project-overview → プロジェクト全体像の索引を生成
```

### 4. Use — 使う
```
/ask 今月の主な意思決定は？
/ask このプロジェクトのリスクは何？
/weekly-review        → 週次棚卸し
```

---

## コマンド一覧

| コマンド | 説明 |
|---|---|
| `/capture <title>` | 30秒でinboxにメモを追加 |
| `/distill <file>` | inboxメモをアトミックノートに分割 |
| `/moc <theme>` | テーマ別MOC（索引）を生成・更新 |
| `/ask <question>` | ナレッジベースを検索して根拠付きで回答 |
| `/weekly-review` | 週次の棚卸しとサマリー生成 |

---

## 運用ルール

- **1 Note, 1 Idea**: 1ノートに1つのアイデア
- **自分の言葉**: コピペ禁止、要約して記述
- **週2回15分**: `/distill` で inbox を整理
- **使えば賢くなる**: `/ask` の結果をノートに書き戻す
