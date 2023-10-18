*Todoアプリに必要な機能*
タスクに必要な項目
-- TODOの開始予定日、実際の開始日、終了予定日、実際の終了日
タスクを操作するための項目
1. TODOリストを表示する
2. TODOタスクを追加する
3. TODOタスクの説明文を変更する
4. TODOタスク自体を削除ウする
5. TODOタスクに「作業前」「作業中」「作業完了」フラグを立てる
6. TODOタスクから「完了」フラグを外す
7. カレンダーでTODOの開始予定日、実際の開始日、終了予定日、実際の終了日を確認できるようにする
8. TODOを複数のユーザで共有できるようにする


versionによりテストを行うときには https://zenn.dev/sh0nk/scraps/a981a1e100f62c
docker-compose run --entrypoint "poetry run pytest --asyncio-mode=auto" demo-app
のコマンドで行う

2023/10/13
1. TODOの作成、編集、削除機能
TODOの作成は可能 create_task
TODOの編集は編集する際にidを指定してdefaltから変更する必要があるため、変更したい項目の確認をしながら変更ができない update_task
TODOの削除は可能 delete_task

TODOのDone(完了フラグ)がうまく動かない -> 動いた
TODOのDone,in_work,before_workが同時に選択できないようにする必要がある

2. TODOの内容
TODOの内容
TODOの開始予定日
TODOの開始日
TODOの終了予定日
TODOの終了日

日付の
