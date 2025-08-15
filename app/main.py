import streamlit as st

st.title("Cats vs Dogs")
st.write("Upload an image to classify (stub).")
file = st.file_uploader("Image", type=["png","jpg","jpeg"])
if file:
    st.image(file)
    st.metric("Prediction", "Cat (stub)")
