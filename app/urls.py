from django.contrib import admin
from django.urls import path
from genres.views import genreCreateListView, GenreRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/',genreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>',GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]
