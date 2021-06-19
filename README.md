# 本貸し出し管理
##このアプリについて
本の貸し出し管理の管理者用アプリ。必要時にだけ立ち上げて使用する。  
・ログイン画面は別途用意するか、管理画面をそのまま使用（検討中）  
・サンプルの為**DB**は**sqlite3**を使用  
・コードビルド起動用ファイル＆ECS起動用設定ファイルは内容未記入




##接続可能URL
```URL
DEBUG = False
http://127.0.0.1:8000/ ←アクセス不可

http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/book_rental/book/
http://127.0.0.1:8000/book_rental/book/add/
http://127.0.0.1:8000/book_rental/book/mod/5/ ←アクセス不可
http://127.0.0.1:8000/book_rental/book/del/7/ ←アクセス不可

python manage.py runserver
```