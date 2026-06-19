---
id: note-insight-docker-image
title: Dockerイメージはコンテナを作るためのテンプレート
created: 2026-05-29
source: [[2026-05-29_insight_docker-basics]]
quiz_fail_log: []
---

## Summary
- Dockerイメージは、Dockerコンテナを作るための元になるテンプレートです。
- アプリ本体、ライブラリ、設定など、実行に必要なものをまとめます。
- イメージを取得したり作成したりして、それをもとにコンテナを起動します。

## Tags
#docker #container #development #basics

## Links
- [[note-insight-docker]]
- [[note-insight-docker-container]]
- [[note-insight-dockerfile]]
- [[note-insight-docker-hub]]

## Body
Dockerイメージは、コンテナを作るための設計図やテンプレートにあたるものです。アプリケーション本体だけでなく、実行に必要なライブラリや設定も含めてまとめられます。

イメージそのものは実行中の環境ではなく、そこからコンテナを作って動かします。たとえばRubyのイメージを取得しておくと、そのイメージをもとにRubyを使えるコンテナを起動できます。

## Example
```bash
docker pull ruby:3.3
```

