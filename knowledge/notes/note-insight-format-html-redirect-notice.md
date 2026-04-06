---
id: note-insight-format-html-redirect-notice
title: format.html { redirect_to mypage_rooms_path, notice: "部屋から退出しました" }の要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **通常のHTMLリクエスト時にリダイレクトとメッセージ表示を行う処理**
- HTMLリクエストではページ遷移が必要なので `redirect_to` を使います。
- `notice:` はフラッシュメッセージとして次の画面に渡されます。

## Tags
#insight

## Links
- [[関連ノート]]

## Body
**通常のHTMLリクエスト時にリダイレクトとメッセージ表示を行う処理**

**解説：**
HTMLリクエストではページ遷移が必要なので `redirect_to` を使います。
`notice:` はフラッシュメッセージとして次の画面に渡されます。

```ruby
format.html { redirect_to root_path, notice: "完了しました" }
```

このコードでは、処理後に別ページへ遷移しつつメッセージを表示するために redirect_to を使っています。
