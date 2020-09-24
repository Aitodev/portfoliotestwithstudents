from django.shortcuts import render, redirect
from .models import Portfolio
import telebot
from django.views import View
from django.core.mail import send_mail
from .forms import ApplicationsForm


#1314657102:AAGbNCKRR3u0IS10sU42DO1XGFKCKNxmVDY
bot = telebot.TeleBot('1314657102:AAGbNCKRR3u0IS10sU42DO1XGFKCKNxmVDY')

def index(request):
    portfolio = Portfolio.objects.all()
    form = ApplicationsForm()
    return render(request, 'mainapp/index.html', {'port': portfolio, 'form': form})

def indexinner(request):
    return render(request, 'mainapp/inner-page.html')

def portfolio(request):
	return render(request, 'mainapp/portfolio-details.html')

class ApplicationsView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ApplicationsForm(request.POST)
            if form.is_valid():
                form.save()
                mail = form.cleaned_data['mail']
                name = form.cleaned_data['name']
                comment = form.cleaned_data['comment']
                subject = 'Новая заявка на подписку!'
                from_email = 'aitolivelive@gmail.com'
                to_email = ['aitolivelive@gmail.com', 'aitofullstack@gmail.com', 'kiroskost@gmail.com']
                message = 'Новая заявка!' + '\r\n' + '\r\n' + 'Почта: ' + mail + '\r\n' + '\r\n' + 'Имя:' + name + '\r\n' + 'Коммент:' + comment
                send_mail(subject, message, from_email, to_email, fail_silently=False)
                bot.send_message(879505800, message)
        return redirect('home')
