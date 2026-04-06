# knowledge-base Workflows

## CODE

1. Collect
   inbox にメモを取り込む
2. Distill
   inbox から atomic note を作る
3. Connect
   notes をまとめる MOC を作る
4. Use
   ask、search、quiz、weekly-review で再利用する

## capture

- `YYYY-MM-DD_insight_{short-title}.md` を `knowledge/inbox/` に作る

## distill

- inbox を読む
- アイデアをカテゴリ分けする
- 重複チェックをする
- 同一概念なら新規作成より既存ノート更新を優先する
- 別観点なら別ノートにしつつ `Links` でつなぐ
- ノート案を見せてから保存する

## moc

- テーマに沿うノートを集める
- サマリー、セクション、Open Questions、関連リンクを含める
- 保存前に案を見せる

## ask

- 通常質問は notes 優先で検索する
- `#tag` を含むならタグ一覧として返す
- 回答は結論、根拠、補足、次アクションの順にする

## search

- notes、maps、inbox を全文検索する
- 件数と抜粋を出す

## quiz

- 1問ずつ出題する
- 重複出題を避ける
- その日学んだノートを当日に復習する
- 翌日は前日に学んだノートを復習する
- `#要復習` が付いたノートだけをまとめて復習する
- `惜しい` `不正解` `スキップ` は `#要復習` 候補として扱う
- `#要復習` は2回連続で正解したら外す

## weekly-review

- inbox の棚卸し
- 直近 7 日のノート集計
- MOC の Open Questions 整理
- 来週のアクション提案
