---
id: note-insight-format-html-redirect-notice
title: "respond_toにおけるformat.htmlとは何か"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **`respond_to` の中で、通常のHTMLリクエストに対する処理を書く分岐**
- ブラウザで普通のページ遷移をする場合のレスポンスをここに書く。
- `redirect_to` や `render` を使って、次に表示する画面やメッセージを指定する。

## Tags
#insight

## Links

## Body
**`respond_to` の中で、通常のHTMLリクエストに対する処理を書く分岐**

**解説：**
`format.html` は、`respond_to` ブロックの中で HTML リクエスト向けの処理を書く場所です。
ブラウザで普通のページを開いたり、フォーム送信後に画面遷移したりするときのレスポンスをここに書きます。
この中では `redirect_to` や `render` を使って、次に表示する画面や `notice` などのメッセージを指定します。


## Example
```ruby
format.html { redirect_to root_path, notice: "完了しました" }
```

このコードでは、HTML リクエストに対して別ページへ遷移しつつ、フラッシュメッセージを表示するよう指定しています。
