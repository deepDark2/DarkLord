from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping

from web.models import Guest


@request_mapping("/guest")
class GuestView(View):

    @request_mapping("/a", method="get")
    def all(self,request):
        obj = Guest.objects.all();
        context = {
            'center':'guest/list.html',
            'objs':obj
        };
        return render(request,'home.html',context);
    # guest/g/3
    @request_mapping("/g/<int:pk>/", method="get")
    def get(self,request,pk):
        data = Guest.objects.get(id=pk);
        context = {
            'center':'guest/get.html',
            'obj':data
        };
        return render(request,'home.html',context);

    @request_mapping("/iv", method="get")
    def insertview(self,request):
        context = {
            'center':'guest/add.html',
        };
        return render(request,'home.html',context);

    @request_mapping("/i", method="get")
    def insert(self,request):
        title = request.GET['title'];
        content = request.GET['content'];
        obj = Guest(title=title, content=content);
        obj.save();
        return redirect('/guest/a');

    @request_mapping("/d/<int:pk>", method="get")
    def delete(self,request,pk):
        obj = Guest.objects.get(id=pk);#models.py에서 자동생성된 id를 가져옴
        obj.delete();
        return redirect('/guest/a');

    @request_mapping("/uv/<int:pk>/", method="get")
    def updateview(self, request, pk):
        obj = Guest.objects.get(id=pk);
        context = {
            'center': 'guest/update.html',
            'obj': obj
        };
        return render(request, 'home.html', context);
    #값을 models.py에서 가져롱때는 models내 테이블 클래스명.objects.get();
    #값을 태그에서(<form>)가져올땐 request.GET/POST['<form>내에 name으로 지정된 이름'];, 이 값을 변수 하나에 지정해서 사용.

    @request_mapping("/u", method="get")
    def update(self,request):
        id = request.GET['id'];
        title = request.GET['title'];
        content = request.GET['content'];

        obj = Guest.objects.get(id=id);
        obj.title = title;
        obj.content = content;
        obj.save();
        return redirect('/guest/g/'+id)
