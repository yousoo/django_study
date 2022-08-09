from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from custommodel.forms import MembersForm, MembersModifyForm
from .models import Members
from django.contrib import messages #에러메시지 관련
from django.http import JsonResponse #Json메시지 응답
from django.contrib.auth.hashers import check_password #암호 해쉬값 체크 관련

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

# 아이디 중복확인
# 1. csrf를 해제한다 : @csrf_exempt
# 2. username을 받는다.
# 3. Members에서 username으로 검사한다
# 4. 검사결과를 객체로 넣는다.
# 5. 객체 길이가 1개 이상이면 이미 있다.
# 6. 중복이라고 에러로 내보낸다.
def username_check(request):
    username = request.GET['username']
    print('username:')
    print(username)
    if Members.objects.filter(username=username).exists():
        user_exist = {
            "is_user": "yes",
        }
    else:
        user_exist = {
            "is_user": "no",
        }
    return JsonResponse(user_exist)

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
        else:
            messages.info(request, '사용자 아이디나 암호가 틀렸습니다!')
    context = {}
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect('signin')

def index(request):
    return render(request, 'index.html')

def userupdate(request):
    search_user = request.user
    user_detail = Members.objects.get(username=search_user)
    if request.method == 'POST':
        form = MembersModifyForm(request.POST, instance=user_detail)
        if form.is_valid():
            print('여기까지')
            user_detail = form.save(commit=False)
            """
            패스워드 암호화
            1.입력된 암호 필드값을 받아서
            2.해쉬로 암호화한다.
            """
            raw_password = form.cleaned_data.get('password1') #입력된 암호필드값 받기
            user_detail.set_password(raw_password) #암호화
            user_detail.member_name = form.cleaned_data.get('member_name')
            user_detail.sex = form.cleaned_data.get('sex')
            user_detail.phone_number = form.cleaned_data.get('phone_number')
            user_detail.introduce = form.cleaned_data.get('introduce')
            user_detail.save()
            user = authenticate(request, username=search_user, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = MembersForm(instance=user_detail)
    context = {'form': form, 'user_detail': user_detail}
    return render(request, 'user_update.html', context)