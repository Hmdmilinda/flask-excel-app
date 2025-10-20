import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

st.title("📊 Google Sheet Data Entry")

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]

uploaded_file = st.file_uploader("Upload credentials.json", type="json")

if uploaded_file:
    creds_json = json.load(uploaded_file)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
    client = gspread.authorize(creds)

    sheet = client.open("App_Data").sheet1

    name = st.text_input("Enter Name")
    value = st.number_input("Enter Value", step=1)

    if st.button("Submit"):
        if name and value:
            sheet.append_row([name, value])
            st.success("✅ Data submitted successfully!")
        else:
            st.warning("⚠️ Please fill all fields.")
