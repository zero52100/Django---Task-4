from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
]
