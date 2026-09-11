import streamlit as st
import pandas as pd
import joblib

model = joblib.load("ad_model.pkl")

st.title("Adsorption Capacity Prediction App")
st.write("Enter values of variables for adsorption")

n = st.number_input(
    "What number of predictions do you wish to do?",
    min_value=1,
    step=1,
    value=1
)

inputs = []

for i in range(n):

    st.subheader(f"Prediction {i + 1}")

    Batch = st.number_input(
        "Batch:",
        min_value=0.0,
        key=f"Batch_{i}"
    )

    Temperature = st.number_input(
        "Temperature:",
        min_value=0.0,
        key=f"Temperature_{i}"
    )

    Volume = st.number_input(
        "Volume:",
        min_value=0.0,
        key=f"Volume_{i}"
    )

    pH = st.number_input(
        "pH:",
        min_value=0.0,
        max_value=14.0,
        key=f"pH_{i}"
    )

    Time = st.number_input(
        "Contact time:",
        min_value=0.0,
        key=f"Time_{i}"
    )

    Adsorbate_Dose = st.number_input(
        "Adsorbate Dose:",
        min_value=0.0,
        key=f"Adsorbate_Dose_{i}"
    )

    Adsorbent_Mass = st.number_input(
        "Adsorbent Mass:",
        min_value=0.0,
        key=f"Adsorbent_Mass_{i}"
    )

    inputs.append({
        "Batch": Batch,
        "Temperature": Temperature,
        "Volume": Volume,
        "pH": pH,
        "Time": Time,
        "Adsorbate Dose": Adsorbate_Dose,
        "Amount of Adsorbent": Adsorbent_Mass
    })


if st.button("Predict"):

    for i, data in enumerate(inputs):

        new_combo = pd.DataFrame([data])

        prediction = model.predict(new_combo)

        st.success(
            f"Prediction {i + 1}: {prediction[0]:.2f}"
        )