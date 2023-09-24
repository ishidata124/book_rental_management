# 本貸し出し管理
## このアプリについて
本の貸し出し管理の管理者用アプリ。必要時にだけ立ち上げて使用する。
- ログイン画面は別途用意するか、管理画面をそのまま使用（検討中）
- サンプルの為**DB**は**sqlite3**を使用  
  ※昔作成したものを少し直したものになります。

## 構成
- Python 3.8
- Django 4.1
- django-bootstrap4

## 実行方法
1.venv環境作成
```
# make venv directory
python3 -m venv venv

# change directory
cd venv

# Scripts配下のファイルを実行すると仮想が起動。各システムに合わせて実行。
# windowsの場合
Scripts/Activate.ps1
# ※セキュリティではじかれる場合、PowerShellを管理者権限で実行後下記コマンド実行。
set-executionpolicy remotesigned
```
2.依存インストール
```
# pip upgrade
pip install --upgrade pip

# 依存 install
python -m pip install requests==2.3.0
python -m pip install Django==4.1
python -m pip install django-bootstrap4
```
3.実行
```
# execute
python ../manage.py runserver
```
4.トラブルシューティング
```
# ※下記エラーが出る場合
# FileNotFoundError: [Errno 2] No such file or directory: 'C:\\var\\log\\book_rental_management\\app.log'

# make directory
mkdir -p /var/log/book_rental_management

# make file command for linux
touch /var/log/book_rental_management/app.log

# make file fcommand or windows
New-Item -Type File /var/log/book_rental_management/app.log
```

## 接続可能URL
```URL
DEBUG = False
http://127.0.0.1:8000/ ←アクセス不可

http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/book_rental/book/
http://127.0.0.1:8000/book_rental/book/add/
http://127.0.0.1:8000/book_rental/book/mod/5/ ←アクセス不可
http://127.0.0.1:8000/book_rental/book/del/7/ ←アクセス不可
```

## 管理者ユーザー
```
id: admin
pw: root
```

## 今後の予定
- テストケースを作成していく
- Docker化  
※ 2023/09/24 この資材は凍結
