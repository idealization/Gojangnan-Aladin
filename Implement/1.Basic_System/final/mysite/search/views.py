from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from search.models import Book
from django.db.models import Q


def index(request):

    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    book_list = Book.objects.order_by('title')  # title 순으로 정렬

    if kw:
        book_list = book_list.filter(
            Q(title__icontains=kw) |  # 제목검색
            Q(ISBN__icontains=kw) |  # ISBN 검색
            Q(author__icontains=kw) |  # 저자 검색
            Q(original_title__icontains=kw)  # original title 검색
        ).distinct()

    paginator = Paginator(book_list, 20)  # 페이지당 20개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'book_list': page_obj, 'page': page, 'kw': kw}  # page와 kw가 추가되었다.
    return render(request, 'search/book_list.html', context)  # render 함수는 html 파일로 변환한다.


def detail(request, book_isbn):

    book = get_object_or_404(Book, ISBN=book_isbn)  # 404 페이지를 나타나게 한다.
    context = {'book': book}
    return render(request, 'search/book_detail.html', context)
