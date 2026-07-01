# knowledge-base 日次フロー

## メインフロー

通常運用は PREPノート保存を起点にする。

1. PREPノートを受け取る
2. 既存ノート・MOC と重複確認する
3. Tags / Links / 保存案を確認する
4. `knowledge/notes/` に保存する
5. 関連 MOC を作成または更新する
6. 当日の日誌へ追記する
7. `quiz` で復習する

## 生メモの補助フロー

未整理のメモ、Raycast の雑メモ、複数概念が混ざった貼り付けは `capture -> distill -> done` で扱う。

1. `capture` で生メモを `knowledge/inbox/` に保存する
2. 保存した inbox メモを `distill` の入力にする
3. `distill` で 1 ノート 1 アイデアに分けて `knowledge/notes/` に保存する
4. done に移す前に、保存内容と最低限の Links 整理を確認する
5. distill 済みの inbox メモを `knowledge/inbox/done/` に移す
6. 必要なら関連テーマの MOC を更新する

## capture

- 保存先は `knowledge/inbox/`
- ファイル名は `YYYY-MM-DD_insight_{title}.md`
- 本文は生メモのまま保存する
- 1 ファイルに複数概念が入っていてよい
- 入力テンプレートは `タイトル / 日時 / 元メモ / 関連タグ候補` を基本にする

テンプレート例:

```markdown
# タイトル

**日時**: 2026-04-09
**元メモ**: Raycast
**関連タグ候補**: #frontend #stimulus

---

ここに生メモをそのまま入れる
```

例:

- `knowledge/inbox/2026-04-09_insight_stimulus-classes-api.md`

## distill

- PREPノートは原則 distill しない
- 1つのPREPノートに複数の独立した概念が混ざっている場合だけ分解する
- inbox メモを読み、概念ごとに分割する
- 既存 `knowledge/notes/` と重複しないか確認する
- 完全重複なら既存ノート更新を優先する
- 保存前にノート案を確認する
- 新しい概念群を追加したら、関連 MOC の更新候補があるか確認する

例:

- 1 つの inbox メモから
  `entry-point`
  `css-entry`
  `build-output`
  `stimulus-classes-property-api`
  の 4 ノートに分ける

## done

- notes 保存後、元の inbox ファイルを `knowledge/inbox/done/` に移す
- 移動前に notes 保存済みか確認する
- 移動前に保存内容を確認済みか確認する
- 関連ノートへの `Links` 整理が必要なら done 前に済ませる
- 移動したファイル名を記録または報告する

例:

- `knowledge/inbox/2026-04-09_insight_stimulus-classes-api.md`
- `knowledge/inbox/done/2026-04-09_insight_stimulus-classes-api.md`

## MOC 更新の目安

- PREPノート保存後、関連 MOC を確認する
- 既存 MOC に入るなら、保存したノートへのリンクを追加する
- 新しい概念群が既存テーマに入るなら、distill 直後にも関連 MOC を確認する
- 明らかに既存マップへ足せる内容なら、更新候補を先に作る
- 新テーマなら MOC 新規作成は後回しでもよい

## テンプレートの使い分け

- AIにPREPノートを作らせるときは `knowledge/templates/template-prep-prompt.md` を使う
- 手動でノートを作るとき、または完成形を確認するときは `knowledge/templates/template-note.md` を使う
- どちらも `## 言語化` は8項目の理解チェックにそろえる

## 迷ったときの判断

- PREPノートを保存したいなら `prep-note-save`
- 生メモの保存だけなら `capture`
- 生メモをノート化したいなら `distill`
- ノート化が終わった元メモ整理なら `done`
- テーマ横断で整理したいなら `moc`
