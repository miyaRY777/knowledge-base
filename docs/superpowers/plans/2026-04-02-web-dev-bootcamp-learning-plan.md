# Web Developer Bootcamp 学習実行プラン

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Web Developer Bootcamp（全74セクション）をハンズオン形式で、Claude Codeと協力しながら完走する

**Architecture:** ローカルsandbox（`~/sandbox/web-dev-bootcamp/`）でコードを書き、Claude Codeとペアプロ・質問・クイズをしながら進める。学びはknowledge-baseに蓄積する。

**Tech Stack:** HTML, CSS, JavaScript, Node.js, Express, MongoDB, React（コース準拠）

---

## Task 1: 初回セッション立ち上げ（s19から再開）

**Files:**
- Create: `~/sandbox/web-dev-bootcamp/s14-s25-javascript/s19_loops.js`

- [ ] **Step 1: Claude Codeをsandboxディレクトリで起動する**

ターミナルで実行：
```bash
cd ~/sandbox/web-dev-bootcamp
claude
```

- [ ] **Step 2: s19の動画を見てポーズし、演習コードをClaudeと書く**

ファイルを作成して書き始める：
```bash
# Claude Codeに伝える例
「s19 繰り返し処理を学んでいます。forループで1〜10を出力するコードを一緒に書いてください」
```

- [ ] **Step 3: コードを実行して確認する**

```bash
node s14-s25-javascript/s19_loops.js
```

Expected: 1〜10が出力される

- [ ] **Step 4: わからない点をその場でClaudeに質問する**

例：
```
「while と for はどう使い分けますか？」
「break と continue の違いを教えてください」
```

---

## Task 2: セクション完了時のknowledge-base蓄積

**Files:**
- Create: `~/workspace/miyaRY777/knowledge-base/knowledge/inbox/YYYY-MM-DD_insight_s19-loops.md`（`/capture`が自動生成）

- [ ] **Step 1: セクション終わりに `/capture` でメモを作る**

Claude Codeで実行（knowledge-baseディレクトリで）：
```
/capture s19-loops
```

- [ ] **Step 2: 学んだことをメモファイルに書く**

生成されたファイルに自分の言葉で記述する例：
```markdown
## s19 繰り返し処理

- for, while, for...of の使い分け
- break で抜ける、continue でスキップ
- 無限ループに注意（while の終了条件を忘れない）
```

- [ ] **Step 3: `/distill` でアトミックノートに変換する**

```
/distill YYYY-MM-DD_insight_s19-loops.md
```

- [ ] **Step 4: `/quiz` で復習する**

```
/quiz #javascript
```

---

## Task 3: s19〜s25 JavaScript基礎を完走する

**Files:**
- `~/sandbox/web-dev-bootcamp/s14-s25-javascript/` 配下にセクションごとに .js ファイルを作成

各セクションで以下を繰り返す：

- [ ] **s19: 繰り返し処理**
  - `s19_loops.js` を作成
  - for, while, for...of を演習

- [ ] **s20: 関数入門**
  - `s20_functions.js` を作成
  - 関数定義・引数・return を演習

- [ ] **s21: 続・関数**
  - `s21_functions2.js` を作成
  - スコープ・高階関数を演習

- [ ] **s22: 配列のコールバックメソッド**
  - `s22_array_callbacks.js` を作成
  - `map`, `filter`, `reduce`, `find` を演習

- [ ] **s23: モダンなJavaScriptの機能**
  - `s23_modern_js.js` を作成
  - 分割代入・スプレッド・テンプレートリテラルを演習

- [ ] **s24: DOM入門**
  - `s24_dom/index.html` + `s24_dom/app.js` を作成
  - `querySelector`, `addEventListener` を演習

- [ ] **s25: DOMイベント**
  - `s25_dom_events/index.html` + `s25_dom_events/app.js` を作成
  - クリック・キーボードイベントを演習

各セクション終わりに Task 2 のフローで knowledge-base に蓄積する。

---

## Task 4: s26〜s29 非同期・AJAX・OOP

**Files:**
- `~/sandbox/web-dev-bootcamp/s26-s29-async/` 配下にセクションごとに .js ファイルを作成

- [ ] **s26: 卓球得点表（実践）**
  - `s26_scoreboard/index.html` + `app.js` を作成

- [ ] **s27: 非同期なJavaScript**
  - `s27_async.js` を作成
  - Promise, async/await を演習

- [ ] **s28: AJAXとAPI**
  - `s28_ajax/index.html` + `app.js` を作成
  - `fetch()` でAPIを叩く演習

- [ ] **s29: プロトタイプ・クラス・OOP**
  - `s29_oop.js` を作成
  - classの書き方・継承を演習

---

## Task 5: s30〜s38 Node.js・Express・MongoDB

**Files:**
- `~/sandbox/web-dev-bootcamp/s30-s38-nodejs/` 配下にセクションごとにフォルダを作成

- [ ] **s31: Node.js入門**
  - `s31_node/app.js` を作成
  - `node app.js` で実行確認

- [ ] **s32: モジュールとNPM**
  - `npm init -y` でpackage.json生成
  - 外部パッケージをインストールして使う

- [ ] **s33: Express入門**
  - `s33_express/app.js` を作成
  - ルーティングの基本を演習

- [ ] **s34: テンプレートを使った動的なHTML**
  - EJSテンプレートを使った演習

- [ ] **s35: RESTの基本**
  - RESTfulなルーティングを実装

- [ ] **s36〜s38: MongoDB・Mongoose**
  - MongoDB接続・CRUDをMongooseで演習

---

## Task 6: s39〜s59 YelpCamp（大型プロジェクト）

**Files:**
- `~/sandbox/web-dev-bootcamp/s39-s59-yelpcamp/` に1つのExpressアプリを作成

- [ ] **セットアップ**
  ```bash
  cd ~/sandbox/web-dev-bootcamp/s39-s59-yelpcamp
  npm init -y
  npm install express mongoose ejs
  ```

- [ ] **各セクションをコースに沿って実装**
  - s39: CRUD基本
  - s40: ミドルウェア
  - s42: エラーハンドリング
  - s44: MongoDBリレーション
  - s47: クッキー・セッション
  - s50: 認証（Passport.js）
  - s54: 画像アップロード（Cloudinary）
  - s55: 地図（Mapbox）
  - s58: セキュリティ対策
  - s59: デプロイ（Render等）

---

## Task 7: s60〜s73 React

**Files:**
- `~/sandbox/web-dev-bootcamp/s60-s73-react/` にViteプロジェクトを作成

- [ ] **セットアップ（s62のタイミングで実行）**
  ```bash
  cd ~/sandbox/web-dev-bootcamp/s60-s73-react
  npm create vite@latest . -- --template react
  npm install
  npm run dev
  ```

- [ ] **各セクションをコースに沿って実装**
  - s60〜s61: React・JSXの基本
  - s63: Props
  - s65: イベント処理
  - s66〜s67: State
  - s68: コンポーネント設計
  - s69: Form
  - s70: useEffect
  - s71〜s72: Material UI + Todoアプリ

---

## セッション共通チェックリスト

各学習セッションで確認するリスト：

- [ ] `~/sandbox/web-dev-bootcamp/` でClaude Codeを起動した
- [ ] 動画を見てポーズし、コードを書いた
- [ ] わからない点はClaudeに質問した
- [ ] セクション終わりに `/capture` でメモした
- [ ] `/quiz` で復習した
