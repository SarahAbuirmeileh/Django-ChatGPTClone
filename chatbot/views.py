from django.shortcuts import render
from django.http import JsonResponse
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = openai_api_key


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = "Fixed for testing"
        return JsonResponse({'message':message, 'response':response})
    return render(request, 'chatbot.html')