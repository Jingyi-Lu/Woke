from django.shortcuts import render
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User 
# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='username',max_length=100)
    email = forms.CharField(label='email',max_length=100)
    password = forms.CharField(label='password',max_length=100,widget=forms.PasswordInput())
    confirmed_password = forms.CharField(label='confirmed_password',max_length=100,widget=forms.PasswordInput())

def welcome(request):
    return render(request,'welcome.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        re = auth.authenticate(username=username,password=password)  #用户认证
        if re is not None:  #如果数据库里有记录（即与数据库里的数据相匹配或者对应或者符合）
            auth.login(request,re)   #登陆成功
            return render(request,'explore.html')    #跳转--redirect指从一个旧的url转到一个新的url
        else:  #数据库里不存在与之对应的数据
            return render(request,'login.html',{'login_error':'incorrect username or password'})  #注册失败
    return render(request,'login.html')

def successful(request):
    return render(request,'successful.html')

def signup(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)  #包含用户名和密码
        if uf.is_valid():
            #获取表单数据
            username = uf.cleaned_data['username']  #cleaned_data类型是字典，里面是提交成功后的信息
            email = uf.cleaned_data['email']
            password = uf.cleaned_data['password']
            confirmed_password = uf.cleaned_data['confirmed_password']
            if password != confirmed_password:
                return render(request,'signup.html',{'signup_error':'Not the same password!'})
            print(username,password)
            if username == 'abc':
                return render(request,'signup.html',{'signup_error':''})
            #添加到数据库
            # registAdd = User.objects.get_or_create(username=username,password=password)
            
            if User.objects.get(username=username):
                return render(request,'signup.html',{'signup_error':'username already exists'})
            registAdd = User.objects.create_user(username=username, password=password)
        

            # print registAdd
            if registAdd == False:
                return render(request,'welcome.html')
 
            else:
                # return HttpResponse('ok')
                return render(request,'successful.html')
                # return render_to_response('share.html',{'registAdd':registAdd},context_instance = RequestContext(request))
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        uf = UserForm()
    # return render_to_response('regist.html',{'uf':uf},context_instance = RequestContext(request))
    return render(request,'signup.html')

def explore(request):
    return render(request,'explore.html')