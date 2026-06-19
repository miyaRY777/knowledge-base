---
id: note-insight-form-method-attribute
title: method属性はフォーム送信のHTTPメソッドを指定する
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- `method属性` は、フォーム送信に `GET` と `POST` のどちらを使うかを指定します。
- 検索のようにURLに条件を含めてよい場合は `get`、データを送る場合は `post` が適切です。
- `post` はリクエストボディにデータを載せるため、URLに内容が露出しません。

## Tags
#html #form #http

## Links
- [[note-insight-html-form]]
- [[note-insight-form-action-attribute]]
- [[note-insight-side-effect-web]]

## Body
`method属性` で `get` を指定すると入力値がURLのクエリパラメータとして送られます。検索フォームのように「この条件で検索した」という状態をURLで共有したい場面に向いています。一方 `post` はリクエストボディにデータを含めるため、パスワードやメールアドレスのような情報をURLに出さずに送れます。副作用（サーバー状態の変更）を伴う操作には `post` を使うのが基本です。

## Example
```html
<form action="/search" method="get">
  <input type="text" name="keyword">
  <button type="submit">検索</button>
</form>
```
