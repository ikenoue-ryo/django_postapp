# アプリ概要
SNSの投稿アプリ

## 主な仕様
SNSと同様に投稿ができるWebアプリです。タグ付けやタグ検索、フォロー機能、コメント投稿機能、など実装しています。

## 注意事項
多少、バグがでますので適宜修正ください。PCサイトのみ制作しスマホは未制作です。

## バージョン
- python 3.6.1
- Django 3.0.5

## 起動
- docker-compose -f docker-compose.prod.yml up -d --build
- docker-compose -f docker-compose.prod.yml exec django python manage.py migrate --noinput
- docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic --no-input --clear
- docker-compose -f docker-compose.prod.yml exec django python manage.py createsuperuser

## 画面イメージ
<img src="https://user-images.githubusercontent.com/61681360/88868586-8ee56580-d24b-11ea-9ca0-e88033e6f862.png">
<img src="https://user-images.githubusercontent.com/61681360/88868886-5003df80-d24c-11ea-917e-d99528f0e1af.png">
<img src="https://user-images.githubusercontent.com/61681360/88868922-6c078100-d24c-11ea-82f8-3848e16842be.png">