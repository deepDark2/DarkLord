from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping

from web.models import Guest, Article


@request_mapping("/article")
class ArticleView(View):

    @request_mapping("/a", method="get")
    def all(self,request):
        obj = Article.objects.all();
        context = {
            'center':'article/list.html',
            'objs':obj
        };
        return render(request,'home.html',context);
    # guest/g/3
    @request_mapping("/g/<int:pk>/", method="get")
    def get(self,request,pk):
        data = Article.objects.get(id=pk);
        context = {
            'center':'article/get.html',
            'obj':data
        };
        return render(request,'home.html',context);

    @request_mapping("/iv", method="get")
    def insertview(self,request):
        context = {
            'center':'article/add.html',
        };
        return render(request,'home.html',context);

    @request_mapping("/i", method="get")
    def insert(self,request):
        name = request.GET['name'];
        price = request.GET['price'];
        obj = Article(name=name, price=price);
        obj.save();
        return redirect('/article/a');

    @request_mapping("/d/<int:pk>", method="get")
    def delete(self,request,pk):
        obj = Article.objects.get(id=pk);#models.py에서 자동생성된 id를 가져옴
        obj.delete();
        return redirect('/article/a');

    @request_mapping("/uv/<int:pk>/", method="get")
    def updateview(self, request, pk):
        obj = Article.objects.get(id=pk);
        context = {
            'center': 'article/update.html',
            'obj': obj
        };
        return render(request, 'home.html', context);
    #값을 models.py에서 가져롱때는 models내 테이블 클래스명.objects.get();
    #값을 태그에서(<form>)가져올땐 request.GET/POST['<form>내에 name으로 지정된 이름'];, 이 값을 변수 하나에 지정해서 사용.

    @request_mapping("/u", method="get")
    def update(self,request):
        name = request.GET['name'];
        price = request.GET['price'];
        id = request.GET['id'];
        obj = Article.objects.get(id=id);
        obj.name = name;
        obj.price = price;
        obj.save();
        return redirect('/article/g/'+id)
