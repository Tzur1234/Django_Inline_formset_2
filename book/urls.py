from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('authors/', views.AuthorListView.as_view(), name="author_list").
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name="author_detail")
]