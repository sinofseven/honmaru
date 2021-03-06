# Honmaru 〜 現在鋭意作成中です 〜
このフレームワーム "Honmaru"はSAM(※)用Serverless Frameworkを目指しています。

(*) [Serverless Application Model](https://github.com/awslabs/serverless-application-model)

# 作業予定
- [x] 設計
  - [x] やりたいことを固める
  - [x] コマンド体系を作る
  - [x] マイルストーンを作る
- [ ] 事前検証
  - [ ] ~~```aws cloudformation package```でやっていることを理解する~~ 当面行わない
  - [x] Travis CIの使い方を調べる
  - [x] Python 3系におけるCLI Tool用フレームワークの選定 ([Click]()を使用することに決定)
  - [ ] Pythonでモジュールを公開する方法を調べる
  - [x] changesetを実行する際にRequestId(?)を指定可能かどうか (指定可能)
- [ ] 実装
  - [ ] 設定ファイル, 環境変数, コマンド引数の優先順位の作成とロード機構の実装
  - [ ] packageの実装
  - [ ] deploy/removeの実装
  - [ ] parameter機能の実装
  - [ ] changeset関連の機能
    - [ ] deployコマンドでチェンジセットだけ作って実行しないオプションの実装
    - [ ] list-changesetコマンドの実装
    - [ ] exec-changesetコマンドの実装
  - [ ] モジュールインストールの実装
  - [ ] モジュールインストールの際にDockerを使用するためのオプションを実装
- 次期開発用検証
  - [ ] ~~```aws cloudformation package```でやっていることを理解する~~ 当面行わない
