# Web Developer Bootcamp 学習設計

## 概要

Udemy「The Web Developer Bootcamp 完全日本語版」をハンズオン形式で進めるための学習環境・ワークフロー設計。

- **教材:** The Web Developer Bootcamp 完全日本語版（全74セクション）
- **現在地:** セクション18まで完了（HTML/CSSは穴抜けあり）
- **目標:** 全74セクションを完走する
- **AI連携:** ペアプログラミング・質問・クイズ形式の復習

---

## 環境構成

### コーディング環境

ローカルsandboxディレクトリを使用。リポジトリ作成・環境構築は不要。

```
~/sandbox/web-dev-bootcamp/
├── s01-s13-html-css/      # HTML・CSS基礎（穴抜けで学習済み）
├── s14-s25-javascript/    # JavaScript基礎〜DOM（現在進行中）
├── s26-s29-async/         # 非同期・AJAX・OOP
├── s30-s38-nodejs/        # Node.js・Express・MongoDB・Mongoose
├── s39-s59-yelpcamp/      # YelpCamp大型プロジェクト
└── s60-s73-react/         # React編
```

- Claude Codeは `~/sandbox/web-dev-bootcamp/` で起動して使う
- Reactセクション（s60）に入ったタイミングで `npx create-next-app@latest` を実行

### knowledge-base連携

学んだ内容はこのknowledge-baseに蓄積する。

```
/capture → /distill → /quiz
```

---

## セクション構成

| フォルダ | セクション | 内容 |
|----------|-----------|------|
| s01-s13-html-css | s1〜s13 | HTML・CSS・Flexbox・Bootstrap |
| s14-s25-javascript | s14〜s25 | JS基礎・配列・オブジェクト・DOM |
| s26-s29-async | s26〜s29 | 非同期・AJAX・API・OOP |
| s30-s38-nodejs | s30〜s38 | Node.js・Express・MongoDB・Mongoose |
| s39-s59-yelpcamp | s39〜s59 | YelpCamp（CRUD・認証・デプロイ） |
| s60-s73-react | s60〜s73 | React・JSX・State・useEffect |

---

## 1セッションのワークフロー

1. **動画を見る** — 手を動かしたいところでポーズ
2. **Claude Codeを起動** — `~/sandbox/web-dev-bootcamp/` で起動
3. **コードを書く** — Claudeとペアプログラミング
4. **わからない点はその場で質問** — Claudeに解説してもらう
5. **セクション終わりに `/capture` でメモ** — knowledge-baseに蓄積
6. **`/quiz` で復習** — 間違えた問題は `#要復習` タグで管理

---

## AI連携の使い方

| シーン | やること |
|--------|---------|
| コードを書くとき | Claudeと一緒に考えながら書く |
| わからないとき | その場でClaudeに質問 |
| セクション終わり | `/quiz` でClaudeに問題を出してもらう |
| 週次 | `/weekly-review` で振り返り |
