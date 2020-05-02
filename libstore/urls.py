from django.urls import path
from . import views

urlpatterns = [
    path('', views.library, name='library'),
    path('books/<slug:slug>/', views.shelf, name='book_details'),
    path('createBook', views.create_book, name='create_book'),
    
]

