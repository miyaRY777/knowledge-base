---
id: note-insight-active-record-callbacks
title: Active Record Callbacksの仕組みと注意点
created: 2026-03-31
source: [[2026-03-31_insight_rails-study.md]]
---

## Summary（3行）
- モデルの作成・更新・削除の前後に自動で処理を挟む仕組み
- before_create, after_save などタイミング別にフックできる
- 便利だが多用すると処理の流れが追いにくくなるリスクがある

## Tags
#rails #activerecord #callbacks

## Links
- [[note-insight-dependent-restrict-with-error]]
- [[note-insight-current-attributes]]

## Body
Active Record Callbacksは、レコードのライフサイクル（作成・更新・削除・バリデーション）の各タイミングに処理を差し込める仕組み。たとえば保存前にデータを整形したり、削除後にログを残したりできる。ただしコールバックが増えると「このレコードを保存したら裏で何が起きるのか」が見えにくくなり、デバッグやテストが難しくなる。特にafter_commitで外部APIを呼ぶようなケースは副作用が大きい。シンプルなデータ整形には便利だが、複雑なビジネスロジックはServiceオブジェクトなどに切り出す方が保守しやすい。

```ruby
class User < ApplicationRecord
  before_create :set_default_name

  private

  def set_default_name
    self.name ||= "ゲスト"
  end
end
```
