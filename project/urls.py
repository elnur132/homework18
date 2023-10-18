
from django.contrib import admin
from django.urls import path
from app.views import CreateName, ListName

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', ListName.as_view(), name = 'list'),
    path('add/', CreateName.as_view(), name='create')
]
