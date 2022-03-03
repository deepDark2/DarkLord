from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping

from config.settings import UPLOAD_DIR
from web.models import Guest, Article, Item


@request_mapping("/item")
class ItemView(View):

    @request_mapping("/a", method="get")
    def all(self,request):
        obj = Item.objects.all();
        context = {
            'center':'item/list.html',
            'objs':obj
        };
        return render(request,'home.html',context);


    @request_mapping("/iv", method="get")
    def insertview(self,request):
        context = {
            'center':'item/add.html',
        };
        return render(request,'home.html',context);

    @request_mapping("/i", method="post")
    def insert(self,request):
        name = request.POST['name'];
        price = request.POST['price'];
        imgname = '';
        if 'img' in request.FILES:
            img = request.FILES['img'];
            imgname = img._name;
            f = open('%s/%s' % (UPLOAD_DIR, imgname), 'wb')
            for chunk in img.chunks():
                f.write(chunk);
                f.close();
        obj = Item(name=name, price=price,imgname = imgname);
        obj.save();
        return redirect('/item/a');
        #이미지 등록후 완전히 반영되는데에는 시간이 걸린다.

    @request_mapping("/g/<int:pk>", method="get")
    def get(self, request,pk):
        obj = Item.objects.get(id=pk);
        import logging
        #-----------------------------------------------
        name = 'guest';
        if request.session['sessionname'] != None:
            name = request.session['sessionname'];
        logger = logging.getLogger('iot_file');
        logger.debug(obj.name+','+str(obj.price)+','+name);
        #------------------------------------------------
        context = {
            'center': 'item/get.html',
            'objs': obj
        };
        return render(request, 'home.html', context);