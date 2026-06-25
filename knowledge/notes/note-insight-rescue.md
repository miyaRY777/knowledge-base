---
id: note-insight-rescue
title: "rescueは発生した例外をキャッチして処理を継続させる仕組み"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_fail_log: []
---

## Summary
- **例外をキャッチする仕組み（書く場所と範囲が違う）**
- `rescue` はメソッド内でエラーを捕まえるキーワードです。
- `rescue_from`（よく「Rescue」と呼ばれる）はコントローラ全体でエラーを処理するために使います。

## Tags
#activerecord

## Links

## Body
`rescue` はメソッド内で特定の例外をキャッチするキーワードで、`rescue ActiveRecord::RecordNotFound` のように例外クラスを指定できます。
`rescue_from` はコントローラクラスに書くことでそのコントローラ全体（サブクラス含む）に対してエラーハンドリングを適用でき、同じ例外への対応を一か所にまとめられます。
局所的な例外処理には `rescue`、アプリ横断的なエラーには `rescue_from` という使い分けが基本です。


## Example
```ruby
def show
  @room = Room.find(params[:id])
rescue ActiveRecord::RecordNotFound
  redirect_to root_path
end
```

このコードでは、レコードが見つからないエラーを捕まえてリダイレクトするために rescue を使っています。

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
