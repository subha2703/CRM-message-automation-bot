import requests

def send_telegram(message):
    try:
        bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
        chat_id = "YOUR_GROUP_OR_USER_CHAT_ID"  # Fixed chat ID
        send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message}
        response = requests.post(send_url, data=payload)
        return response.status_code == 200
    except:
        return False
