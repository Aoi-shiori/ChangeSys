from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def book_lis(request,book_id,category_id):
    text = "您获取的图书ID是: %s,图书分类是%s" % (book_id,category_id)
    return HttpResponse(text)
def book_author(request):
    #author_id = request.GET.get('id')
    author_id = request.GET['id']
    text = "作者是%s" % author_id
    return HttpResponse(text)
def book_publisher(request,publisher_id):
    text = '出版社是%s' % publisher_id
    return HttpResponse(text)
