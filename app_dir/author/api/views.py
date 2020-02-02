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
from .serializers import TABLE, AuthorSerializer, AuthorCreateSerializer


class AuthorListAPIView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AuthorSerializer
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


class AuthorCreateAPIView(CreateAPIView):
    serializer_class = AuthorCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = TABLE.objects.all()


class AuthorDetailAPIView(RetrieveAPIView):
    queryset = TABLE.objects.all()
    serializer_class = AuthorSerializer


class AuthorDeleteAPIView(DestroyAPIView):
    queryset = TABLE.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AuthorSerializer


class AuthorUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = TABLE.objects.all()
    serializer_class = AuthorSerializer
