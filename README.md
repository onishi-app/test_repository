# GitHubにPushする手順
https://qiita.com/shizuma/items/2b2f873a0034839e47ce

オリジン追加
> git remote add origin プッシュするURL

管理情報表示
> git status

push対象ファイル追加（-A で全て追加）
> git add -A

管理情報表示
> git status

コミット
> git commit -m "{コメント}"

GitHubにアップロード
> git push -u origin <ブランチ名>

pushに失敗したら次のコマンドでOKだよ
> git fetch
その次に
> git merge

sampleですー。

kintai branch
