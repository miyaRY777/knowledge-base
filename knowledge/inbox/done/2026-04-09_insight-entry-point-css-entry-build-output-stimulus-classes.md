- [ ] `エントリーポイント`とは？
👉 **処理や読み込みが始まる起点になるファイルや場所のこと**

**解説：**
エントリーポイントは、「ここからアプリや処理を始めます」という入口です。
JavaScriptの読み込みやビルドでは、最初に読み込むファイルを指すことが多いです。
1つのファイルだけとは限らず、用途ごとに複数あることもあります。

```js
// app/javascript/application.js
import "@hotwired/turbo-rails"
import "controllers"
import "./menu"
```

このコードでは、JavaScriptの読み込みをここから始めるために エントリーポイント を使っています。

---

- [ ] `CSSエントリ`とは？
👉 **CSSの読み込みやビルドの始まりになるCSSファイルのこと**

**解説：**
CSSエントリは、スタイルをまとめて読み込むための入口になるファイルです。
このファイルから `@import` したり、Tailwindの設定を通して最終的なCSSを作ったりします。
Railsの特別な機能名ではなく、ビルドや構成の考え方として使われる名前です。

```css
/* app/assets/stylesheets/application.css */
@import "tailwindcss";
@import "./components/buttons.css";
```

このコードでは、複数のスタイルをここからまとめて読み込むために CSSエントリ を使っています。

---

- [ ] `ビルド出力`とは？
👉 **変換やまとめ処理のあとに作られる最終的なファイルのこと**

**解説：**
ビルド出力は、元のコードをそのまま使わず、ブラウザで使いやすい形に変換した結果です。
たとえば、複数のCSSやJavaScriptを1つにまとめたファイルなどがこれにあたります。
編集するのは元ファイル側で、ビルド出力ファイルを直接触らないことが多いです。

```bash
$ yarn build
# app/assets/builds/application.css が生成される
```

このコードでは、ビルドした結果として使うファイルを作るために ビルド出力 を使っています。

---

- [ ] `StimulusのClassesプロパティAPI`とは？
👉 **HTML側で渡したclass名を、Stimulusコントローラから使いやすくする仕組みのこと**

**解説：**
Stimulusでは `static classes = [...]` と書くことで、HTMLのclass名をJavaScript側で取り出せます。
「表示中のclass」「エラー時のclass」などを、決まった名前で安全に使いたいときに便利です。
指定したclassがHTML側にないと、使い方によってはエラーになるものもあるので注意が必要です。

```js
// controllers/toggle_controller.js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static classes = ["hidden"]

  hide() {
    this.element.classList.add(this.hiddenClass)
  }
}
```

```erb
<div data-controller="toggle"
     data-toggle-hidden-class="hidden">
  メニュー
</div>
```

このコードでは、HTML側で渡した hidden というclass名をJavaScript側で安全に使うために StimulusのClassesプロパティAPI を使っています。
