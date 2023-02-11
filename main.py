import requests
import streamlit as st
from streamlit_extras.colored_header import colored_header

api_key = "PEaNRU8XXspffKpqulJGid5bX3KudesOXXR3zqFQ"
url = "https://api.nasa.gov/planetary/apod?api_key=PEaNRU8XXspffKpqulJGid5bX3KudesOXXR3zqFQ"
response = requests.get(url)
data = response.json()

title = data["title"]
description = data["explanation"]
image = data["hdurl"]

image_response = requests.get(image).content

with open("photo.jpg", "wb") as file:
    file.write(image_response)

colored_header(
    label=title, description=description, color_name="red-60")
st.image("photo.jpg")
