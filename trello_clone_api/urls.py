
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('apps.users.api.urls')),
    path('boards/', include('apps.boards.api.routers'))
]
