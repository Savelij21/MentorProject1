import requests
from django.conf import settings


def send_telegram_message(user_tg_id: int, text: str):
    """Отправка сообщения пользователю через Telegram Bot API."""

    bot_token = settings.BOT_TOKEN

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": user_tg_id,
        "text": text,
        "parse_mode": "HTML",
    }

    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
    except Exception:
        print("Error through sending message to Telegram")
