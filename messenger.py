# messenger.py
# frontend.py
import matplotlib
matplotlib.use('agg')
import streamlit as st
from backend import send_whatsapp_message


def main():
    st.title("WhatsApp-Messenger")

    phone_number = st.text_input("Recipient's Phone Number")
    message = st.text_area("Message")
    date = st.date_input("Date")
    time = st.text_input("Time (24 hrs format, e.g., 12:00)")

    if st.button("Schedule Message"):
        if phone_number and message and date and time:
            send_whatsapp_message(phone_number, message, date.strftime("%Y-%m-%d"), time)
            st.success("Message scheduled successfully!")
        else:
            st.warning("Please fill in all the fields.")


if __name__ == "__main__":
    main()
