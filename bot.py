import os
import threading
import telebot
from http.server import HTTPServer, BaseHTTPRequestHandler

TOKEN = "8583878475:AAGS-cdYq3iLBN_32NblHIwhrqhm0f4GS3k"  # <-- сюди токен від BotFather

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Вітаю!\n\nЩоб швидко отримати відповіді на всі запитання про роботу на платформі, перегляньте, будь ласка, цю сторінку:\nhttps://best-expert.com.ua/psy\n\nЦе заощадить ваш час і допоможе швидше розпочати роботу.")

def run_bot():
    bot.infinity_polling()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_http_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=run_bot, daemon=True).start()
run_http_server()
