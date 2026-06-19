---
id: note-insight-docker-engine
title: Dockerエンジンはコンテナを作成・実行・管理する中核部分
created: 2026-05-29
source: [[2026-05-29_insight_docker-basics]]
quiz_fail_log: []
---

## Summary
- Dockerエンジンは、Dockerコンテナを作成、実行、管理する中心的な仕組みです。
- `dockerd`、API、`docker` CLIクライアントなどを含むクライアント・サーバー型の構成です。
- `docker run` のようなコマンドを実行すると、裏側でDockerエンジンがコンテナを扱います。

## Tags
#docker #container #development #basics

## Links
- [[note-insight-docker]]
- [[note-insight-docker-container]]

## Body
Dockerエンジンは、Dockerの中核となる実行基盤です。コンテナを作る、起動する、停止する、管理するといった処理を担います。

利用者は `docker` コマンドを入力しますが、その命令はDockerエンジン側で処理されます。たとえば `docker run hello-world` を実行すると、必要なイメージをもとにコンテナを起動する処理がDockerエンジンによって行われます。

## Example
```bash
docker run hello-world
```

