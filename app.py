import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('SVMFinalModel.pkl', 'rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Rainier Climbing Success Prediction")
st.text("All the values are in the metric system")

battery_voltage = st.number_input("Enter Battery Voltage")
st.write("Battery Voltage", battery_voltage)
temperature = st.number_input("Enter Temperature")
st.write("Temperature", temperature)
relative_humidity = st.number_input("Enter Relative Humidity")
st.write("Relative Humidity", relative_humidity)
wind_speed_daily = st.number_input("Enter Wind Speed Daily")
st.write("Wind Speed Daily", wind_speed_daily)
solare_radiation = st.number_input("Enter Solare Radiation")
st.write("Solare Radiation", solare_radiation)

input_test = [battery_voltage, temperature,
              relative_humidity, wind_speed_daily, solare_radiation]

result = Lrdetect_Model.predict([input_test])*100

button_clicked = st.button("Predict Climbing Success")
if button_clicked:
    st.text(result)
    if result > 90:
        st.text("Climbing Success 😁")
    elif result > 60 and result < 90:
        st.text("Can take a chance 🤔")
    else:
        st.text("Not a good idea ⚠️💀")
