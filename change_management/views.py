from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.db import connection
from datetime import datetime


# Create your views here.
def get_corsor():
    return connection.cursor()

def changemanagement(request):
    cursor =get_corsor()
    cursor.execute('select*from change_management')
    changemanagements = cursor.fetchall()
    return render(request, 'change_management.html', context={'changemanagements': changemanagements})

def changemanagement_add(request):
    if request.method =='GET':
        return render(request,'changemanagement_add.html')
    else:
        AssociationTypes = request.POST.get("AssociationTypes")
        AssociatedNumber = request.POST.get("AssociatedNumber")
        Datebase = request.POST.get("Datebase")
        Informant = request.POST.get("Informant")
        ChangeContent = request.POST.get("ChangeContent")
        cursor = get_corsor()
        cursor.execute("insert into change_management(ChangeID,AssociationTypes,AssociatedNumber,Datebase,Informant,FillTime,Reviewer,ReviewStatus,ReviewContent,ChangeContent,AuditTime) value (null,'%s','%s','%s','%s','%s',null, null,null,'%s',null)" % (AssociationTypes, AssociatedNumber, Datebase, Informant, datetime.now(), ChangeContent))
        return redirect(reverse('index_home:index_management'))

def changemanagement_delete (request):
    if 'delete'in request.POST:
        if request.method == 'POST':
            ChangeID =request.POST.get("ChangeID")
            cursor =get_corsor()
            cursor.execute("delete from change_management where ChangeID =%s" %ChangeID)
            return redirect(reverse('index_home:index_management'))
        else:
            raise RuntimeError("删除图书的method错误！")
    else:
        return HttpResponse("编辑还没做")
