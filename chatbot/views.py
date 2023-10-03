from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from decouple import config

# Load the API key from .env
API_KEY = config('API_KEY')
openai.api_key = API_KEY

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    print(response)
    answer = response.choices[0].message.content.strip()
    return answer

# Create your views here.
def chatbot(request):

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')


