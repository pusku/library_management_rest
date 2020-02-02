from django.urls import path
from .views import (
   AuthorCreateAPIView,
   AuthorListAPIView,
   AuthorDeleteAPIView,
   AuthorDetailAPIView,
   AuthorUpdateAPIView
)

urlpatterns = [
    path('', AuthorListAPIView.as_view(), name='list'),
    path('create', AuthorCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', AuthorDeleteAPIView.as_view(), name='delete'),
    path('detail/<int:pk>/', AuthorDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', AuthorUpdateAPIView.as_view(), name='update')
]
