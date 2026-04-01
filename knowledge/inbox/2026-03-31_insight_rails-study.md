# 3月31日 学習メモ

**日時**: 2026-03-31
**情報源**: Raycast学習メモ

---

- [ ] `Active Record Callbacks`とは？

👉 
**モデルの処理の前後に、自動で特定の処理を実行する仕組みのこと**

例えば保存前にデータを整形したり、削除後にログの記録に使います。
使いすぎると処理の流れが見えづらくなるので注意が必要です。

**解説：**
Active Record Callbacks は、レコードの作成・更新・削除などのタイミングで、自動的に処理を挟むために使います。
バリデーション前や保存後など、特定のタイミングにフックして処理を書けます。
ただし処理が増えると見えにくくなるため、使いすぎには注意が必要です。

具体例：

```ruby
class User < ApplicationRecord
  before_create :set_default_name

  private

  def set_default_name
    self.name ||= "ゲスト"
  end
end
```

このコードでは、ユーザーが作成される前に name が空なら「ゲスト」を設定するために Active Record Callbacks を使っています。

---

- [ ] `CurrentAttributes`とは？

👉 **リクエストごとに共通で使いたい値を管理する仕組み**

**解説：**
CurrentAttributes は、ログイン中のユーザーなどをグローバルに扱うための仕組みです。
コントローラやモデルのどこからでも同じ値にアクセスできるようになります。
ただし状態を持つため、使いすぎると依存関係が分かりにくくなる点に注意が必要です。

```ruby
# app/models/current.rb
class Current < ActiveSupport::CurrentAttributes
  attribute :user
end

# controller
class ApplicationController < ActionController::Base
  before_action do
    Current.user = current_user
  end
end

# model
class Post < ApplicationRecord
  before_create do
    self.user = Current.user
  end
end
```

このコードでは、ログインユーザーをどこからでも使えるようにするために CurrentAttributes を使っています。
