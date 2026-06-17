---
id: note-insight-turbo-confirm
title: "turbo_confirmはTurbo操作の前にブラウザの確認ダイアログを出す指定"
created: 2026-04-07
source: [[2026-04-07_insight_rails-ruby-terms.md]]
---

## Summary
- `turbo_confirm` は Turbo 操作の前に確認ダイアログを出す指定です。
- 削除や再発行のような誤操作を防ぎたい場面で使います。
- OK を押したときだけ処理が続きます。

## Tags
#rails #turbo #ui

## Links

## Body
`turbo_confirm` は、Turbo を使ったリンクやフォーム送信の前に確認ダイアログを出したいときに使う指定です。削除や再発行のように、うっかり実行すると困る操作に向いています。

Turbo の `data` 属性に設定して、ユーザーが確認ダイアログで OK を選んだときだけ処理が続くようにします。

## Example
```erb
<%= link_to "再発行",
            regenerate_share_link_mypage_room_path(room),
            data: { turbo_method: :patch, turbo_confirm: "招待リンクを再発行しますか？" } %>
```

このコードでは、招待リンクの再発行を実行する前に、確認ダイアログを表示するために `turbo_confirm` を使っています。

## Action
- [ ] `turbo_method` と一緒に使う例を別ノートに整理する
