from django.urls import path
from . import views

app_name = 'bookauthor'

urlpatterns = [
    path('', views.index, name='book'),
    path('books/<int:id_book>', views.book_details),
    path('author', views.index_author, name='author'),
    path('author/<int:id_author>', views.author_details),
    # path('delete/<int:id_author>', views.author_details),
]
