- [ ] `Docker`とは？

👉 **アプリをコンテナという単位で動かすためのプラットフォーム**

**解説：**
`Docker` は、アプリや必要な環境をまとめて、別のPCやサーバーでも動かしやすくするための仕組みです。
「自分のPCでは動くけど、他の環境では動かない」を減らすために使われます。Docker公式では、アプリを build・share・run するためのプラットフォームとして説明されています。([Docker](https://www.docker.com/ "Docker: Accelerated Container Application Development"))

**具体例：**
- RailsアプリをDockerで起動する
- PostgreSQLもDockerで起動する
- チームメンバーが同じ環境で開発できるようにする

この例では、開発環境をそろえてアプリを動かすために `Docker` が関係しています。

---

- [ ] `Dockerエンジン`とは？

👉 **Dockerコンテナを作成・実行・管理する中心部分**

**解説：**
`Dockerエンジン` は、Dockerの中核となる仕組みです。
Docker公式では、`dockerd` というデーモン、API、`docker` CLIクライアントを含むクライアント・サーバー型のアプリケーションとして説明されています。([Docker Documentation](https://docs.docker.com/engine/ "Docker Engine"))

```bash
docker run hello-world
```

このコードでは、Dockerコンテナを実行するために `Dockerエンジン` が裏側で動いています。

---

- [ ] `Dockerイメージ`とは？

👉 **コンテナを作るための設計図・テンプレート**

**解説：**
`Dockerイメージ` は、アプリ本体、実行に必要なライブラリ、設定などをまとめたものです。
イメージをもとにして、実際に動く `Dockerコンテナ` を作ります。

```bash
docker pull ruby:3.3
```

このコードでは、Rubyを使うための `Dockerイメージ` を取得しています。

---

- [ ] `DockerHub`とは？

👉 **Dockerイメージを探したり共有したりできるサービス**

**解説：**
`DockerHub` は、Dockerイメージを保存・公開・取得できる場所です。
Docker公式では、コンテナイメージを見つけたり共有したりするための中央リポジトリとして説明されています。([Docker Hub](https://hub.docker.com/ "Docker Hub Container Image Library | App Containerization"))

```bash
docker pull postgres
```

このコードでは、DockerHubなどのレジストリから `postgres` の `Dockerイメージ` を取得しています。

---

- [ ] `Dockerfile`とは？

👉 **Dockerイメージの作り方を書いた設定ファイル**

**解説：**
`Dockerfile` は、どのOSや言語環境を使うか、どのファイルをコピーするか、どのコマンドを実行するかを書くファイルです。
`DockerFile` ではなく、正式には `Dockerfile` と書くのが一般的です。Docker公式ドキュメントでも `Dockerfile` という表記が使われています。([Docker ドキュメント](https://docs.docker.jp/engine/reference/builder.html "Dockerfile リファレンス"))

```dockerfile
FROM ruby:3.3

WORKDIR /app

COPY . .

CMD ["ruby", "app.rb"]
```

このコードでは、Rubyでアプリを動かすための `Dockerイメージ` を作る手順として `Dockerfile` を使っています。

---

- [ ] `Dockerコンテナ`とは？

👉 **Dockerイメージから作られて実際に動く実行環境**

**解説：**
`Dockerコンテナ` は、Dockerイメージをもとに起動する実体です。
イメージが「設計図」なら、コンテナは「実際に動いているアプリ環境」です。

```bash
docker run -p 3000:3000 my-rails-app
```

このコードでは、`my-rails-app` というイメージから `Dockerコンテナ` を起動しています。
