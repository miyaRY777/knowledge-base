# 最重要ルール

- 推測で埋めない
- 根拠となるノートやファイルを示す
- 書き込み系の操作は保存前に案を確認する
- ノート本文はコピペせず、自分の言葉で要約する
- 重複メモは許容するが、重複ノートは `distill` 時に統合を検討する

---

# Codex 入口

- Claude 用設定は `./.claude/` に残す
- Codex 用設定は `./.codex/` に置く
- knowledge-base を扱うときは `./.codex/skills/knowledge-base/SKILL.md` を参照する

---

# 運用の基本

## CODE サイクル

1. Collect
2. Distill
3. Connect
4. Use

## 再現している操作

- `capture`
- `distill`
- `moc`
- `ask`
- `search`
- `quiz`
- `weekly-review`

## 役割

- `knowledge-qa`
- `note-distiller`
- `moc-builder`

## 重複時の判断

- Raycast や inbox では重複を気にしすぎなくてよい
- `distill` では既存ノートとの重複を確認する
- 完全に同じ概念なら新規作成より既存ノート更新を優先する
- 似ているが観点が違う場合は、別ノートにして `Links` でつなぐ
- 判断に迷う場合は、新規保存の前に統合案を出す
