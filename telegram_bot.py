import os
import requests

def send_telegram_message(message):
    token = os.getenv("8652796222:AAGVySSu67kJDjWO8najx_x7fGEQ3gvrBbk")
    chat_id = os.getenv("7352325192")

    if not token or not chat_id:
        print("[Telegram]: ⚠️ زانیاری تەلەگرام لە ژینگەکەدا نییە.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("[Telegram]: ✅ نامە بە سەرکەوتوویی بۆ تلگرام نێردرا!")
    else:
        print(f"[Telegram]: ❌ هەڵە لە ناردنی نامە: {response.text}")