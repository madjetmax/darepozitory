from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TestM, Goods, Profile
from .forms import CreateNL, RegisterF

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required



def main_page(request):
    
    # return HttpResponse('<h1>Home Page</h1>')
    all_links = ['home', 'shop', 'registration']
    return render(request, 'main_page.html', {
        'all_links': all_links,
        'user': request.user
        })


def page_num(response, page):
    print(1)
    page_info = Goods.objects.all()[page-1]
    return render(response, 'shop_temp.html', {'page_title':page_info.title, 'page_info': page_info})
    
    


def get_page(response, page):
    try:
        item = TestM.objects.all()[page-1]
        page_tile = item.name
        page_content = item.text
        return render(response, 'base.html', {
            'title': page_tile,
            'content': page_content,
        })
    except Exception:
        pass
def post_test(response):
    if response.method == 'POST':
        print(1)
    return render(response, 'post_test.html', {})
# def logut(response):
#     if response.user.is_authenticated:
#         logout(response)
#     return redirect('login/')
    
    
def login_wiev(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request=request, username=username, password=password)
            if user is None:
                print(1)
            else:
                login(request=request, user=user)
                return redirect('/')
        return render(request, 'login.html', {})


def logout_wiew(response):
    if response.method == 'POST':
        logout(request=response)
        return redirect('/reg/')
    return render(response, 'logout.html', {'request': response})

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
        
       
    else:
        if request.method == 'POST':
            form = RegisterF(request.POST)
            username = request.POST['name']
            password = request.POST['password']
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = RegisterF()
        return render(request, 'register.html', {
            'form': form
        })


def create(response):
    if response.method == 'POST':
        if response.POST.get('save'):
            print(response.POST.get('name'))
            print(response.POST.get('password'))
            print(response.POST.get('check'))
            print(response.POST.get('time'))
            print(response.POST.get('color'))
            print(response.POST.get('range'))

    # form = CreateNL(response.POST)
        # print(form.data)

       
        # if form.is_valid():
        #     n = form.cleaned_data['name']
        #     t = Goods()
        #     t.title = n
        #     t.content = []
        #     t.save()
    # else:
    # form = CreateNL()
    return render(response, 'castom_form.html', {})
 