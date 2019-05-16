#encoding:utf-8
from django.urls import path,re_path
from . import views

app_name = 'change_management'

urlpatterns = [
    # path('',views.book,name='index'),
    # path('login/',views.login,name='signin'),
    # path('book_lis/<book_id>/<category_id>/', views.book_lis,name='book_lis'),
    # path('book_author/', views.book_author,name='book_author'),
    # #path('book_publisher/<path:publisher_id>', views.book_publisher,name ='book_publisher'),
    # re_path(r'^book_publisher/(?P<publisher_id>\d{4})/$',views.book_publisher),
    # path('booklist',views.booklist,name='bklist'),
    # path('booklist/page/<int:page>/',views.booklist,name = 'page'),
    # path('index/',views.index,name ='index2'),
    path('change_implementation/',views.change_implementation,name='implementation'),
]

