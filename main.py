import streamlit as st
import plotly.express as px
from backend3 import *
st.title("Weather Forecast For Next Days")
place=st.text_input("Place: ")
days=st.slider("Forecast Days",min_value=1,max_value=5,value=1,
               help="Choose the number of days you would like to forecast")
option=st.selectbox("Select date to view",options=("Temperature","Sky"))
st.subheader(f"{option} For The Next {days} Days in {place}" )

if place:
    try:
        filtered_data = get_data(place, days)
        #Get the temperature sky data
        if option=="Temperature":
            temperatures = [item["main"]["temp"] / 10 for item in filtered_data]
            dates=[item["dt_txt"] for item in filtered_data]
            #Create a temperature plot
            figure=px.line(x=dates , y =temperatures, labels ={"x":"Temperature","y":"Sky"})
            st.plotly_chart(figure)
        if option=="Sky":
            images={"Clear":"004 images/clear.png","Clouds":"004 images/cloud.png",
                    "Rain":"004 images/rain.png","Snow":"004 images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths=[images[conditions] for conditions in sky_conditions]
            st.image(image_paths,width=115)
    except KeyError:
        st.write("That place does not exist")