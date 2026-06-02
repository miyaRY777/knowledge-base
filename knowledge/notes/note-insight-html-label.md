---
id: note-insight-html-label
title: labelはフォーム部品に説明文をつけるHTML要素
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
---

## Summary
- `label` は入力欄・チェックボックス・ラジオボタンに「何を入力する場所か」を示す要素です。
- `for` 属性と対応する `id` を一致させることでフォーム部品と関連付けられます。
- ラベルをクリックするだけで対応する入力欄にフォーカスが移る UX 上のメリットがあります。

## Tags
#html #form #accessibility

## Links
- [[note-insight-html-form]]
- [[note-insight-html-attribute]]

## Body
`label` は入力欄に「名前」「メールアドレス」などの説明をつけるための要素です。単に文字を置くだけでなく、`for` 属性で入力欄の `id` と関連付けることで、ラベルのテキスト自体をクリックしても入力欄が選択されるようになります。ラジオボタンでは同じ `name` 属性を持つ選択肢をグループにすることで、どれか一方だけを選ばせる制御ができます。アクセシビリティの観点でも重要で、スクリーンリーダーがどの入力欄かを伝えるためにも使われます。

## Example
```html
<label for="email">メールアドレス</label>
<input id="email" type="email" name="email">
```
