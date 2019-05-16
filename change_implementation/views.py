from django.shortcuts import render
from datetime import datetime

# Create your views here.
def change_implementation(request):
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
            {
                'name': '葫芦娃',
                'author': '曹雪芹',
                'price': 60.943534,
                'tody': datetime(year=2019,month=3,day=14,hour=11,minute=1,second=0),
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
    return render(request, 'change_implementation.html',context=connect)

