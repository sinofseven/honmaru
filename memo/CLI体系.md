- コマンド体系
  - remove: stackの削除
  - deploy: stackの作成
  - changeset: changesetの表示/作成/実行 (分けるかなぁ?)
    - 分けるとすれば
      - list-changeset
      - exec-changeset
      - make-changeset: deployに含めればいい気もする
  - listen: CFnのcreate/update/delete stack (CI/CD用)
  - package: lambda/api用のオブジェクトをS3に上げてテンプレートを更新する
  - ???: moduleのインストールを行う
    - install?: なんとなく誤解を招きそうだけど、他に思いつかない
- 真・コマンド体系
  - remove: stackの削除
  - deploy: stackの作成
  - list-changeset
  - exec-changeset
  - package
  - install
  - listen
- 開発順序
  1. package
  1. deploy/remove
  1. listen
  1. list-changeset
  1. exec-changeset
  1. install