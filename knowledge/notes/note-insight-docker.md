---
id: note-insight-docker
title: Dockerはアプリをコンテナ単位で動かすためのプラットフォーム
created: 2026-05-29
source: [[2026-05-29_insight_docker-basics]]
---

## Summary
- Dockerは、アプリと実行に必要な環境をまとめて扱うためのプラットフォームです。
- コンテナという単位でアプリを動かすことで、環境差による動作のずれを減らせます。
- RailsアプリやPostgreSQLなどを同じ開発環境で動かしたいときに役立ちます。

## Tags
#docker #container #development #basics

## Links
- [[note-insight-docker-container]]
- [[note-insight-docker-image]]
- [[note-insight-docker-engine]]

## Body
Dockerは、アプリケーションとその実行に必要な環境をまとめ、コンテナとして動かしやすくするためのプラットフォームです。開発者ごとにPCの状態が違っても、同じような実行環境を用意しやすくなります。

たとえばRailsアプリ本体とPostgreSQLをDockerで起動すれば、チームメンバーが近い条件で開発できます。「自分のPCでは動くが、他の環境では動かない」という問題を減らすために使われます。

## Example
- RailsアプリをDockerで起動する
- PostgreSQLもDockerで起動する
- チームで同じ開発環境をそろえる

