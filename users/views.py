from django.shortcuts import render,redirect
from .forms import RegisterForm

# Create your views here.

def register(request):
    redirect_to=request.POST.get('next',request.GET.get('next',''))
    if request.method=='POST':  #如果是post请求
        form=RegisterForm(request.POST)   #将post数据实例化为一个表单

        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')

    else:
        form=RegisterForm()
        #如果不是Post方法,就展示一个空的表单

    return render(request,'users/register.html',context={'form':form,'next':redirect_to})

def index(request):
    return render(request,'index.html')