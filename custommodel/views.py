from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from custommodel.forms import MembersForm, SignInForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            member_name = form.cleaned_data.get('member_name')
            sex = form.cleaned_data.get('sex')
            phone_number = form.cleaned_data.get('phone_number')
            introduce = form.cleaned_data.get('introduce')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = MembersForm()
    return render(request, 'signup.html', {'form': form})

# contrib.auth에서 login 모듈을 가지고 왔으므로 그 안에 있는 메서드인 login()과
# 겹치게 되므로 로그인 view는 이름을 login이라고 짓지말자
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    context = {}
    return render(request, 'signin.html', context)

def index(request):
    return render(request, 'index.html')