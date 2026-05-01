---
name: knowledge-file-audit
description: Use when auditing files in the local knowledge-base repository for correctness, source alignment, link integrity, metadata consistency, or factual accuracy; always cite local evidence and primary sources before judging or proposing changes.
---

# Knowledge File Audit Skill

対象リポジトリ:
- `/Users/miyary777/workspace/miyaRY777/knowledge-base`

対象ファイル:
- `knowledge/notes/**/*.md`
- `knowledge/maps/**/*.md`
- `knowledge/inbox/**/*.md`
- `knowledge/reference/**/*.md`
- 必要に応じて `.codex/skills/knowledge-base/` と `AGENTS.md`

## 目的

knowledge-base に保存されているノート、MOC、参照メモ、inbox が、根拠と一次ソースに照らして正しいか確認する。

## 最重要ルール

- 推測で正しいと判断しない
- 根拠になったローカルファイルを必ず示す
- 技術的・仕様的な主張は、必ず一次ソースを確認する
- 一次ソースを確認できない主張は `一次ソース未確認` と明記する
- ノート本文はコピペせず、自分の言葉で要約する
- 書き込み系の操作は、保存前に修正案を提示して確認する

## 一次ソースの扱い

一次ソースとして優先するもの:

- 公式ドキュメント
- 公式 API リファレンス
- 公式仕様書、RFC、標準化団体の文書
- 公式リポジトリ、公式 changelog、公式 release notes
- 製品やライブラリの作者・運営元が公開する資料

一次ソースとして扱わないもの:

- 個人ブログ
- Qiita、Zenn、dev.to などの記事
- Stack Overflow、Reddit、SNS
- ChatGPT など AI からの回答
- 公式ではないまとめ記事

補助資料として使ってよいが、正誤判断の根拠にはしない。

## 代表的な一次ソース

- Ruby: Ruby 公式リファレンス、Ruby docs、ruby/ruby
- Rails: Rails Guides、Rails API、rails/rails
- Hotwire / Turbo / Stimulus: hotwired.dev、公式 GitHub
- SQL / DB: 対象 DB の公式 docs、SQL 標準に近い話は仕様や公式資料
- PostgreSQL: postgresql.org docs
- MySQL: dev.mysql.com docs
- SQLite: sqlite.org docs
- Web / HTTP / Cookie: RFC、WHATWG、W3C、MDN は補助。MDN のみで断定しない
- Security: OWASP、RFC、ベンダー公式 docs
- Git: git-scm.com docs

## 監査手順

1. 対象ファイルを読む
   - `source:`、`Links`、`Tags`、`review_log`、本文、Example、Action を確認する
2. ローカル根拠を追う
   - `source:` が指す inbox や関連ノートを確認する
   - `Links` の関連ノートを必要な範囲だけ確認する
3. 主張を分解する
   - 用語定義
   - 挙動
   - 実務上の注意
   - コード例
   - 推奨・非推奨
4. 一次ソースで検証する
   - 最新性が関係する場合は必ず公式情報を確認する
   - 公式資料が複数ある場合は、対象技術に最も近い公式資料を優先する
5. 判定する
   - `正しい`
   - `概ね正しいが補足が必要`
   - `誤りまたは誤解を招く`
   - `一次ソース未確認`
6. 修正が必要なら案を出す
   - 変更対象ファイル
   - 変更理由
   - 修正文案
   - 根拠ファイル
   - 一次ソース
   - 保存確認

## チェック観点

### 内容の正確性

- ローカルメモから飛躍していないか
- 公式仕様や公式 docs と矛盾していないか
- 「常に」「必ず」「できない」など強い表現が妥当か
- コード例が実際の挙動と合っているか

### メタデータ

- `id` とファイル名が対応しているか
- `title` が本文内容と合っているか
- `created` と `source` が妥当か
- `Tags` が内容に合っているか
- `#要復習` の数と `review_log` の件数が一致しているか

### リンク

- `source:` の参照先が存在するか
- `Links` の参照先が存在するか
- MOC のリンク先が内容と合っているか
- 同一概念の重複ノートがないか

### 表現

- 初学者向けに誤解しにくいか
- 断定が強すぎないか
- 具体例が本文の主張を正しく支えているか

## 出力形式

通常は次の順で返す。

```markdown
## 結論
- 判定:
- 要約:

## 根拠ファイル
- `path/to/file.md`: 確認した内容

## 一次ソース
- 公式資料名: URL または参照先

## 指摘
- 重大度:
- 対象:
- 内容:
- 理由:

## 修正案
- 対象ファイル:
- 修正文案:
- 保存確認:
```

問題がない場合も、確認した根拠ファイルと一次ソースを示す。

## 書き込み時

- `distill` や `moc` と同じく、保存前に必ず案を見せる
- `#要復習` と `review_log` の修正は `scripts/review_tag_sync.rb` を優先する
- ユーザーが保存を承認した後だけファイルを変更する

