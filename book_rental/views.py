import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from book_rental.forms import BookForm
from book_rental.models import Book


logger = logging.getLogger(__name__)


class BookList(ListView):
    paginate_by = 10

    def post(self, request, *args, **kwargs):
        form_value = [
            self.request.POST.get('search_key', None),
            self.request.POST.get('search_val', None),
        ]
        request.session['form_value'] = form_value
        # 検索時にページネーションに関連したエラーを防ぐ
        self.request.POST = self.request.POST.copy()
        self.request.POST.clear()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # sessionに値がある場合、その値をセットする。（ページングしてもform値が変わらないように）
        search_key = ''
        search_val = ''
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            search_key = form_value[0]
            search_val = form_value[1]

        context['search_key'] = search_key  # 検索フォーム
        context['search_val'] = search_val  # 検索フォーム
        return context

    def get_queryset(self):
        # sessionに値がある場合、その値でクエリ発行する。
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            search_key = form_value[0]
            search_val = form_value[1]

            # 検索条件
            if "book_no" in search_key:
                logger.info("Search for book number")
                return Book.objects.filter(book_no__contains=search_val)

            if "name" in search_key:
                logger.info("Search for book name")
                return Book.objects.filter(name__contains=search_val)

            if "publisher" in search_key:
                logger.info("Search for book publisher")
                return Book.objects.filter(publisher__contains=search_val)

            if "category" in search_key:
                logger.info("Search for book category")
                return Book.objects.filter(category__contains=search_val)

            # すべて返す
            logger.info("View all books")
            return Book.objects.all()
        else:
            # すべて返す
            logger.info("View all books")
            return Book.objects.all()


def book_cont(request):
    """コントローラー分岐"""
    if 'cont_type' in request.POST:
        # POSTで送信した値をform変数に格納
        cont_type = request.POST.get('cont_type', None)

        if 'add' in cont_type:
            # 追加ボタンが押された場合の処理
            logger.info("To the add book screen")

            book = Book()
            form = BookForm(instance=book)  # book インスタンスからフォームを作成
            return render(request, 'book_rental/book_add.html', dict(form=form))
        else:
            # それ以外の場合book_no取得
            book_no = request.POST.get('book_no', None)

        if 'edit' in cont_type:
            # 編集ボタンが押された場合の処理
            logger.info("To the edit screen of the book")
            book = get_object_or_404(Book, pk=book_no)
            form = BookForm(instance=book)
            return render(request, 'book_rental/book_edit.html', dict(form=form, book_no=book_no))

        if 'del' in cont_type:
            """書籍の削除"""
            logger.info("Delete workbook")
            book = get_object_or_404(Book, pk=book_no)
            book.delete()
            return redirect('book_rental:book_list')

    # エラーページへ
    logger.error("Unexpected behavior!")
    return render(request, 'error.html')


def book_add(request):
    """書籍の追加"""
    book = Book()

    form = BookForm(request.POST, instance=book)  # POST された request データからフォームを作成
    if form.is_valid():  # フォームのバリデーション
        logger.info("Add books")
        book = form.save(commit=False)
        book.save()
        return redirect('book_rental:book_list')

    logger.info("Book addition failure")
    return render(request, 'book_rental/book_add.html', dict(form=form))


def book_edit(request, book_no=None):
    """書籍の編集"""
    if book_no:  # book_no が指定されている (修正時)
        book = get_object_or_404(Book, pk=book_no)

    if request.method == 'POST':
        logger.info("Book editing")
        form = BookForm(request.POST, instance=book)  # POST された request データからフォームを作成
        if form.is_valid():  # フォームのバリデーション
            book = form.save(commit=False)
            book.save()
            return redirect('book_rental:book_list')

    # 編集画面へ
    logger.info("Book editing failure")
    return render(request, 'book_rental/book_edit.html', dict(form=form, book_no=book_no))
