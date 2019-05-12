from django.shortcuts import render

def api(request):
    return render(request,'apihtml/api_admin.html')

def user_login(request):
    return render(request,'apihtml/user_login.html')


def user_logout(request):
    return render(request,'apihtml/user_logout.html')


def user_information(request):
    return render(request,'apihtml/user_information.html')


def user_updateinformation(request):
    return render(request,'apihtml/user_updateinformation.html')


def get_company(request):
    return render(request,'apihtml/get_company.html')

def accidents_list(request):
    return render(request,'apihtml/accidents_list.html')


def accident_detail(request):
    return render(request,'apihtml/accident_detail.html')


def accident_add(request):
    return render(request,'apihtml/accident_add.html')


def accident_type(request):
    return render(request,'apihtml/accident_type.html')


def accident_rank(request):
    return render(request,'apihtml/accident_rank.html')


def event_type(request):
    return render(request,'apihtml/event_type.html')


def events_list(request):
    return render(request,'apihtml/events_list.html')


def event_detail(request):
    return render(request,'apihtml/event_detail.html')


def event_add(request):
    return render(request,'apihtml/event_add.html')


def accident_analysis(request):
    return render(request,'apihtml/accident_analysis.html')


def event_analysis(request):
    return render(request,'apihtml/event_analysis.html')