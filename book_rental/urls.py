from django.urls import path

from book_rental import views

app_name = 'book_rental'
urlpatterns = [
    # 書籍
    path('book/book_cont/', views.book_cont, name='book_cont'),  # 一覧コントローラー
    path('book/add/', views.book_add, name='book_add'),  # 登録
    path('book/mod/<int:book_no>/', views.book_edit, name='book_mod'),  # 編集
    path('book/', views.BookList.as_view(), name='book_list'),  # 一覧表示
]
