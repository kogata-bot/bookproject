from django.urls import path
from .views import (
    ListBookView,
    DetailBookView,
    CreateBookView,
    DeleteBookView,
    UpdateBookView,
    CreateReviewView,
    index_view,
    )

urlpatterns = [
    path('',index_view,name='index'),
    path('book/', ListBookView.as_view(),name='list-book'), #reverse-lazy(name)
    path('book/<int:pk>/detail/',DetailBookView.as_view(),name='detail-book'),
    path('book/create/',CreateBookView.as_view(),name='create-book'),
    path('book/<int:pk>/delete/',DeleteBookView.as_view(),name='delete-book'),
    path('book/<int:pk>/update/',UpdateBookView.as_view(),name='update-book'),
    path('book/<int:book_id>/review/',CreateReviewView.as_view(),name='review'),
]