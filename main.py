import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast For Next Days")
place=st.text_input("Place: ")
days=st.slider("Forecast Days",min_value=1,max_value=5,value=1,
               help="Choose the number of days you would like to forecast")
option=st.selectbox("Select date to view",options=("Temperature","Sky"))
st.subheader(f"{option} For The Next {days} Days in {place}" )
data=get_data(place,days,option)
figure=px.line(x= , y =, labels =)
st.plotly_chart()