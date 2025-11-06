import streamlit as st
from PIL import Image
import numpy as np
# import your classifier / functions from your project, e.g.:
# from classifier import load_model, predict_face

@st.cache(allow_output_mutation=True)
def load_model():
    # load your trained ML classifier, encodings, etc
    # e.g. model = joblib.load('model.pkl')
    # return model
    pass

def predict(image, model):
    # pre-process the image as your classifier expects
    # run prediction
    # return the result / name / confidence
    pass

def main():
    st.title("Face Recognition Web App")
    st.write("Upload an image and the app will predict whose face it is")

    model = load_model()

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Detecting...")
        result = predict(image, model)
        st.write(f"Prediction: **{result}**")

if __name__ == "__main__":
    main()
