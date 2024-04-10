from django.shortcuts import render
from django.http import JsonResponse

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = "Fixed for testing"
        return JsonResponse({'message':message, 'response':response})
    return render(request, 'chatbot.html')