---
id: note-insight-active-job-serialize
title: Active Jobはジョブ引数をシリアライズしてキューに保存する
created: 2026-06-16
source: [[2026-06-16_insight_active-job-enqueue-and-serialization]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- シリアライズとは、Ruby オブジェクトをキューに保存できる形（文字列やハッシュ）に変換することです。
- Active Job が自動で行うため、通常は意識しなくてよいです。
- Global ID を使うことで、モデルオブジェクトもシリアライズの対象にできます。

## Tags
#rails #active-job #serialization

## Links
- [[note-insight-active-job-global-id]]
- [[note-insight-active-job-deserialize]]

## Body
キューはプロセスをまたいで引数を受け渡すため、Ruby オブジェクトをそのままの形では保存できません。そこで Active Job は enqueue 時にジョブ引数をシリアライズし、キューが扱える形式に変換します。文字列・数値・配列・ハッシュは基本的にそのまま扱えますが、Active Record モデルは Global ID を介して変換されます。この処理は Active Job の内部で自動的に行われるため、アプリ開発者が自分でシリアライズコードを書く必要はありません。

## Example
```ruby
user = User.find(1)
NotifyUserJob.perform_later(user)
# ↑ enqueue時にuserが自動でシリアライズされる
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
