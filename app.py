import streamlit as st
from keras.models import load_model
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import numpy as np

model = load_model('model.keras')

st.title("CNN number predictor")

canvas_result = st_canvas(
    stroke_width=10,
    stroke_color="white",
    background_color="black",
    width=280,
    height=280,
    drawing_mode="freedraw",
    key="canvas"
)

if canvas_result.image_data is not None:
    img = Image.fromarray((canvas_result.image_data[:,:,0:3]))
    img = img.convert("L")
    img = img.resize((28,28)) 
    img_arr = np.array(img).astype('float32')
    img_arr = img_arr.reshape((1,28,28,1))
    if st.button('Predict'):
        pred = model.predict(img_arr)
        st.success(f"Prediction : {np.argmax(pred)}")