from django.shortcuts import render
from django.http import HttpResponse
import fopenaiAPI1
import audioplay
import os
from django.conf import settings

def gamepage(request):
    if request.method == "POST":
        # POST 요청할 때 입력된 데이터를 가져옴
        # 'user_input'은 form에서 사용된 input 요소의 name 속성
        user_input = request.POST.get('user_input', '')
        # 여기서 user_input을 사용하여 필요한 작업 수행
        ans = fopenaiAPI1.qna(user_input)
        # fopenaiAPI1.main(request.POST)
        return render(request, 'GPTinput.html', {'user_input': user_input, 'Data': ans})
    
    # GET 요청일 때는 그냥 페이지를 렌더링
    return render(request, "GPTinput.html")

def getImagepage(request):
    if request.method == "POST":
        # POST 요청할 때 입력된 데이터를 가져옴
        # 'user_input'은 form에서 사용된 input 요소의 name 속성
        user_input = request.POST.get('user_input', '')
        # 여기서 user_input을 사용하여 필요한 작업 수행
        image = fopenaiAPI1.getImage(user_input)
        # fopenaiAPI1.main(request.POST)
        return render(request, 'getImage.html', {'Data': image})
    
    # GET 요청일 때는 그냥 페이지를 렌더링
    return render(request, "getImage.html")

def datatest(request):
    context = {'Person1':'설렁탕', 'Person2':'비빔밥', 'Person3':'삼겹살'}
    return render(request, "datatest.html", context)

def fortest(request):
    lst1 =['banana', 'apple', 'orange']
    context = {'Person1':'설렁탕', 'Person2':'비빔밥', 'Person3':lst1}
    return render(request, "fortest.html", context)

def mediatest(request):
    audioplay.play()
    lst1 =['banana', 'apple', 'orange']
    context = {'Person1':'설렁탕', 'Person2':'비빔밥', 'Person3':lst1}
    return render(request, "mediatest.html", context)

def category(request):
    lst1 =['banana', 'apple', 'orange']
    context = {'Person1':'설렁탕', 'Person2':'비빔밥', 'Person3':'볶음우동'}
    return render(request, "category.html", context)
