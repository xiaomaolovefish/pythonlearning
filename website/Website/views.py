# coding:utf-8
from django.shortcuts import render

# Create your views here.
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Website.settings")# project_name 项目名称
django.setup()
import json
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext,loader,Context


#导入发布房源的表单和表
#from ShareHouse.models import ShareH
from ShareHouse.models import ShareH
from ShareHouse.models import ShareHForm
from ShareHouse.form import Share_H
def index1(request):
    if request.method == 'POST':# 当提交表单时
     
        form = AddForm(request.POST) # form 包含提交的数据
         
        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
     
    else:# 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})
def learn(request):
    data = [1,2,3,4]
    return render(request, 'learn.html', {'data': data})
def learn3(request):
    return render(request, 'learn3.html')
 
def learn2(request):
    if request.method == 'get':# 当提交表单时
        form = Share_H(request.GET)
        if form.is_valid():
            a = form.cleaned_data
            print a
            a.save()
            return HttpResponseRedirect('/index.html') # 跳转
            #return render(request, 'index.html', {'form': form})
           # new_form = ShareH(name = form['name'], adress = form['adress'], price = form['price'], detail = form['detail'], )
          
        
     
    else:# 当正常访问时
        form = Share_H()
    return render(request, 'learn2.html', {'form': form})

def learn1(request):
    return render(request, 'learn1.html')

#def scene_update(request):
  #  if request.method == "POST":
 #           name = request.POST.get('name')
 #           status = 0
 #           result = "Error!"
 #           return HttpResponse(json.dumps({
 #               "status": status,
 #               "result": result
 #           }))
def scene_update(request):
    if request.method == "POST":
            name = request.POST.get('name')
            print name
            status = 0
            result = "Error!"
            return HttpResponse(json.dumps({
                "status": status,
                "result": result
            }))

def ajax_list(request):
    a = list(range(100))
    return HttpResponse(json.dumps(a), content_type='application/json')

def search(request):
    a = Poll.objects.all()
    return HttpResponse(json.dumps(a), content_type='application/json')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

#使用模板在前端显示后台数据
def share_house(request):
    posts = ShareH.objects.all()
    t = loader.get_template('share_house.html')
    c = Context({ 'posts':posts})
    return HttpResponse(t.render(c))

   

def index(request):
    return render(request, 'index.html')

def H_add(request):
    if request.method == 'GET':# 当提交表单时
     
        form = ShareHForm(request.GET) # form 包含提交的数据
        template = 'share_house.html'
         
        if form.is_valid():# 如果提交的数据合法
            form.save()
            return HttpResponseRedirect('/index/')
     
    else:# 当正常访问时
        form = ShareHForm()
   # return render_to_response('share_house.html', form, context_instance=RequestContext(request))
    return render(request, template,
                get_context(request, form))
def H_show(request):
    a = ShareH.objects.all()
    return HttpResponse('share_house.html',json.dumps(a), content_type='application/json')
   
def home(request):
    if request.method == 'GET':# 当提交表单时
     
        form = ShareHForm(request.GET) # form 包含提交的数据
       
         
        if form.is_valid():# 如果提交的数据合法
            form.save()
            return HttpResponseRedirect('/index/')
     
    else:# 当正常访问时
        form = ShareHForm()
    return render(request, 'home.html', {'form': form})
