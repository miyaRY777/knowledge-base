# knowledge-base Workflows

このファイルを knowledge-base の運用ルールの正本とする。
`README.md`、`AGENTS.md`、`SKILL.md`、`CLAUDE.md` には入口と参照先だけを置き、詳細ルールはここへ集約する。

## Main Workflow

通常運用のメインは PREPノート保存ループとする。

```text
PREPノート
-> 重複確認
-> Tags / Links / 保存案
-> notes保存
-> MOC作成・更新
-> 日誌追記
-> quiz
```

## CODE

現在の主導線は PREPノート保存ループとする。CODE は通常の生メモを扱うための補助ループとして使う。

1. Collect
   inbox にメモを取り込む
2. Distill
   inbox から atomic note を作る
3. Connect
   notes をまとめる MOC を作る
4. Use
   ask、search、quiz、monthly-learning-review で再利用する

## capture

- `YYYY-MM-DD_insight_{short-title}.md` を `knowledge/inbox/` に作る
- テンプレートは最小限にする
- ファイル名の日付は実行日を使う

## distill

- PREPノートは原則として distill しない
- 1つのPREPノートに複数の独立した概念が混ざっている場合だけ分解する
- inbox を読む
- アイデアをカテゴリ分けする
- 重複チェックをする
- 同一概念なら新規作成より既存ノート更新を優先する
- 別観点なら別ノートにしつつ `Links` でつなぐ
- ノート案を見せてから保存する
- 保存後、元の inbox ファイルを `knowledge/inbox/done/` に移動するか提案する

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
- 出題文は `title` だけで作らず、`背景`、`結論`、`理由`、`具体例`、`言語化` など本文全体を見て自然な問題文にする
- フェーズ制を採用する（フロントマターの `quiz_phase` で管理）
  - Phase 1（4択）: A〜Dから選ぶ。`quiz_streak` が2で次回セッションから Phase 2 へ昇格
  - Phase 2（説明）: 概念・重要な場面・実務での扱いまで自由記述。`quiz_fail_streak` が2で Phase 1 に降格
- `#要復習` の操作は Phase 2 のみ行う
  - Phase 2 不正解・スキップ → `#要復習` を追加
  - Phase 2 正解1回 → `#要復習` を削除
  - Phase 1 では不正解・スキップでも `#要復習` を付けない
- `#要復習` を保存するときは、対象ノートと変更内容を示して確認を取る
- `quiz_fail_log` は間違えた日付の累計リストとして扱い、リセットしない
- `fail=1`、`fail>=2`、`fail-in:YYYY-MM` などの絞り込み指定がある場合は、`quiz_fail_log` を根拠に対象を絞る

### 出題形式（Phase 1）

- 問題文にトピック名を含めてよい
- **選択肢にトピック名（問われている用語）を含めない**（答えが丸見えになるため）
- コード系トピック → 穴埋め形式
  ```
  Q. 次のコードの ___ に入る属性の説明として正しいものはどれですか？
  <p ___="highlight">重要</p>
  ```
- 概念系トピック → シナリオ形式
  ```
  Q. 「〜したい場合」に使う概念の説明として正しいものはどれですか？
  ```

### 解説形式

- 正解・不正解にかかわらず毎回「解説 ＋ 具体例（コード例・数値例）」をセットで出す

## weekly-review

- 実装済みだが、現在は未運用。通常は monthly-learning-review を優先する
- inbox の棚卸し
- 直近 7 日のノート集計
- MOC の Open Questions 整理
- 来週のアクション提案

## knowledge-file-audit

- 対象ノートや MOC の正確性、リンク整合性、メタデータを監査する
- 推測で正しいと判断しない
- 根拠になったローカルファイルを必ず示す
- 技術的・仕様的な主張は一次ソースを確認する
- 一次ソースを確認できない主張は `一次ソース未確認` と明記する
- 修正が必要な場合は、保存前に修正案を提示して確認する

## monthly-learning-review

- 対象月の `knowledge/inbox/`、`knowledge/notes/`、`knowledge/maps/` を確認する
- 月次 MOC 名は `map-YYYY-MM-learning.md`
- 保存先は `knowledge/maps/monthly/`
- 既存ファイルがあれば更新を優先する
- 今月のテーマは 3〜6 個にまとめる
- 重要概念は 5〜8 件程度に絞る
- 未決事項は次月に持ち越したい論点だけを書く
- 生成案を表示し、承認後に保存する

## content-save

ユーザーがコンテンツを貼り付けて「保存したい」と言ったとき:

1. 分類する
   - 単一概念: `knowledge/notes/` にアトミックノート
   - 複数トピック・図・全体フロー: `knowledge/maps/` に MOC
   - 未整理の生メモ: `knowledge/inbox/` に保存して後で distill
2. 既存ノート・MOC と重複確認する
3. 既存ありの場合は補強か新規かをユーザーに確認する
4. 保存案をユーザーに確認してから作成する
5. 関連ファイルへのリンクを追加する

## prep-note-save

PREP プロンプトで生成した学習ノートを保存する場合:

- 生成依頼には `knowledge/templates/template-prep-prompt.md` を使う
- 手動作成や完成形確認には `knowledge/templates/template-note.md` を使う
- 重複確認をする
- 内容から Tags を提案して確認する
- 保存案を確認してから作成する
- 保存先は `knowledge/notes/note-insight-{topic}.md`
- `## 言語化` は8項目の理解チェックとして空欄のまま残し、復習時に埋める
- 関連ノートへの Links を追加する
- 保存後、関連 MOC を確認する
- 既存 MOC があれば、保存したノートへのリンクを追加する
- 該当 MOC がなく、関連ノートが複数ある場合は、新規 MOC 作成を提案する
- 関連ノートが少ない場合は MOC 候補として扱い、無理に新規 MOC を作らない
- 保存後、当日の日誌 `knowledge/inbox/YYYY-MM-DD_journal.md` を作成または更新し、`今日学んだこと` にノート用セクションを追加する

## journal

- PREPノート保存時は、当日の日誌を作成または更新して `今日学んだこと` にノート用セクションを追加する
- ユーザーが「今日の日誌を作って」と依頼した場合も、その日作成・更新したノートを確認して日誌を作成または更新する
- 保存先は `knowledge/inbox/YYYY-MM-DD_journal.md`
- `結論`、`理由`、`具体例`、`まとめ` は必ず空白のままにする
