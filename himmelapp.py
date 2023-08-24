import streamlit as st
import cv2
st.title('ISO paint-thingy')

path = r"C:\Users\petno\Downloads\SampleInput.jpg"


@st.cache_data
def load_img(path, size_scale):
    img = cv2.imread(path)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img, gray

hour_to_filter = st.slider('Resize Percent', 1, 100, 100)
img, gray = load_img(path, hour_to_filter)
width = int(img.shape[1] * hour_to_filter / 100)
height = int(img.shape[0] * hour_to_filter / 100)
dim = (width, height)
# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

print("hej")

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.image(img)
