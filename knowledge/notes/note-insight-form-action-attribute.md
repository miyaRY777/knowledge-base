---
id: note-insight-form-action-attribute
title: action属性はフォームの送信先URLを指定する
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- `action属性` は、フォームに入力されたデータをどのURLに送るかを指定します。
- ログインなら `/login`、検索なら `/search` のように処理を担うパスを書きます。
- 省略すると現在のページのURLに送信されます。

## Tags
#html #form

## Links
- [[note-insight-html-form]]
- [[note-insight-form-method-attribute]]

## Body
`action属性` は `<form>` タグに書く属性で、送信先のURLを決めます。フォームはユーザーの入力をサーバーに届ける仕組みなので、どのエンドポイントに届けるかを明示する必要があります。Railsでは `form_with url: ...` のように対応するルーティングのパスを渡す書き方が一般的です。

## Example
```html
<form action="/login" method="post">
  <input type="email" name="email">
  <button type="submit">ログイン</button>
</form>
```
