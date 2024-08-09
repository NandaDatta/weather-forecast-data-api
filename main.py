import streamlit as st
import plotly.express as px
from backend import get_data

# Setting the title
st.title("Weather Forecast fot the Next Day's")

# storing the user input in a variable
place = st.text_input('Place: ')

# creating slider for days
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

# Creating options to forecast the data with that option
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

# sub header to display the header
st.subheader(f"{option} for the next {days} days in {place}")


# plotting area
d, t = get_data(place, days, kind)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
