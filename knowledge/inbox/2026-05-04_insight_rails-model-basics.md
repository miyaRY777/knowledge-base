- [ ] `スコープ`とは？

👉 **よく使う検索条件に名前をつけて再利用する仕組み**

**解説：**
`スコープ` は、RailsのModelに検索条件をまとめて定義するための機能です。
一覧画面で「公開中だけ取得する」「新しい順に並べる」など、同じ条件を何度も使うときに便利です。Rails Guidesでも、Active Recordのクエリはメソッドチェーンで組み合わせられると説明されています。
([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_querying.html?utm_source=chatgpt.com "Active Record Query Interface"))

```ruby
class Project < ApplicationRecord
  scope :active, -> { where(status: "active") }
end

Project.active
```

このコードでは、`status` が `"active"` のプロジェクトだけを取得するために `スコープ` を使っています。

---

- [ ] `Resend`とは？

👉 **Webアプリからメールを送信するための外部メールサービス**

**解説：**
`Resend` はRailsの標準機能ではありません。
開発者向けのメール送信サービスで、問い合わせメール、招待メール、パスワード再設定メールなどを送るときに使われることがあります。公式サイトでは、トランザクションメールやマーケティングメールを送信できるサービスとして説明されています。
([Resend](https://resend.com/?utm_source=chatgpt.com "Resend · Email for developers"))

**具体例：**
- ユーザー登録後に確認メールを送る
- パスワード再設定メールを送る
- プロジェクト招待メールを送る
- お問い合わせ内容を管理者へ送る

この例では、Railsアプリからメールを外部に送信するために `Resend` が関係しています。

---

- [ ] `オンプレ`とは？

👉 **自社や自分たちで用意したサーバー環境でシステムを動かす方式**

**解説：**
`オンプレ` は「オンプレミス」の略で、Railsの特別な機能名ではありません。
RenderやHerokuのようなクラウドに任せるのではなく、自分たちでサーバーやネットワークを管理する運用方式です。

**具体例：**
- 会社内にサーバーを置いてアプリを動かす
- サーバーのOS更新やセキュリティ対応も自社で管理する
- クラウドサービスではなく、自社管理のインフラを使う

この例では、アプリをどこで動かすかという運用方式として `オンプレ` が関係しています。

---

- [ ] `inclusion`とは？

👉 **値が決められた候補の中に含まれているか確認するバリデーション**

**解説：**
`inclusion` はRailsのバリデーションで、入力された値が指定した一覧に含まれているかを確認するときに使います。
たとえば、ステータスや役割など、使える値を限定したい場合に便利です。Rails Guidesでは、`inclusion` は指定した集合に値が含まれているかを検証するバリデーションとして説明されています。
([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_validations.html?utm_source=chatgpt.com "Active Record Validations"))

```ruby
class ProjectMembership < ApplicationRecord
  validates :role, inclusion: { in: [0, 1, 2] }
end
```

このコードでは、`role` に `0`, `1`, `2` 以外の値が入らないようにするために `inclusion` を使っています。

---

- [ ] `presence`とは？

👉 **値が空ではないことを確認するバリデーション**

**解説：**
`presence` はRailsのバリデーションで、名前やメールアドレスなど、必ず入力してほしい項目に使います。
空文字や `nil` のまま保存されるのを防ぐために使います。Rails Guidesでは、`presence: true` によって属性が空でないことを確認できると説明されています。
([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_validations.html?utm_source=chatgpt.com "Active Record Validations"))

```ruby
class Profile < ApplicationRecord
  validates :adventurer_name, presence: true
end
```

このコードでは、冒険者名が空のまま保存されないようにするために `presence` を使っています。

---

- [ ] `uniqueness`とは？

👉 **同じ値がすでに存在しないか確認するバリデーション**

**解説：**
`uniqueness` はRailsのバリデーションで、メールアドレスやユーザー名などを重複させたくないときに使います。
ただし、Rails側のバリデーションだけでは完全ではないため、重要な項目ではDB側にもユニーク制約をつけるのが安全です。Rails Guidesでも、`uniqueness` は保存前に値の一意性を検証するものとして説明されています。
([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_validations.html?utm_source=chatgpt.com "Active Record Validations"))

```ruby
class User < ApplicationRecord
  validates :email, uniqueness: true
end
```

このコードでは、同じメールアドレスのユーザーを重複登録しにくくするために `uniqueness` を使っています。

---

- [ ] `integer`とは？

👉 **整数を保存するためのデータ型**

**解説：**
`integer` は、小数ではない数値を保存するための型です。
Railsのマイグレーションでは、年齢、順番、件数、ステータス番号などを保存するときに使います。RailsのマイグレーションはRubyのDSLでDB構造を変更できる仕組みです。
([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_migrations.html?utm_source=chatgpt.com "Active Record Migrations"))

```ruby
class AddPositionToTasks < ActiveRecord::Migration[7.1]
  def change
    add_column :tasks, :position, :integer
  end
end
```

このコードでは、タスクの表示順を整数で保存するために `integer` を使っています。

---

- [ ] `bigint`とは？

👉 **より大きな整数を保存するためのデータ型**

**解説：**
`bigint` は、`integer` より大きな整数を保存できるデータ型です。
Railsでは、主キーの `id` や外部キーの `user_id` などでよく使われます。Rails Guidesでは、Active Recordの主キーはデフォルトで `id` という整数カラムになり、PostgreSQLやMySQLでは `bigint` が使われると説明されています。
([Ruby on Rails Guides](https://guides.rubyonrails.org/v6.0/active_record_basics.html?utm_source=chatgpt.com "Active Record Basics"))

```ruby
class CreateProfiles < ActiveRecord::Migration[7.1]
  def change
    create_table :profiles do |t|
      t.bigint :user_id, null: false

      t.timestamps
    end
  end
end
```

このコードでは、`users` テーブルの `id` と対応させるために、`user_id` に `bigint` を使っています。
