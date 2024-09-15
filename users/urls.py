from django.urls import path

from users.views import render_index

urlpatterns = [
    path('', render_index, name='index'),
]