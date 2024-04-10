from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from dotenv import load_dotenv
import os
from django.contrib import auth
from django.contrib.auth.models import User
from chatbot.models import Chat
from django.utils import timezone


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

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})

    return render(request, 'chatbot.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Error while creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Passwords not matched'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


