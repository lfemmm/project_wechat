from django.shortcuts import render

def api(request):
    return render(request,'apihtml/api_admin.html')

def user_login(request):
    return render(request,'apihtml/user_login.html')


def user_logout(request):
    return render(request,'apihtml/user_logout.html')
