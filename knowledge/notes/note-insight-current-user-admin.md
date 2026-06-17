---
id: note-insight-current-user-admin
title: "current_user.admin?はログイン中のユーザーが管理者かどうかを確認する書き方"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **今ログインしているユーザーが管理者かどうかを確認する書き方**
- `current_user` は、ログイン中のユーザーを表すことが多いです。そこに対して `admin?` を呼ぶと、管理者権限があるかどうかを判定できます。`current_user` という名前自体は Rails 本体の共通メソッドではなく、Devise などの認証機能でよく使われるものです。`admin?` の部分は boolean カラム由来の判定です。 ([Ruby on Rails API](https://api.rubyonrails.org/classes/ActiveRecord/AttributeMethods.html "ActiveRecord::AttributeMethods - Rails API"))
- if current_user.admin?

## Tags
#rails #activerecord #authorization

## Links

## Body
`current_user.admin?` は、boolean カラム `admin` に対してRailsが自動生成する述語メソッドです。
`current_user` は Rails 本体のメソッドではなく、Devise などの認証ライブラリが提供するヘルパーで、「今ログインしているユーザー」を返します。
管理者機能への分岐はコントローラの `before_action` で行い、`redirect_to` で弾くパターンが一般的です。

## Example

```ruby
if current_user.admin?
  redirect_to admin_root_path
end
```

このコードでは、今ログインしているユーザーが管理者なら管理画面へ進ませるために `current_user.admin?` を使っています。
