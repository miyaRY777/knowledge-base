---
id: note-insight-html-form
title: form要素はユーザー入力をサーバーに送信するHTML要素
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- `form` は入力欄・ボタンなどをまとめてユーザーの入力をサーバーへ送る仕組みです。
- `action` でどこに送るか、`method` でどのHTTPメソッドを使うかを指定します。
- 検索・ログイン・会員登録・お問い合わせなど幅広い場面で使われます。

## Tags
#html #form #http

## Links
- [[note-insight-form-action-attribute]]
- [[note-insight-form-method-attribute]]
- [[note-insight-html-label]]
- [[note-insight-side-effect-web]]

## Body
`<form>` は入力部品（`input`・`select`・`textarea` など）をまとめる容器です。ユーザーが送信ボタンを押すと、`action` 属性のURLへ `method` 属性で指定したHTTPメソッドでデータが送られます。Railsでは `form_with` ヘルパーがHTMLの `<form>` タグを生成しつつ、CSRFトークンの埋め込みも自動で行います。

## Example
```html
<form action="/contact" method="post">
  <input type="text" name="message">
  <button type="submit">送信</button>
</form>
```
