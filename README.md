# knowledge-base

学習メモを **探せる・信じられる・使える** 状態に育てるためのナレッジベース。
運用の基本は `Collect → Distill → Connect → Use` の CODE サイクル。

---

## 入口

| 目的 | 場所 |
|------|------|
| 生メモを置く | `knowledge/inbox/` |
| アトミックノートを見る | `knowledge/notes/` |
| テーマ別マップを見る | `knowledge/maps/` |
| Codex の運用ルールを見る | `AGENTS.md` |
| knowledge-base スキルを見る | `.codex/skills/knowledge-base/SKILL.md` |
| 既存の運用資料を見る | `knowledge/reference/` |

---

## ディレクトリ構造

```text
knowledge-base/
├── README.md
├── AGENTS.md
├── .codex/
│   └── skills/knowledge-base/
├── .claude/
├── docs/
├── scripts/
├── test/
└── knowledge/
    ├── inbox/      # Collect: 生メモ
    ├── notes/      # Distill: 1ノート1アイデア
    ├── maps/       # Connect: MOC / テーマ別索引
    ├── projects/   # Use: 案件・プロジェクトノート
    ├── resources/  # 参照用ストック
    └── reference/  # 運用説明
```

---

## CODE サイクル

### 1. Collect

メモを `knowledge/inbox/` に保存する。

ファイル名:

```text
YYYY-MM-DD_insight_{short-title}.md
```

### 2. Distill

inbox のメモを読み、1ノート1アイデアの atomic note として `knowledge/notes/` に分ける。

ルール:
- 既存ノートとの重複を確認する
- 完全に同じ概念なら既存ノート更新を優先する
- 似ているが観点が違う場合は別ノートにして Links でつなぐ
- 保存前に案を確認する

### 3. Connect

関連する notes を `knowledge/maps/` の MOC にまとめる。

MOC には、サマリー、セクション、Open Questions、関連リンクを含める。
MOC も保存前に案を確認する。

### 4. Use

検索、質問、クイズ、週次レビューで再利用する。

```bash
python3 .codex/skills/knowledge-base/scripts/kb_tool.py search callback
python3 .codex/skills/knowledge-base/scripts/kb_tool.py ask "Callbacksの注意点は？"
python3 .codex/skills/knowledge-base/scripts/kb_tool.py quiz --yesterday --level 2
python3 .codex/skills/knowledge-base/scripts/kb_tool.py weekly-review
```

---

## 主要 MOC

| MOC | テーマ |
|-----|--------|
| `knowledge/maps/map-web-security-basics.md` | Webセキュリティ、HTTPS、TLS、2FA |
| `knowledge/maps/map-cyber-attack-basics.md` | サイバー攻撃の種類 |
| `knowledge/maps/map-cookie-basics.md` | Cookie の基本と属性 |
| `knowledge/maps/map-session-basics.md` | セッション、セッションID、期限、攻撃 |
| `knowledge/maps/map-http-client-basics.md` | HTTP通信、Fetch、Axios |
| `knowledge/maps/map-activerecord-query-basics.md` | ActiveRecord、SQL、N+1 |
| `knowledge/maps/map-ruby-rails-predicate-basics.md` | `nil?`、`empty?`、`blank?`、`presence` |
| `knowledge/maps/map-rails-basics.md` | Rails 基礎 |
| `knowledge/maps/map-stimulus-basics.md` | Stimulus 基礎 |
| `knowledge/maps/map-computer-architecture-basics.md` | コンピュータ構成 |

---

## クイズ運用

クイズ対象は基本的に `knowledge/notes/` の atomic note。

対象の選び方:
- 今日学んだノート
- 昨日学んだノート
- `#要復習` のノート
- タグ指定したノート

出題レベル:

| レベル | 形式 |
|--------|------|
| 1 | 1問1答。用語や要点を1〜2文で短く答える |
| 2 | 中間形式。概念と重要になる場面を説明する |
| 3 | 総合説明。概念、場面、実務やコードでの扱いまで説明する |

例:

```bash
python3 .codex/skills/knowledge-base/scripts/kb_tool.py quiz --today-only --level 1
python3 .codex/skills/knowledge-base/scripts/kb_tool.py quiz --yesterday --level 2
python3 .codex/skills/knowledge-base/scripts/kb_tool.py quiz --tag 要復習 --level 3
```

採点後の扱い:
- `惜しい`、`不正解`、`スキップ` は `#要復習` を付ける
- `#要復習` を保存するときは対象ノートと変更内容を確認する
- `#要復習` は日をまたいだ2回連続正解で外す
- 同じ日に何度正解しても `review_streak` は最大1までとする

---

## 運用ルール

- 推測で埋めない
- 根拠となるノートやファイルを示す
- 書き込み系の操作は保存前に案を確認する
- ノート本文はコピペせず、自分の言葉で要約する
- 重複メモは許容するが、distill 時に重複ノートの統合を検討する
- inbox は軽く保ち、整理は distill で行う
- MOC は新しい概念群が増えたタイミングで更新候補を見る

---

## タグ例

| タグ | 用途 |
|------|------|
| `#rails` | Rails |
| `#activerecord` | ActiveRecord |
| `#database` | DB / SQL |
| `#http` | HTTP / API |
| `#web` | Web 基礎 |
| `#security` | セキュリティ |
| `#cookie` | Cookie |
| `#session` | セッション |
| `#javascript` | JavaScript |
| `#要復習` | クイズで復習が必要なノート |
