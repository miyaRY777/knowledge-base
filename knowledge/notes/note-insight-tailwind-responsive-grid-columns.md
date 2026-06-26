---
id: note-insight-tailwind-responsive-grid-columns
title: "`md:grid-cols-2 lg:grid-cols-4`とは？"
created: 2026-04-19
source: [[2026-04-19_insight_rails-and-tailwind-terms.md]]
review_streak: 0
last_reviewed_on: 2026-06-18
quiz_fail_log: []
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
`md:grid-cols-2 lg:grid-cols-4` は、Tailwind CSS のレスポンシブ接頭辞を使って Grid の列数を切り替える書き方です。接頭辞なしのクラスがすべての幅に適用され、より大きなブレークポイントで上書きされます（モバイルファースト）。

| 接頭辞 | 最小幅 | イメージ |
|--------|--------|----------|
| （なし）| 0px〜 | スマートフォン（縦） |
| `sm:` | 640px〜 | スマートフォン（横） |
| `md:` | 768px〜 | タブレット |
| `lg:` | 1024px〜 | ノートPC |
| `xl:` | 1280px〜 | デスクトップ |
| `2xl:` | 1536px〜 | 大型モニター |

`gap` はグリッド要素間のすき間を指定するプロパティです。`gap-4` は 1rem（16px）。縦横個別に指定する場合は `gap-y-4` / `gap-x-4` を使います。

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


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
