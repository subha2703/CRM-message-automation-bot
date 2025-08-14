import streamlit as st
import easyocr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from greetings import GREETINGS
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT, BOT_LINK
import tempfile
import os

# Streamlit UI
st.set_page_config(page_title="CIA Card Greeting Bot", page_icon="📨")
st.title("📨 CIA Card Scan & Greeting Bot")

st.markdown("Upload a CIA card image. The system will scan it, extract the email, and send a greeting.")

# Upload card
uploaded_file = st.file_uploader("🖼️ Upload CIA Card Image (PNG, JPG)", type=['png', 'jpg', 'jpeg'])

# Select Greeting
selected_greeting = st.selectbox("🎉 Select a Greeting Template", list(GREETINGS.keys()))

# Scan and Send Button
if st.button("📤 Scan and Send Email"):
    if uploaded_file is not None and selected_greeting:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        try:
            # OCR
            reader = easyocr.Reader(['en'])
            results = reader.readtext(tmp_file_path, detail=0)
            os.unlink(tmp_file_path)  # delete temp file

            # Extract email from scanned text
            email_found = None
            for text in results:
                if "@" in text and "." in text:
                    email_found = text.strip()
                    break

            if email_found:
                message_template = GREETINGS[selected_greeting]
                final_message = message_template.format(bot_link=BOT_LINK)

                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = email_found
                msg['Subject'] = f"Cube AI - {selected_greeting}"
                msg.attach(MIMEText(final_message, 'plain'))

                # Send Email
                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()
                    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    server.send_message(msg)

                st.success(f"✅ Email sent to {email_found} with greeting '{selected_greeting}'!")
            else:
                st.warning("⚠️ Could not detect a valid email in the uploaded image.")

        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please upload a CIA card image and select a greeting.")
