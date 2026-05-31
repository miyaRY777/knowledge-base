# Docker基礎マップ

> **このMOCで分かること**: オンプレミスとの対比からDockerの全体像、コンテナ・イメージ・Dockerfileの関係を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | オンプレミス | 自社設備でサーバーを運用するスタイル | [[note-insight-on-premise]] |
| 2 | Docker | アプリをコンテナとして動かすプラットフォーム | [[note-insight-docker]] |
| 3 | Dockerエンジン | コンテナを動かすDockerの中核ソフトウェア | [[note-insight-docker-engine]] |
| 4 | Dockerイメージ | コンテナの設計図となる読み取り専用のテンプレート | [[note-insight-docker-image]] |
| 5 | Dockerコンテナ | イメージから起動した実行中の環境 | [[note-insight-docker-container]] |
| 6 | Dockerfile | イメージをコードで定義するファイル | [[note-insight-dockerfile]] |
| 7 | Docker Hub | Dockerイメージを共有・配布するレジストリ | [[note-insight-docker-hub]] |
| 8 | オーケストレーション | 複数コンテナの連携・管理を自動化する仕組み | [[note-insight-orchestration]] |

---

## 背景：なぜコンテナが必要か

[[note-insight-on-premise]]
[[note-insight-docker]]

**ポイント**:
- オンプレミスは自社でサーバーを保有・管理するスタイル。クラウドとの対比で理解する
- 環境差異（開発機 vs 本番サーバー）を解消し、「手元で動いたものがそのまま本番でも動く」を実現するのがDockerのコア価値

---

## コンテナの仕組み

[[note-insight-docker-engine]]
[[note-insight-docker-image]]
[[note-insight-docker-container]]
[[note-insight-dockerfile]]

**ポイント**:
- イメージはコンテナの設計図（読み取り専用）。コンテナはイメージから起動した実行インスタンス
- Dockerfile にベースイメージ・インストールコマンド・起動コマンドを記述し `docker build` でイメージを作る
- コンテナは使い捨てが基本。状態を持たせたい場合はボリュームやDBコンテナを分離する
- Dockerエンジンがコンテナの起動・停止・ネットワーク管理を担う

---

## イメージの共有と運用

[[note-insight-docker-hub]]
[[note-insight-orchestration]]

**ポイント**:
- Docker Hub はDockerイメージの公開レジストリ。`docker pull` で取得できる
- 本番環境で複数コンテナを連携させるにはオーケストレーション（Kubernetes, Docker Composeなど）が必要

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| Docker Composeの使い方を別ノートにするか | - | - | - |
| ボリューム・バインドマウントの違いを整理する | - | - | - |
| コンテナとVMの違いをノート化するか | - | - | [[note-insight-docker-container]] |

---

## 関連リンク

- [[map-rails-basics]]
- [[map-database-fundamentals]]
