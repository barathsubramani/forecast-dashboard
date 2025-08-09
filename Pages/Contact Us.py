import streamlit as st
from sendingEmails import send_emails

st.title("Contact Us")

st.write("Feel free to reach out to us by typing in your e-mail.")

with st.form(key="email_forms"):
    user_email = st.text_input(label="E-mail", placeholder="Enter your e-mail...", key="enter")
    raw_message = st.text_area(label="Tell us more about you.", placeholder="Type in your queries...", key="des", )
    message = f"""\
Subject: New email from {user_email} 

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(button)

    if button:
        send_emails(message)
        st.info("Your email was sent successfully.")
