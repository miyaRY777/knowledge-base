---
id: note-insight-tailwind-responsive-grid-columns
title: `md:grid-cols-2 lg:grid-cols-4`とは？
created: 2026-04-19
source: [[2026-04-19_insight_rails-and-tailwind-terms.md]]
---

## Summary
- `md:grid-cols-2 lg:grid-cols-4` は、Tailwind CSS で画面幅ごとに Grid の列数を切り替える指定です。
- `md:` 以上では 2 列、`lg:` 以上では 4 列の Grid になります。
- レスポンシブにカード一覧や一覧レイアウトを調整したいときに便利です。

## Tags
#frontend #tailwindcss #responsive #grid

## Links
- [[note-insight-classlist-and-hidden]]

## Body
`md:grid-cols-2 lg:grid-cols-4` は、Tailwind CSS のレスポンシブ接頭辞を使って Grid の列数を切り替える書き方です。`md:` 以上の画面幅では 2 列、`lg:` 以上の画面幅では 4 列になり、画面サイズに合わせてレイアウトを変えられます。

カード一覧や管理画面の一覧など、横幅に応じて見やすい列数へ調整したいときに使います。

## Example
```erb
<div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
</div>
```

このコードでは、通常時は 1 列のまま、`md` 以上で 2 列、`lg` 以上で 4 列に切り替わります。

## Action
- [ ] `sm:` や `xl:` を含めたブレークポイントの使い分けも整理する
