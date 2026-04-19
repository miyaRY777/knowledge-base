---
id: note-insight-tailwind-responsive-grid-columns
title: `md:grid-cols-2 lg:grid-cols-4` は画面幅で列数を切り替える
created: 2026-04-19
source: [[2026-04-19_insight_rails-and-tailwind-terms.md]]
---

## Summary
- `grid-cols-2` は 2 列、`grid-cols-4` は 4 列の Grid を作ります。
- `md:` と `lg:` を付けると、画面サイズごとに適用する列数を切り替えられます。
- レスポンシブにカード一覧や一覧レイアウトを調整したいときに便利です。

## Tags
#frontend #tailwindcss #responsive #grid

## Links
- [[note-insight-classlist-and-hidden]]

## Body
`md:grid-cols-2 lg:grid-cols-4` は、Tailwind CSS のレスポンシブ接頭辞を使って Grid の列数を切り替える書き方です。中サイズ以上では 2 列、大サイズ以上では 4 列になり、画面幅に合わせて自然にレイアウトを変えられます。

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
