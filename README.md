# knowledge-base

Claude Code を活用した「外部脳」ナレッジベース。
情報を **探せる・信じられる・使える** 状態に整理する。

---

## ディレクトリ構造

```
knowledge-base/
├── knowledge/
│   ├── inbox/       # 🧲 COLLECT: Raycastメモなどの生データ
│   │   └── done/    # distill済みのメモ
│   ├── notes/       # 📝 DISTILL: アトミックノート（1ノート1アイデア）
│   ├── maps/        # 🔗 CONNECT: MOC（テーマ別索引）
│   └── projects/    # 🎯 USE: 案件・プロジェクトフォルダ
├── .claude/
│   └── commands/    # Slash Commands
├── BACKLOG.md       # 追加したい機能・改善アイデア
└── README.md
```

---

## 使い方（CODEサイクル）

### 1. Collect — 情報を集める
Raycastなどで書いたメモを inbox に取り込む。

```
/capture rails-study    → inbox にファイルを生成
```

または Raycast のメモを `knowledge/inbox/YYYY-MM-DD_insight_{title}.md` に直接コピペ。

### 2. Distill — 要点を抽出する（週2回・各15分）
```
/distill 2026-04-01_insight_rails-study.md
```
→ 1ノート1アイデアのアトミックノートに分割 → `knowledge/notes/` に保存
→ 元ファイルを `inbox/done/` に移動

### 3. Connect — つなぐ
```
/moc rails-basics           → Rails基礎の索引を生成
/moc rails-basics --update  → 既存MOCを更新
```

### 4. Use — 使う
```
/ask Callbacksの注意点は？        → 根拠リンク付きで回答
/ask #rails タグのノートは？      → タグ検索
/search before_create             → キーワード全文検索
/quiz                             → ランダムに1問出題
/quiz --today-only                → 当日に学んだノートだけ復習
/quiz #rails 5問                  → タグ絞り込みで5問連続
/quiz --yesterday                 → 前日に学んだノートだけ復習
/quiz #要復習                     → 間違えた問題だけ復習
/weekly-review                    → 週次振り返り
```

---

## コマンド一覧

| コマンド | 説明 |
|---------|------|
| `/capture <title>` | inboxにメモファイルを生成 |
| `/distill <file>` | inboxメモをアトミックノートに分割 |
| `/moc <theme>` | テーマ別MOC（索引）を生成・更新 |
| `/ask <question>` | ナレッジベースを検索して根拠付きで回答 |
| `/search <keyword>` | キーワードで全文検索 |
| `/quiz [#tag] [N問]` | クイズ形式で復習（間違え管理付き） |
| `/weekly-review` | 週次の棚卸しと振り返り |
| `ruby scripts/review_tag_sync.rb --note PATH --action wrong|correct|check --date YYYY-MM-DD` | `#要復習` と `review_log` の補助更新 |

---

## quiz の運用

- 当日に学んだ内容は、その日のうちにクイズで復習する
- 翌日は前日に学んだ内容をもう一度復習する
- `#要復習` が付いたノートは別枠で復習する
- `#要復習` は間違えるたびに重複して追加してよい
- その日に追加した `#要復習` は、その日のうちには外さない
- 翌日以降に正解したときだけ、最古の `#要復習` を 1 個外す

---

## 運用ルール

- **1 Note, 1 Idea**: 1ノートに1つのアイデア
- **自分の言葉**: コピペ禁止、要約して記述
- **週2回15分**: `/distill` で inbox を整理
- **使えば賢くなる**: `/ask` や `/quiz` の結果をノートに書き戻す
- **完璧より回す**: 溜めすぎず、こまめに流す
- **capture を軽く保つ**: 生メモはテンプレに沿って inbox へ保存し、整理は distill で行う
- **done は確認後**: notes 保存と最低限の Links 整理を確認してから inbox/done に移す
- **MOC は distill の直後に確認**: 新しい概念群が既存テーマに入るなら、その場で更新候補を見る

---

## タグ一覧（例）

| タグ | 用途 |
|------|------|
| `#rails` | Rails関連 |
| `#activerecord` | ActiveRecord関連 |
| `#database` | DB・SQL関連 |
| `#http` | HTTP・API関連 |
| `#cs-basics` | CS基礎知識 |
| `#要復習` | クイズで間違えた問題（重複可・review_log と同期） |
