import streamlit as st
import os
def save_uploadedfile(uploadedfile):
    with open(os.path.join("./media-directory/", "selfie.jpg"), "wb") as f:
        f.write(uploadedfile.getbuffer())
    
picture = st.camera_input("Take a picture")
st.markdown('')
if picture:
    st.sidebar.divider()
    st.sidebar.image(picture, caption="Selfie")
    if st.button("Segment!"):
        ## Function to save image
        save_uploadedfile(picture)
        st.sidebar.success("Saved File")
        selfie_img = os.path.join("media-directory", "/selfie.jpg")
    st.write("Click on **Clear photo** to retake picture")
    img_file = './media-directory/selfie.jpg'
st.divider()