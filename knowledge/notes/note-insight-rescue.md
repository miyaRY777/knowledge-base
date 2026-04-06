---
id: note-insight-rescue
title: rescueの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **例外をキャッチする仕組み（書く場所と範囲が違う）**
- `rescue` はメソッド内でエラーを捕まえるキーワードです。
- `rescue_from`（よく「Rescue」と呼ばれる）はコントローラ全体でエラーを処理するために使います。

## Tags
#activerecord

## Links
- [[関連ノート]]

## Body
**例外をキャッチする仕組み（書く場所と範囲が違う）**

**解説：**
`rescue` はメソッド内でエラーを捕まえるキーワードです。
`rescue_from`（よく「Rescue」と呼ばれる）はコントローラ全体でエラーを処理するために使います。

```ruby
def show
  @room = Room.find(params[:id])
rescue ActiveRecord::RecordNotFound
  redirect_to root_path
end
```

このコードでは、レコードが見つからないエラーを捕まえてリダイレクトするために rescue を使っています。
