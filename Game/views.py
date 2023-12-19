from django.shortcuts import render
from django.http import HttpResponse
import fopenaiAPI1
import audioplay
import os
from django.conf import settings
import time
from openai import OpenAI
from dotenv import load_dotenv
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

turtle_assistant_id = os.getenv('TURTLE_ASSISTANT_ID')
TURTLE_ASSISTANT_ID = turtle_assistant_id

escape_assistant_id = os.getenv('ESCAPE_ASSISTANT_ID')
ESCAPE_ASSISTANT_ID = escape_assistant_id


def gamestart(request):
    if request.method =="POST":
        if request.POST.get('action') == 'start' :    
            thread_id, category, username = create_thread(request)
            if category == 'turtle':
                # 현재는 스레드값을 가져와서 파일을 만들기 때문에 파일 삭제를 위해서 작성
                # cmd에서 icacls filename /grant %USERNAME%:F 실행해야 할 수 있음(권한 생성, 관리자모드로 실행해야 할 수도..)
                # 근데 만약에 회원가입 구현한다면 회원별로 파일을 만들어야 할 것 같음
                # 그래서 굳이 필요없을 것 같음 -> 탈퇴시 삭제(이러면 사용자들에게 권한을 주지 않아도 될 듯)
                # turtle_thread_id = request.session.get('turtle_thread_id')
                # print(turtle_thread_id)
                # if turtle_thread_id :
                #     old_file_path = os.path.join('C:\\Users\\yooji\\python_AI\\nlp_project\\django\\threads', f'turtle{turtle_thread_id}.txt')
                #     print(old_file_path)
                #     if os.path.isfile(old_file_path):
                #         os.remove(old_file_path)             
                request.session['turtle_thread_id'] = thread_id
                request.session['turtle'] = category
                request.session['username'] = username

                return redirect('turtlesoupgame')
            
            elif category == 'escape':
                request.session['escape_thread_id'] = thread_id
                request.session['escape'] = category
                request.session['username'] = username
            
                return redirect('escapegame')

            # threadsession = request.session.get('thread_id', 'cannot find thread id')
            # categorysession = request.session.get('category', 'cannot find category')
            # print(threadsession, categorysession)
            # request.session.save()
            # return render(request, "gamestart.html", {'thread_id': thread_id, 'category': category})
            
        elif request.POST.get('action') == 'continue' :
            request.session['username'] = request.POST.get('username')
            if request.POST.get('user_input') == 'turtle':
                return redirect('turtlesoupgame')
            elif request.POST.get('user_input') == 'escape':
                return redirect('escapegame')
    else :
        gamect = request.GET.get('game')
        cate = {'gamect': gamect}
        return render(request, "gamestart.html", cate)

def turtlesoupgame(request):
    # thread = request.session.get('turtle_thread_id', 'cannot find thread id')
    # category = request.session.get('turtle', 'cannot find category')
    username = request.session.get('username', 'cannot find username')
    file_name = file_name = f'{username}turtle.txt'
    file_path = os.path.join('C:\\Users\\yooji\\python_AI\\nlp_project\\django\\threads', f'{file_name}.txt')
    with open(file_path, 'r') as file:
        thread = file.read()
        file.close()

    if request.method == "POST":
        user_input = request.POST.get('user_input', '')
        run = submit_message(TURTLE_ASSISTANT_ID, thread, user_input)
        wait_on_run(run, thread)
        return redirect('turtlesoupgame')
    else :
        thread_list = answer_print(get_response(thread))
        return render(request, "turtlesoupgame.html", {'Data': thread_list})
    
def escapegame(request):
    # thread = request.session.get('escape_thread_id', 'cannot find thread id')
    # category = request.session.get('escape', 'cannot find category')
    username = request.session.get('username', 'cannot find username')
    file_name = file_name = f'{username}escape.txt'
    file_path = os.path.join('C:\\Users\\yooji\\python_AI\\nlp_project\\django\\threads', f'{file_name}.txt')
    with open(file_path, 'r') as file:
        thread = file.read()
        file.close()

    if request.method == "POST":
        user_input = request.POST.get('user_input', '')
        run = submit_message(ESCAPE_ASSISTANT_ID, thread, user_input)
        wait_on_run(run, thread)
        return redirect('escapegame')
    else :
        thread_list = answer_print(get_response(thread))
        return render(request, "escapegame.html", {'Data': thread_list})


