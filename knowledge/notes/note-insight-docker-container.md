---
id: note-insight-docker-container
title: DockerコンテナはDockerイメージから作られて実際に動く実行環境
created: 2026-05-29
source: [[2026-05-29_insight_docker-basics]]
quiz_fail_log: []
---

## Summary
- Dockerコンテナは、Dockerイメージをもとに起動する実行環境です。
- イメージがテンプレートなら、コンテナは実際に動いているアプリ環境です。
- `docker run` を使うと、指定したイメージからコンテナを起動できます。

## Tags
#docker #container #development #basics

## Links
- [[note-insight-docker]]
- [[note-insight-docker-image]]
- [[note-insight-docker-engine]]

## Body
Dockerコンテナは、Dockerイメージから作られて実際に動く実行環境です。イメージがコンテナを作るための元になるテンプレートだとすると、コンテナはそこから起動された実体です。

アプリをコンテナとして起動すると、必要な環境をまとめた単位で動かせます。たとえばRailsアプリのイメージからコンテナを起動し、ホスト側のポートとつなげることでブラウザからアクセスできるようにします。

## Example
```bash
docker run -p 3000:3000 my-rails-app
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
