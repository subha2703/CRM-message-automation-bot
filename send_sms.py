import requests

def send_sms(phone, message):
    try:
        url = "https://www.fast2sms.com/dev/bulkV2"
        payload = {
            "authorization": "YOUR_FAST2SMS_API_KEY",
            "message": message,
            "language": "english",
            "route": "q",
            "numbers": phone
        }
        headers = {'cache-control': "no-cache"}
        response = requests.post(url, data=payload, headers=headers)
        return response.status_code == 200
    except:
        return False
