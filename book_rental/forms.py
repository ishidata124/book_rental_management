from django.forms import ModelForm
from book_rental.models import Book
from django import forms


class BookForm(ModelForm):
    """書籍のフォーム"""

    class Meta:
        model = Book
        fields = ('book_no', 'name', 'publisher', 'category',)


class SearchForm(forms.Form):
    search_key = forms.CharField(
        initial='',
        required=True,
    )
    search_val = forms.CharField(
        initial='',
        required=False,  # 必須ではない
    )
