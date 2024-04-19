# if you are cloning the messenger do not forget to install the required dependencies beforehand.
# backend
import pywhatkit
from datetime import datetime

def send_whatsapp_message(phone_number, message, date, time):
    try:

        datetime_obj = datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M")


        pywhatkit.sendwhatmsg(phone_number, message, datetime_obj.hour, datetime_obj.minute)
        print("Message scheduled successfully!")
    except Exception as e:
        print("An error occurred:", e)