def gamepage(request):
    # thread_id = request.session.get('openai_thread_id');
    # file_path = os.path.join('C:\\Users\\yooji\\python_AI\\nlp_project\\django\\threads', f'{thread_id}.txt')
    # game_name = request.session.get('game name')
    # file_path = os.path.join('C:\\Users\\yooji\\python_AI\\nlp_project\\django\\threads', 'turtlesoupgame.txt')
    # with open(file_path, 'r') as file:
    #     thread = file.read()
    #     file.close()
    thread = request.session.get('openai_thread_id', 'cannot find thread id')
    print('Saved data in gamepage', thread)

    if request.method == "POST":
        # POST 요청할 때 입력된 데이터를 가져옴
        # 'user_input'은 form에서 사용된 input 요소의 name 속성
        user_input = request.POST.get('user_input', '')
        # 여기서 user_input을 사용하여 필요한 작업 수행
        # ans = fopenaiAPI1.qna(user_input)
        # fopenaiAPI1.main(request.POST)
        run = submit_message(TURTLE_ASSISTANT_ID, thread, user_input)
        wait_on_run(run, thread)

        # thread_list = last_answer(get_response(thread)) 
        # thread_list = answer_print(get_response(thread))       
        # ans = get_openai_response(user_input)
        # get_new_messages(request, request.POST.get('user_input', ''))
        return redirect('gamepage')
        # return render(request, 'GPTinput.html', {'Data': thread_list})
    else :
        thread_list = answer_print(get_response(thread))
    
    # GET 요청일 때는 그냥 페이지를 렌더링
    return render(request, "GPTinput.html", {'Data': thread_list})

def create_thread(request):
    # if request.POST.get
    user_input = request.POST.get('user_input')
    username = request.POST.get('username')
    print(user_input)
    thread = client.beta.threads.create()
    # request.session['game name'] = user_input
    # request.session.save()
    # thread_id = thread.id
    # request.session['openai_thread_id'] = thread_id
    # threadsession = request.session.get('openai_thread_id', 'cannot find thread id')
    # print('Saved data', threadsession)
    # print(thread_id)
    # request.session['thread_id'] = thread.id
    # request.session['category'] = user_input
    # threadsession = request.session.get('thread_id', 'cannot find thread id')
    # categorysession = request.session.get('category', 'cannot find category')
    # print(threadsession, categorysession)
    print(thread.id)
    file_name = f'{username}{user_input}.txt'
    file_path = os.path.join('C:\\Users\\yooji\\python_AI\\nlp_project\\django\\threads',f'{file_name}.txt')
    # file_path = os.path.join('C:\\Users\\yooji\\python_AI\\nlp_project\\django\\threads', 'turtlesoupgame.txt')
    with open(file_path, 'w') as file:
        file.write(str(thread.id))
    return thread.id, user_input, username


def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread,
        assistant_id=assistant_id,
    )

def get_response(thread):
    return client.beta.threads.messages.list(thread_id=thread, order="asc")

def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

def last_answer(messages) :
    for m in messages :
        pass
    return {'content': m.content[0].text.value, 'role': m.role}

def answer_print(messages) :
    answer_list = []
    for m in messages :
        # 사용자의 입력과 시스템의 응답을 구분하기 위해 role을 추가하여 딕셔너리 형태 맵핑해서 저장
        answer_list.append({'content': m.content[0].text.value, 'role': m.role})
    return answer_list

def get_new_messages(request, user_input):
    file_path = os.path.join('C:\\Users\\yooji\\python_AI\\nlp_project\\django\\threads', 'escapegame_test.txt')
    with open(file_path, 'r') as file:
        thread = file.read()
        file.close()

    run = submit_message(TOUR_ASSISTANT_ID, thread, user_input)
    wait_on_run(run, thread)
    response = get_response(thread)
    new_messages_list = [response.data[-2], response.data[-1]]
    # new_messages_list = answer_print(last_thread_list) 
    return JsonResponse(new_messages_list, safe=False)

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