---
id: note-insight-csrf
title: "CSRFはログイン済み状態を悪用して意図しないリクエストを送らせる攻撃"
created: 2026-05-02
source: [[2026-05-02_insight_samesite-csrf-soft-delete.md]]
quiz_fail_log: []
---

## Summary
- CSRF は、ログイン済みユーザーの権限を悪用して、本人の意図しないリクエストを送らせる攻撃です。
- Cookie が自動送信される仕組みと関係し、状態変更を伴うリクエストで特に問題になります。
- Rails では CSRF トークンを検証して、正規のフォームやリクエストかを確認します。

## Tags
#web #security #csrf #rails #cookie

## Links
- [[note-insight-cookie-samesite]]
- [[note-insight-cookie]]
- [[note-insight-rails-cookies]]
- [[note-insight-post-request]]

## Body
CSRF は、ユーザーがログインしている状態を利用し、別サイトなどから本人が意図していない操作リクエストを送らせる攻撃です。ブラウザは条件が合えば Cookie を自動で送るため、サーバー側から見ると「ログイン済みユーザーからのリクエスト」に見えてしまうことがあります。

特に、送金、投稿、削除、設定変更のように状態を変えるリクエストでは注意が必要です。Rails ではフォームやリクエストに CSRF トークンを含め、サーバー側でその値を検証することで、正規の画面から送られたリクエストかを確認します。

`SameSite=Lax` や `SameSite=Strict` は、クロスサイトで Cookie が送られる場面を減らすため、CSRF のリスクを下げる補助的な対策になります。ただし、Rails の CSRF トークン検証とは役割が違うため、どちらか一方だけで考えない方が安全です。

## Example
```erb
<%= form_with model: @post do |f| %>
  <%= f.text_field :title %>
<% end %>
```

このコードでは、Rails のフォームヘルパーを使うことで、CSRF トークンを含むフォームを生成できます。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
