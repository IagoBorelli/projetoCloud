# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
import telebot

def index(request):
    return render(request, 'index.html')

# Configuração do bot Telegram
token = '7041052334:AAGKmUdY6iqXuG_N5aexrpXdm0To675p3kk'
chat_id = '6767934438'
bot = telebot.TeleBot(token)

def send_telegram_msg(hamburger, endereco, complemento, forma_pagamento):
    msg_final = f'''
    Novo pedido recebido:
    Hambúrguer: {hamburger}
    Endereço: {endereco}
    Complemento: {complemento}
    Forma de pagamento: {forma_pagamento}
    '''
    bot.send_message(chat_id, msg_final, parse_mode="Markdown")

def processar_pedido(request):
    if request.method == 'POST':
        hamburger = request.POST.get('hamburger')
        endereco = request.POST.get('endereco')
        complemento = request.POST.get('complemento')
        forma_pagamento = request.POST.get('gridRadios')
        
        # Enviar mensagem para o Telegram
        send_telegram_msg(hamburger, endereco, complemento, forma_pagamento)

        # Retornar uma resposta indicando que o pedido foi recebido
        return HttpResponse("Pedido recebido e enviado para o Telegram.")

    return HttpResponse("Método não permitido", status=405)
