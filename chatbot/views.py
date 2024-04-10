from django.shortcuts import render
from django.http import JsonResponse
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = openai_api_key


def ask_openai(message):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=message,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
    except Exception:
        answer = "Error while getting response from aopenai"
    return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')


def register(request):
    pass


def login(request):
    pass


def logout(request):
    pass


