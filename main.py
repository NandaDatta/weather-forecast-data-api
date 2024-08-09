import streamlit as st

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

st.subheader(f"{option} for the next {days} days in {place}")