import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Webcam Live Feed")
    run = st.checkbox('Run')

    # Create a placeholder for the video feed
    FRAME_WINDOW = st.image([])

    # Initialize the webcam
    camera = cv2.VideoCapture(0)

    while run:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        st.write('Stopped')

if __name__ == '__main__':
    main()
