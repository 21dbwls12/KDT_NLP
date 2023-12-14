from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

tour_assistant_id = os.getenv('TOUR_ASSISTANT_ID')
TOUR_ASSISTANT_ID = tour_assistant_id

@csrf_exempt
@require_POST
def create_thread(request):
    user_input = request.POST.get('user_input')
    thread = client.beta.threads.create()
    file_path = os.path.join('C:\\Users\\yooji\\python_AI\\nlp_project\\django\\threads', 'escapegame_test.txt')
    with open(file_path, 'w') as file:
        file.write(str(thread.id))
    return thread.id
