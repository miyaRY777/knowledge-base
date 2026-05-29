---
id: note-insight-docker-hub
title: DockerHubはDockerイメージを探して共有できるサービス
created: 2026-05-29
source: [[2026-05-29_insight_docker-basics]]
---

## Summary
- DockerHubは、Dockerイメージを保存、公開、取得できるサービスです。
- 既存のイメージを探したり、チームや外部に共有したりできます。
- `docker pull postgres` のように、必要なイメージを取得するときに利用されます。

## Tags
#docker #container #development #basics

## Links
- [[note-insight-docker]]
- [[note-insight-docker-image]]

## Body
DockerHubは、Dockerイメージを探したり共有したりするためのサービスです。自分でイメージを作らなくても、PostgreSQLやRubyなど、よく使われるイメージを取得して利用できます。

DockerHubのようなレジストリを使うことで、開発環境やアプリの実行環境に必要なイメージを配布しやすくなります。

## Example
```bash
docker pull postgres
```

