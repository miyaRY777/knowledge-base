# knowledge-base

Claude Code を活用した「外部脳」ナレッジベース。
情報を **探せる・信じられる・使える** 状態に整理する。

---

## 入口

- ナレッジ本体を見る: `knowledge/`
- 運用ドキュメントを見る: `knowledge/reference/`
- Codex 用の運用ルールを見る: `AGENTS.md`
- review 補助スクリプトを見る: `scripts/review_tag_sync.rb`

---

## ディレクトリ構造

```text
knowledge-base/
├── README.md
├── AGENTS.md                # Codex 用の運用ルール
├── .claude/                 # Claude 用設定
│   ├── agents/
│   └── commands/
├── .codex/                  # Codex 用設定
│   └── skills/
├── docs/                    # 補助ドキュメント・superpowers 用資料
│   └── superpowers/
├── scripts/                 # 運用補助スクリプト
├── test/                    # スクリプトのテスト
└── knowledge/
    ├── inbox/               # 🧲 COLLECT: Raycastメモなどの生データ
    │   └── done/            # distill済みのメモ
    ├── notes/               # 📝 DISTILL: アトミックノート（1ノート1アイデア）
    ├── maps/                # 🔗 CONNECT: MOC（テーマ別索引）
    ├── projects/            # 🎯 USE: 案件・プロジェクトノート
    ├── reference/           # 運用説明・手順・ルール
    └── .obsidian/           # Obsidian 設定
```

---

## 役割分担

- `knowledge/`: 学習内容そのものを置く
- `knowledge/reference/`: knowledge-base の運用手順やルールを置く
- `docs/`: ナレッジ本体とは別の補助資料を置く
- `.claude/` と `.codex/`: エージェントごとの設定を分けて持つ
- `scripts/` と `test/`: review 更新などの運用を支える

---

## 使い方（CODEサイクル）

### 1. Collect — 情報を集める
Raycast などで書いたメモを inbox に取り込む。

```text
/capture rails-study    → inbox にファイルを生成
```

または Raycast のメモを `knowledge/inbox/YYYY-MM-DD_insight_{title}.md` に直接コピペ。

### 2. Distill — 要点を抽出する

```text
/distill 2026-04-01_insight_rails-study.md
```

1ノート1アイデアのアトミックノートに分割して `knowledge/notes/` に保存し、元ファイルを `knowledge/inbox/done/` に移す。

### 3. Connect — つなぐ

```text
/moc rails-basics
/moc rails-basics --update
```

テーマ別の MOC を作成・更新する。

### 4. Use — 使う

```text
/ask Callbacksの注意点は？
/search before_create
/quiz
/quiz #要復習
/weekly-review
```

学習済みノートを検索し、クイズや週次レビューで再利用する。

---

## コマンド一覧

| コマンド | 説明 |
|---------|------|
| `/capture <title>` | inbox にメモファイルを生成 |
| `/distill <file>` | inbox メモをアトミックノートに分割 |
| `/moc <theme>` | テーマ別 MOC（索引）を生成・更新 |
| `/ask <question>` | ナレッジベースを検索して根拠付きで回答 |
| `/search <keyword>` | キーワードで全文検索 |
| `/quiz [#tag] [N問]` | クイズ形式で復習（間違え管理付き） |
| `/weekly-review` | 週次の棚卸しと振り返り |
| `ruby scripts/review_tag_sync.rb --note PATH --action wrong|correct|check --date YYYY-MM-DD` | `#要復習` と `review_log` の補助更新 |

---

## 主要ファイル

| パス | 用途 |
|------|------|
| `README.md` | 人間向けの入口 |
| `AGENTS.md` | Codex 向けの運用ルール |
| `knowledge/reference/knowledge-base-doc-index.md` | knowledge-base 内の運用資料の入口 |
| `scripts/review_tag_sync.rb` | `#要復習` と `review_log` の同期補助 |

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
- **使えば賢くなる**: `/ask` や `/quiz` の結果をノートに書き戻す
- **完璧より回す**: 溜めすぎず、こまめに流す
- **capture を軽く保つ**: 生メモはテンプレに沿って inbox へ保存し、整理は distill で行う
- **done は確認後**: notes 保存と最低限の Links 整理を確認してから `knowledge/inbox/done/` に移す
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
