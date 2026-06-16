- [ ] `enqueue`とは？

👉 **ジョブを、あとで実行するためにキューへ入れること**

**解説：**
`enqueue` は、ジョブをその場で実行するのではなく、バックグラウンドで実行できるように待ち行列へ登録することです。
Active Job では `perform_later` を呼ぶとジョブが enqueue されます。
すぐ実行する `perform_now` とは違います。

具体例：

```
class NotifyUserJob < ApplicationJob
  def perform(user)
    UserMailer.welcome(user).deliver_now
  end
end

NotifyUserJob.perform_later(User.find(1))
```

このコードでは、`NotifyUserJob` を今すぐ実行するのではなく、あとで実行できるようにキューへ入れるために `perform_later` を使っています。

---

- [ ] `perform_later`とは？

👉 **ジョブを enqueue するためのメソッド**

**解説：**
`perform_later` を呼ぶと、Active Job がジョブをキューに登録します。
その後、設定しているバックエンドが適切なタイミングで実行します。
Rails の Active Job は「ジョブを作る・enqueueする・実行する」流れで使います。

具体例；

```
ReportJob.perform_later(current_user.id)
```

このコードでは、レポート作成ジョブをキューに登録して、あとでバックグラウンド実行するために `perform_later` を使っています。

---

- [ ] `perform_now`とは？

👉 **ジョブをその場ですぐ実行するメソッド**

**解説：**
`perform_now` はキューに入れず、呼んだ場所ですぐ `perform` を実行します。
非同期処理にしたいときは `perform_later`、同期でその場で動かしたいときは `perform_now` を使います。

具体例：

```
ReportJob.perform_now(current_user.id)
```

このコードでは、ジョブをキューに入れず、その場ですぐ処理を実行するために `perform_now` を使っています。
- [ ] Global IDとは？

👉 Active Recordオブジェクトを、あとで再取得できるように、適切な形で表す仕組みのこと

解説：

Global ID は、`User` などのモデルをジョブ引数としてそのまま渡せるようにするための仕組みです
Active Job はモデルそのものを保存するのではなく、あとでそのレコードを見つけられる情報として扱います
そのため、実行時までにレコードが消えていると復元できません。

具体例：

```
class NotifyUserJob < ApplicationJob
  def perform(user)
    puts user.email
  end
end

NotifyUserJob.perform_later(User.find(1))
```

このコードでは、`User.find(1)` の結果をジョブにそのまま渡せるようにするために、Global ID が使われています。

流れ

```
# enqueue時
User.find(1)
# ↓
{ "_aj_global_id" => "gid://app/User/1" }

# 実行時
{ "_aj_global_id" => "gid://app/User/1" }
# ↓
User.find(1) 相当の復元
# ↓
perform(user)

# _aj_global_id
👉 これは「この値は Active Job 用の Global ID です」と示す目印のキーです

# "gid://app/User/1"
👉 これは User モデルの id=1 を表す Global ID の文字列です
```

- [ ] シリアライズとは？

👉 オブジェクトを、保存や送信しやすい形に変換すること

**解説：**
シリアライズは、Rubyのオブジェクトをそのままでは扱いにくい場面で、文字列やハッシュなどの形に変換するときに使います。
Active Job では、ジョブに渡した引数をキューに保存できる形にするためにシリアライズが行われます。
Rails では通常、この処理を自分で書かなくても Active Job が行います。

具体例：

```
user = User.find(1)
NotifyUserJob.perform_later(user)
```

このコードでは、ジョブに `user` を渡せるようにするために、Active Job が内部でシリアライズを使っています。
- [ ] デシリアライズとは？

👉 変換して保存したデータを、使える形に戻すこと！

**解説：**
デシリアライズは、シリアライズされたデータを元に戻して、アプリの中で使える形に復元する処理です。
Active Job では、キューに保存されていた引数をジョブ実行時に取り出して使うために行われます。
対象レコードが削除されていると、復元できずエラーになることがあります。

具体例：

```
class NotifyUserJob < ApplicationJob
  def perform(user)
    UserMailer.welcome(user).deliver_now
  end
end

このコードでは、ジョブ実行時に保存されていた引数を使える `user` に戻すために、デシリアライズが使われています。
```
