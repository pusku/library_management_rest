from django.urls import path
from .views import (
   BookCreateAPIView,
   BookListAPIView,
   BookDeleteAPIView,
   BookDetailAPIView,
   BookUpdateAPIView,
   BookListByAuthor,
   ExcelFileDownloadView
)

urlpatterns = [
    path('', BookListAPIView.as_view(), name='list'),
    path('create', BookCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', BookDeleteAPIView.as_view(), name='delete'),
    path('detail/<int:pk>/', BookDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', BookUpdateAPIView.as_view(), name='update'),
    path('author/<int:pk>/', BookListByAuthor.as_view(), name='book_by_author'),
    path('book_excel', ExcelFileDownloadView.as_view(), name='book_excel')
]
