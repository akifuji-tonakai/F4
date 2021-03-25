# Favorite4
**好きなものを選択し、twitterに投稿するアプリ**<br>
URL*~→メンテ中😉

## 利用方法

 1. twitterアカウントを用意し、連携を行う
 2. 本アプリで画像を選択する
 3. 投稿で完了 連携したアカウントにツイートされる<br>
<a href="https://gyazo.com/6021bae3e02d95300344b79043976741"><img src="https://i.gyazo.com/6021bae3e02d95300344b79043976741.png" alt="samlple" width="434"/></a>

# 目指した課題解決

#### 画像を投稿させる
  診断メーカーや攻略サイトのツイート機能はほとんど画像投稿されず、カード(url)の表示のみだ。その理由としては、
 「twitterの連携権限を小さくし、アプリのセキュリティの要求値を小さくする」、または「連携せずとも気軽に投稿できる」といったものを意図していると推測される。
 連携権限を設定しなければ、不正アクセスでトークンを盗まれ、意思に反するツイートや情報漏洩などの責任を負うことはないからだ。こういった利点から、twitter連携の権限が小さいor全くないサービスがメジャーである。<br>
 
  一方で見られる現象としては、「画像の付属投稿」が極端に見られないことだ。これは先の権限の話に付随する。Oauth認証システムに使っている分だと、tweet投稿の権限が貰えていない、ということだ。<br>
 
  この点が他のtwitter向けアプリケーションとの差別化を図る着想に至った。**画像を投稿させる**機能を作ろう！という。
 何故画像を投稿させることに固執しているかというと、やはり文だけで目立たせるのには限界があり、画像であればアイキャッチも容易であるからだ。<br>
 
## 実装画面

### 管理者専用
 - データ作成
 <a href="https://gyazo.com/5bbf0c3f0483900afbf451126aafcdee"><img src="https://i.gyazo.com/5bbf0c3f0483900afbf451126aafcdee.png" alt="Image from Gyazo" width="1400"/></a>
 <br>
 
 ### ユーザー画面
 
 - ログイン
 <a href="https://gyazo.com/2656cb0189d380bb605b455a1701403c"><img src="https://i.gyazo.com/2656cb0189d380bb605b455a1701403c.png" alt="Image from Gyazo" width="1400"/></a>
 <br>
 
 - 一覧画面
 <a href="https://gyazo.com/5fafcdeedb07599ab4b4e671ac4459a6"><img src="https://i.gyazo.com/5fafcdeedb07599ab4b4e671ac4459a6.png" alt="Image from Gyazo" width="1400"/></a>
 <br>
 
 - **選択⇨投稿**
 <a href="https://gyazo.com/60de500e42fb5429842fdfff5d8c29b7"><img src="https://i.gyazo.com/60de500e42fb5429842fdfff5d8c29b7.gif" alt="Image from Gyazo" width="1400"/></a>
 
## 機能一覧
 - ログインページ(twitter連携)
 - コンテンツの一覧表示
 - 画像選択・投稿ページ
 - 利用規約ページ
 - 退会ページ
 
 ## ローカル
 ローカル環境での動かし方
 - 適当なdjangoアプリ作ってシークレットキーを入手
 - pip install
 - mysqlの初期設定
 - twitterやdbの環境変数は各自設定してください

 ## ER図
<a href="https://gyazo.com/6be32d7f07d63132e5dccbc6d6b2718e"><img src="https://i.gyazo.com/6be32d7f07d63132e5dccbc6d6b2718e.png" alt="Image from Gyazo" width="704"/></a>

 ## 実装予定の機能
 - サブクラスやキャラで絞る
 - 管理者側のキャラ追加機能
 - 4つに絞る機能
