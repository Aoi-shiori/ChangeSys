from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse

# Create your views here.


def book(request):

    username = request.GET.get('username')
    if username:
     return HttpResponse("这是图书首页")
    else:
        url=reverse('change_management:signin')
        print('#'*30)
        print(url)
        print('#' * 30)
        #return redirect(reverse('change_management:signin'))
        current_namespace = request.resolver_match.namespace
        return redirect(reverse('%s:signin'%current_namespace))


def login(request):
    return HttpResponse("这是登陆页面")

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

bookls = [
    '三国演义',
    '茶花女',
    '西游记',
    '红楼梦',
]


def booklist(request,page=0):
    return HttpResponse(bookls[page])