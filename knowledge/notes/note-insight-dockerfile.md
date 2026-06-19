---
id: note-insight-dockerfile
title: DockerfileはDockerイメージの作り方を書く設定ファイル
created: 2026-05-29
source: [[2026-05-29_insight_docker-basics]]
quiz_fail_log: []
---

## Summary
- Dockerfileは、Dockerイメージを作る手順を書く設定ファイルです。
- ベースにする環境、作業ディレクトリ、コピーするファイル、実行コマンドなどを定義します。
- 表記は `DockerFile` ではなく `Dockerfile` とするのが一般的です。

## Tags
#docker #container #development #basics

## Links
- [[note-insight-docker]]
- [[note-insight-docker-image]]
- [[note-insight-docker-container]]

## Body
Dockerfileは、Dockerイメージを作るための手順を記述するファイルです。どの言語環境を使うか、アプリのファイルをどこへ置くか、コンテナ起動時にどのコマンドを実行するかなどを書きます。

Dockerfileを用意しておくと、同じ手順でイメージを作れるため、開発環境や実行環境を再現しやすくなります。ファイル名は通常 `Dockerfile` と表記します。

## Example
```dockerfile
FROM ruby:3.3

WORKDIR /app

COPY . .

CMD ["ruby", "app.rb"]
```

