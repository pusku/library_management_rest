from django.db.models import Q
from rest_framework.generics import (
  ListAPIView, CreateAPIView,
  RetrieveUpdateAPIView,
  RetrieveAPIView,
  DestroyAPIView
)
from rest_framework import pagination
from rest_framework.permissions import (
 IsAuthenticatedOrReadOnly
)
from ...core.pagination import PostLimitOffsetPagination
from .serializers import TABLE, BookSerializer, BookCreateSerializer, TimeSeriesSerializer
from app_dir.author.models import Author 
from app_dir.book.models import Book
# from rest_framework.viewsets import ReadOnlyModelViewSet
# from drf_renderer_xlsx.mixins import XLSXFileMixin
# from drf_renderer_xlsx.renderers import XLSXRenderer
import pandas as pd
from io import BytesIO as IO
from django.http import HttpResponse
from django.views import View
from rest_pandas import PandasView, PandasScatterSerializer



class BookListByAuthor(ListAPIView):
    serializer_class = BookSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self):
        author = Author.objects.get(id=self.kwargs['pk'])
        return Book.objects.filter(author=author)

class BookListAPIView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = TABLE.objects.all()

        page_size_key = 'page_size'
        page_size = self.request.GET.get(page_size_key)
        query = self.request.GET.get('q')
        pagination.PageNumberPagination.page_size = page_size if page_size else 10

        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

        return queryset_list.order_by('-id')


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = TABLE.objects.all()


class BookDetailAPIView(RetrieveAPIView):
    queryset = TABLE.objects.all()
    serializer_class = BookSerializer


class BookDeleteAPIView(DestroyAPIView):
    queryset = TABLE.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer


class BookUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = TABLE.objects.all()
    serializer_class = BookSerializer

class ExcelFileDownloadView(PandasView):
    queryset = Book.objects.all()
    serializer_class = TimeSeriesSerializer