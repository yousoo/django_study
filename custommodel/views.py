from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from custommodel.forms import MembersForm

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

def index(request):
    return render(request, 'index.html')