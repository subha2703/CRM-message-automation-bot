import pytesseract
import re
from PIL import Image

def extract_info(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    phone_match = re.findall(r'\b\d{10}\b', text)
    email_match = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    telegram_match = re.findall(r'@\w+', text)

    return {
        "phone": phone_match[0] if phone_match else "",
        "email": email_match[0] if email_match else "",
        "telegram": telegram_match[0] if telegram_match else ""
    }