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

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

tour_assistant_id = os.getenv('TOUR_ASSISTANT_ID')
TOUR_ASSISTANT_ID = tour_assistant_id

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
        run = submit_message(TOUR_ASSISTANT_ID, thread, user_input)
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
    return m.content[0].text.value

def answer_print(messages) :
    answer_list = []
    for m in messages :
        answer_list.append(m.content[0].text.value)
    return answer_list

def get_openai_response(request, user_input):
    messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
    messages.append(
                {"role": "user", "content": str(user_input)},
            )
    # OpenAI의 API를 호출하여 사용자 입력에 대한 응답을 얻습니다.
    chat = client.chat.completions.create(
    model="gpt-4-1106-preview", messages=messages )
    
    return chat.choices[0].message.content

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

def gamestart(request):
    lst1 =['banana', 'apple', 'orange']
    context = {'Person1':'설렁탕', 'Person2':'비빔밥', 'Person3':'볶음우동'}
    return render(request, "gamestart.html", context)
