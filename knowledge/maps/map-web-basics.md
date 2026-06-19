# Web基礎マップ

> **このMOCで分かること**: HTMLの構造・DOM・フォーム・URL・HTTPの基礎を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | HTMLの属性 | HTMLタグに追加情報を付与する仕組み | [[note-insight-html-attribute]] |
| 2 | HTMLフォーム | ユーザーの入力データをサーバーへ送る仕組み | [[note-insight-html-form]] |
| 3 | フォームのaction属性 | データの送信先URLを指定する属性 | [[note-insight-form-action-attribute]] |
| 4 | フォームのmethod属性 | データ送信方法（GET/POST）を指定する属性 | [[note-insight-form-method-attribute]] |
| 5 | labelタグ | フォーム入力欄と説明文を関連付ける要素 | [[note-insight-html-label]] |
| 6 | DOMツリー | HTMLをブラウザが木構造に変換したもの | [[note-insight-dom-tree]] |
| 7 | ブロックレベル要素 | 縦に積まれる要素。div・p・h1など | [[note-insight-block-level-element]] |
| 8 | インライン要素 | 横に並ぶ要素。spanや aタグなど | [[note-insight-inline-element]] |
| 9 | span要素 | インラインのグルーピングに使う汎用要素 | [[note-insight-span-element]] |
| 10 | meta charset=utf-8 | HTMLの文字コードをUTF-8と宣言するタグ | [[note-insight-meta-charset-utf8]] |
| 11 | HTMLをUTF-8で保存する理由 | 文字化けを防ぐためにエンコードを統一する | [[note-insight-html-utf8-save]] |
| 12 | HTMLのclass属性 | 要素にクラス名を付けてCSSやJSから操作する | [[note-insight-html-class-attribute]] |
| 13 | 絶対URL | ドメインから始まる完全なURL | [[note-insight-absolute-url]] |
| 14 | 相対URL | 現在のパスを基準にした省略形URL | [[note-insight-relative-url]] |
| 15 | ベースURL | 相対URLの解決に使われる基準URL | [[note-insight-base-url]] |
| 16 | フォールバックURL | エラー時や代替時に使う予備のURL | [[note-insight-fallback-url]] |
| 17 | HTTPリクエスト | クライアントがサーバーへ送る要求 | [[note-insight-http-request]] |
| 18 | HTTPレスポンス | サーバーがクライアントへ返す応答 | [[note-insight-http-response]] |
| 19 | HTTPヘッダー | リクエスト・レスポンスに付属するメタ情報 | [[note-insight-headers]] |
| 20 | Content-Type | 送受信するデータの種類を示すヘッダー | [[note-insight-content-type]] |
| 21 | ステートレス | HTTPはリクエストをまたいで状態を保持しない | [[note-insight-stateless]] |
| 22 | サイドエフェクト（Web） | GETは副作用なし、POSTなどは状態を変える | [[note-insight-side-effect-web]] |

---

## HTMLの構造と要素

[[note-insight-html-attribute]]
[[note-insight-html-form]]
[[note-insight-form-action-attribute]]
[[note-insight-form-method-attribute]]
[[note-insight-html-label]]

**ポイント**:
- HTMLタグには属性（`id`, `class`, `href`など）を付けて情報を追加できる
- フォームはユーザー入力をサーバーへ送る主要な手段。action と method の組み合わせで動作が決まる
- `<label>` を `for` 属性でフォームと紐付けると、クリック範囲が広がりアクセシビリティが向上する

---

## DOMとブラウザレンダリング

[[note-insight-dom-tree]]
[[note-insight-block-level-element]]
[[note-insight-inline-element]]
[[note-insight-span-element]]

**ポイント**:
- ブラウザはHTMLを解析してDOMツリー（木構造）に変換し、それをレンダリングする
- ブロック要素は縦に積まれ（`div`・`p`・`h1`など）、インライン要素は横に並ぶ（`span`・`a`など）
- `<span>` はスタイルを当てたい範囲を囲む汎用インライン要素。意味を持たない

---

## 文字コードとHTML

[[note-insight-meta-charset-utf8]]
[[note-insight-html-utf8-save]]
[[note-insight-html-class-attribute]]

**ポイント**:
- `<meta charset="UTF-8">` がないとブラウザが文字コードを誤判断して文字化けすることがある
- ファイルの保存エンコードと宣言を一致させることが必須
- `class` 属性は複数クラスをスペース区切りで付与でき、CSSやJSから複数要素をまとめて操作できる

---

## URLの種類

[[note-insight-absolute-url]]
[[note-insight-relative-url]]
[[note-insight-base-url]]
[[note-insight-fallback-url]]

**ポイント**:
- 絶対URL（`https://example.com/path`）は常に同じリソースを指す
- 相対URL（`./path` や `/path`）は基準URLからの差分で表す
- ベースURLはページ内の相対URLを解決する起点。`<base href>` タグで上書きできる

---

## HTTPの基礎

[[note-insight-http-request]]
[[note-insight-http-response]]
[[note-insight-headers]]
[[note-insight-content-type]]
[[note-insight-stateless]]
[[note-insight-side-effect-web]]

**ポイント**:
- HTTPはリクエスト→レスポンスの1往復で完結する。状態は保持しない（ステートレス）
- ヘッダーには認証情報・Content-Type・Cookieなどのメタ情報が入る
- Content-Typeを正しく指定しないと受け取る側がデータを正しく解釈できない
- GETは副作用なし・べき等。POST/PUT/DELETEはサーバーの状態を変える可能性がある

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| dataset属性とカスタムデータ属性を整理する | - | - | [[note-insight-dataset-and-data-attributes]] |
| ブロック要素とインライン要素の使い分けをまとめる | - | - | [[note-insight-block-level-element]] |

---

## 関連リンク

- [[map-http-status-and-methods]]
- [[map-http-client-basics]]
- [[map-html-and-dom-basics]]
- [[map-cookie-basics]]
- [[map-session-basics]]
- [[map-web-security-basics]]
