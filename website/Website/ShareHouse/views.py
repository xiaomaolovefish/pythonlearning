# coding:utf-8
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Website.settings")# project_name 项目名称
django.setup()
import json
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext,loader,Context
import datetime
from django.db.models import Q
from django.views.generic.list import ListView

#导入发布房源的表单和èﾡ?
#from ShareHouse.models import ShareH
from models import ShareH
from models import ShareHForm
from models import ShareForm
from form import search_list
from form import AddProfileForm

#from form import Share_H
def index1(request):
    if request.method == 'POST':# 当提交表单时
     
        form = AddForm() # form 包含提交的数æﾍ?
         
        if form.is_valid():# 如果提交的数据合æﾳ?
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
 
def shadd(request):
    if request.method == 'POST':# 当提交表单时
        form = ShareHForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/H_show') # 跳转
       # if form.is_valid():
            #a = form.cleaned_data
            #a = form.clean()
           # print a
           # a.save()
      
            #return render(request, 'index.html', {'form': form})
           # new_form = ShareH(name = form['name'], adress = form['adress'], price = form['price'], detail = form['detail'], )
          
        
     
    else:# 当正常访问时
        form = ShareHForm()
    return render(request, 'shadd1.html', {'form': form})

def update_data(request):
    query = request.GET.get('q') #request.GET是一个类字典对象，它包含所有GET请求的参数，这里表示取得nameäﾸ?q'的参数åﾀ?
    if query:
        #results = 'You just sent %s' % query
        results = ShareH.objects.filter(name=query)
        t = loader.get_template('H_list.html')
        c = Context({ 'results':results})
        return HttpResponse(t.render(c))
    else:
        results = []
    return render(request,'H_list.html', {'results': results})
 
     

def H_show(request):
    a = ShareH.objects.all()
    #a = ShareH.objects.filter(name=444)
    #a = ShareH.objects.filter()
    #a = ShareH.objects.get(name=444)
    #f = ShareHForm(instance=a)
    #return render(request, 'H_show.html', {'f': f})
    #return HttpResponse('H_show.html',json.dumps(a), content_type='application/json')
    return render_to_response("H_show.html",{'a': a})
    #return render_to_response("H_show.html",{'f': f})

def show(request):
    a = get_object_or_404(ShareH,pk=1) 
    #a = ShareH.objects.filter(name=444)
    #a = ShareH.objects.filter()
    #a = ShareH.objects.get(name=444)
    f = ShareHForm(instance=a)
    #return render(request, 'H_show.html', {'f': f})
    #return HttpResponse('H_show.html',json.dumps(a), content_type='application/json')
    #return render_to_response("show.html",{'a': a})
    return render_to_response("show.html",{'f': f})

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

#使用模板在前端显示后台数æﾍ?
def share_house(request):
    posts = ShareH.objects.all()
    t = loader.get_template('share_house.html')
    c = Context({ 'posts':posts})
    return HttpResponse(t.render(c))

   

def index(request):
    #return render(request, 'index.html')
    form = ShareHForm()
    return render(request, 'index.html', {'form': form})

def H_add(request):
    if request.method == 'GET':# 当提交表单时
     
        form = ShareHForm(request.GET) # form 包含提交的数æﾍ?
        template = 'share_house.html'
         
        if form.is_valid():# 如果提交的数据合æﾳ?
            form.save()
            return HttpResponseRedirect('/index/')
     
    else:# 当正常访问时
        form = ShareHForm()
   # return render_to_response('share_house.html', form, context_instance=RequestContext(request))
    return render(request, template,
                get_context(request, form))
   
def home1(request):
    if request.method == 'GET':# 当提交表单时
     
        form = ShareHForm(request.GET) # form 包含提交的数æﾍ?
       
         
        if form.is_valid():# 如果提交的数据合æﾳ?
            form.save()
            return HttpResponseRedirect('/index/')
     
    else:# 当正常访问时
        form = ShareHForm()
    return render(request, 'home.html', {'form': form})

def home(request):
    a = ShareH.objects.all()
    return render(request,"home.html",{'a': a})

def house_info(request):
    t = loader.get_template("house_info.html")
    myid = request.GET.get("id")
    a = get_object_or_404(ShareH,pk=myid)
  
    house = {"title": a.name,"adress":a.adress,"price":a.price,"detail":a.detail,"img":a.InputFile}
    c = Context(house)
    return HttpResponse(t.render(house))
    

def search_list1(request):
    q = request.GET['q']
    results = ShareH.objects.filter(name=q)
    return render(request,"H_list.html",{'results':results})

#模糊查询
def search_list(request):
    q = request.GET['q']
    results = ShareH.objects.filter(Q(name__icontains=q) | Q(detail__icontains=q))
    #return render(request,"H_list.html",{'results':results})   
    return render(request,"H_list.html",{'results':results})

def homepage(request):
    if request.method == 'POST':# 当提交表单时
     
        form = ShareHForm(request.POST or None, request.FILES or None) # form 包含提交的数æﾍ?
       
         
        if form.is_valid():# 如果提交的数据合æﾳ?
            form.save()
            return HttpResponseRedirect('/index/')
     
    else:# 当正常访问时
        form = ShareHForm()
    return render(request, 'homepage.html', {'form': form})

from django.views.generic.edit import CreateView
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView


def p_list(request):
    results = Profile.objects.all()
    return render_to_response("p_list.html",{'results': results})


class ProfileActionMixin(object):
    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(ArticleActionMixin, self).form_valid(form)
from models import Profile
class AuthorCreate(CreateView):
    model = Profile
    fields = ['name','img']
    #template_name_suffix = 'create_author'  
    success_url = '/p_list/'
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(AuthorCreate, self).form_valid(form)
class ProfileUpdateView(UpdateView):
    form_class = AddProfileForm
    model = Profile
   # fields = ['name','img']
    template_name_suffix = '_update_form'
    success_url = '/p_list/'
   
    def get_object(self):
        self.object = Profile.objects.get(pk=self.request.user.pk)
        return self.object
       # return Snippet(create_by = self.request.user)
   
   # def get_form(self, form_class):
      #  return self.form_class(self.request.user, **self.get_form_kwargs())

def gupiao(request):
    now=datetime.datetime.now()
    date=now.strftime('%Y%m%d')
    gpinfo_list = []
    for i in range(10):
        gpinfo_list.append({"title": "%s" % i, "url": "%s_%s.html" % (date,i)})

    return render(request, "gupiao.html", {"gpinfo_list": gpinfo_list})
    #return render("request", "gupiao.html", {"k1": {"tile": 12, "name": "aaa"})


