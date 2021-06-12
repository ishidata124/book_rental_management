from django.contrib import admin
from book_rental.models import Book


# admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_no', 'name', 'publisher', 'category',)  # 一覧に出したい項目
    list_display_links = ('book_no', 'name',)  # 修正リンクでクリックできる項目


admin.site.register(Book, BookAdmin)
