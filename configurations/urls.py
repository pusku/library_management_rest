from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest')),
    path('api-token-auth', obtain_jwt_token),
    path('user/', include(('app_dir.user.urls', 'user'), namespace='user')),
    path('api/user/', include(('app_dir.user.api.urls', 'user_api'), namespace='user_api')),
    path('api/module/', include(('app_dir.module.api.urls', 'module_api'), namespace='module_api')),
    path('api/author/', include(('app_dir.author.api.urls', 'author_api'), namespace='author_api')),
    path('api/book/', include(('app_dir.book.api.urls', 'book_api'), namespace='book_api'))
]

