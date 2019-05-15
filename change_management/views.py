from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
from datetime import datetime

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


def index (request):
    connect={
        'books':[
            {
                'name'  :'三国演义',
                'author':'罗贯中',
                'price' : 55.343254,
                'tody': datetime.now(),
            },
            {
                'name'  :'茶花女',
                'author':'小杜马',
                'price' : 60.503953,
                'tody': datetime.now(),
             },
            {
                'name'  :'西游记',
                'author':'吴承恩',
                'price' : 100.49553,
                'tody': datetime.now(),
             },
            {
                'name'  :'红楼梦',
                'author':'曹雪芹',
                'price' : 90.943534,
                #'tody': datetime.now(),
             },
        ],
        'person':{
            'use':'小明',
            'pw': '222',
            'are': '杭州',

        },

        "comment":[
            # "写的很不错",
            # "非常的精彩"
        ]

    }
    return render(request,'index.html',context=connect )