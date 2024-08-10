import streamlit as st
import plotly.express as px
from backend import get_data
from datetime import datetime

# Setting the title
st.title("Weather Forecast for the Next Day's")

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

if place:
    try:
        # Get the temperature/sky data
        filtered_data = get_data(place, days)

        # temperature/sky plotting area
        if option == "Temperature":

            # Getting temperature data
            temperatures = [dict['main']['temp'] / 10 for dict in filtered_data]

            # Getting dates
            dates = [dict["dt_txt"] for dict in filtered_data]

            # plotting the data
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            # storing the images path
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}

            # Getting sky conditions data
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]

            # Getting dates
            dates = [dict["dt_txt"] for dict in filtered_data]

            # generating the image paths according to the sky conditions
            image_paths = [images[condition] for condition in sky_conditions]

            # setting 4 images per row
            max_images_per_row = 4

            # iterating over the length of image paths and images per row to skip
            for i in range(0, len(image_paths), max_images_per_row):

                # creating columns to display the images
                cols = st.columns(min(max_images_per_row, len(sky_conditions)-i))

                # iterating columns, image_path and for date to display
                for col, image_path, date_str in zip(cols, image_paths[i:i + max_images_per_row], dates[i:i + max_images_per_row]):
                    with col:
                        date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                        formatted_date = date_obj.strftime("%a, %b, %d")
                        st.image(image_path, width=150)
                        st.write(f"<div style='text-align: center;'>{formatted_date}</div>", unsafe_allow_html=True)
    except KeyError:
        st.write("Place does not exist!!.")

