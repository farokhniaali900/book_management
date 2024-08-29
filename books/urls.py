from django.urls import path
from . import views


urlpatterns = [
    path('' , views.book_list , name='book_list'),
    path('book/<int:pk>/' , views.book_detail , name='book_detail'),
    path('book/add/' , views.book_add , name='book_add'),
    path('book/edit/<int:pk>/' , views.book_edit , name='book_edit'),
    path('book/delete/<int:pk>/' , views.book_delete , name='book_delete'),
    path('book/search/' , views.book_search , name='book_search'),
    path('book/filter/' , views.filter , name='book_filter'),
    path('book/filter/delete/' , views.book_filter_delete , name='book_filter_delete'),
]