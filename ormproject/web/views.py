import logging

from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from web.models import Cust


@request_mapping("")
class MyView(View):

    #iot 장비에서 들어온 정보로 로그 작성.
    #일단 상황을 가정하고 가상으로 해본거라 실제는 다르다.
    #서버 띄운 상태에서 iot 프로젝트를 새창에서 열고 그걸 실행해 본다.
    #터미널과 data/iotlog.scv에 무슨 일이!?
    @request_mapping("/iot", method="get")
    def iot(self,request):
        id = request.GET['id'];
        temp = request.GET['temp'];
        el = request.GET['el'];
        #----------------------------------
        el_logger = logging.getLogger('el_file');
        el_logger.debug(id+','+temp+','+el);
        #----------------------------------
        return render(request,'ok.html');

    @request_mapping("/", method="get")
    def home(self, request):
        return render(request, 'home.html');


    @request_mapping("/login", method="get")
    def login(self, request):
        context = {
            'center': 'login.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self, request):
        # id, pwd 를 프로그램을 확인 한다.
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        context = {};
        try:
            cust=Cust.objects.get(id=id);
            if cust.pwd == pwd:
                request.session['sessionid'] = cust.id;
                request.session['sessionname'] = cust.name;
                context['center'] = 'loginok.html';
                context['obj'] = cust;
            else:
                raise Exception;
        except:
            context['center'] = 'loginfail.html';

        # try:
        #     Cust.objects.get(id=id);
        #     Cust.objects.get(pwd=pwd);
        #     context['center'] = 'loginok.html';
        #     data=Cust.objects.get(id=id);
        #     context['obj'] = data;
        #     request.session['sessionid'] = id;
        # except:
        #
        #     context['center'] = 'loginfail.html';


        # if (id == 'qq') & (pwd == '11'):
        #     request.session['sessionid'] = id;
        #     context['center'] = 'loginok.html';
        # else:
        #     context['center'] = 'loginfail.html';
        return render(request, 'home.html', context);

    @request_mapping("/logout", method="get")
    def logout(self, request):
        if request.session['sessionid'] != None:
            del request.session['sessionid'];
        return render(request, 'home.html');

    @request_mapping("/register", method="get")
    def register(self, request):
        context = {
            'center': 'register.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/registerimpl", method="post")
    def registerimpl(self, request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        name = request.POST['name'];
        print(id,pwd,name);
        context = {};
        try:
            Cust.objects.get(id=id);
            context['center'] = 'registerfail.html';
        except:
            Cust(id=id, pwd=pwd, name=name).save();
            context['center'] = 'registerok.html';
            context['rname'] = name;

        return render(request, 'home.html', context);

    @request_mapping("/geo", method="get")
    def geo(self, request):
        context = {
            'center': 'geo.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/geo2", method="get")
    def geo2(self, request):
        context = {
            'center': 'geo2.html'
        };
        return render(request, 'home.html', context);