from django.urls import path

from bot.views import (
    botwebhook

)

from config import BOT_API_TOKEN

urlpatterns = [
    # bot
    path('run-bot/<str:bot_token>', botwebhook.bot_webhook),
    path('demo', botwebhook.demo),
]