# knowledge-base プロジェクト設定

## 最重要ルール

- 推測で埋めない
- 根拠となるノートやファイルを示す
- 書き込み系の操作は保存前に案を確認する
- 複数ファイルを一括作成する場合は、まとめて作成してから1回確認する
- ノート本文はコピペせず、自分の言葉で要約する
- 重複メモは許容するが、重複ノートは `distill` 時に統合を検討する

---

## 運用の基本

### CODE サイクル

1. Collect — inbox にメモを取り込む
2. Distill — inbox からアトミックノートを作る
3. Connect — notes をまとめる MOC を作る
4. Use — ask、search、quiz、weekly-review で再利用する

### 対応する操作

- `/capture` — inbox にメモファイルを生成
- `/distill` — inbox をアトミックノート化
- `/moc` — テーマ別 MOC を生成・更新
- `/ask` — ノートを根拠に質問に回答
- `/search` — ノートを全文検索
- `/quiz` — ノートからクイズ出題
- `/weekly-review` — 週次棚卸し
- `/knowledge-file-audit` — ノートの正確性を監査
- `/monthly-learning-review` — 月次学習マップを作成

### サブエージェント

- `knowledge-qa` — ask / 質問回答
- `note-distiller` — distill
- `moc-builder` — moc

---

## 重複時の判断

- Raycast や inbox では重複を気にしすぎなくてよい
- `distill` では既存ノートとの重複を確認する
- 完全に同じ概念なら新規作成より既存ノート更新を優先する
- 似ているが観点が違う場合は、別ノートにして `Links` でつなぐ
- 判断に迷う場合は、新規保存の前に統合案を出す

---

## パス

| 場所 | 用途 |
|------|------|
| `knowledge/inbox/` | 取り込んだ生メモ |
| `knowledge/inbox/done/` | distill 済みの inbox |
| `knowledge/notes/` | アトミックノート |
| `knowledge/maps/` | MOC（索引） |
| `knowledge/projects/` | プロジェクト資料 |

検索優先順: `notes/` → `maps/` → `projects/` → `inbox/`

---

## コンテンツ保存フロー

ユーザーがコンテンツを貼り付けて「保存したい」と言ったとき:

1. **分類する**
   - 単一概念 → `knowledge/notes/` にアトミックノート
   - 複数トピック・図・全体フロー → `knowledge/maps/` に MOC
   - 未整理の生メモ → `knowledge/inbox/` に保存して後で distill

2. **重複確認**
   - 既存ノート・MOC と照合する
   - 既存ありの場合は補強か新規かをユーザーに確認する

3. **保存案をユーザーに確認してから作成する**

4. **関連ファイルへのリンクを追加する**

---

## ノートカテゴリ

- `decision` — 意思決定
- `metric` — 指標・KPI
- `risk` — リスク
- `data` — データ要件
- `open` — 未決事項
- `action` — アクション
- `stakeholder` — ステークホルダーの意見
- `insight` — 分析結果・示唆
