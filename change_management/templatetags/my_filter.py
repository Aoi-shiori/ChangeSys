from django import template
from datetime import datetime

register = template.Library()

@register.filter
def time_since(value):
    if not isinstance(value,datetime):
        return value
    now =datetime.now()
    timestamp=(now-value).total_seconds()
    if timestamp<60:
        return '刚刚'
    elif  timestamp>=60 and timestamp <=60*60:
        return '%s钟前'%int(timestamp/60)
    elif  timestamp>=60*60 and timestamp <=60*60*24:
        return '%s小时前'%int(timestamp/(60*60))
    elif  timestamp>=60*60*24 and timestamp <60*60*24*30:
        return '%s天前' %int(timestamp/(60*60*24))
    else:
        return value.strftime("%Y-%m-%d %H:%M")
register.filter("time_since",time_since)