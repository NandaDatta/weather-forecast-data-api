import streamlit as st
import plotly.express as px

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
def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
