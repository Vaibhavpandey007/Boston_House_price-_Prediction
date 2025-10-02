import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns


model = joblib.load("boston_gb_model.pkl")
excepted_columns = joblib.load("column.pkl")

st.set_page_config(page_title="Boston Housing Price Predictor", layout="wide")

st.title("🏠 Boston Housing Price Prediction App")
st.write("Predict the price of a house in Boston based on its features.")

st.sidebar.header("Feature Importance")
importances = model.feature_importances_
feat_names = ["crim","zn","indus","chas","nox","rm","age","dis","rad","tax","ptratio","b","lstat"]

fig, ax = plt.subplots(figsize=(5,6))
sns.barplot(x=importances, y=feat_names, ax=ax)
ax.set_title("Feature Importance - Gradient Boosting")
st.sidebar.pyplot(fig)


col1, col2, col3, col4 = st.columns(4)

with col1:
    crim = st.number_input("Crime Rate (CRIM)", 0.0, 100.0, 0.01, step=0.01)
    zn = st.slider("Residential Land (ZN)", 0.0, 100.0, 20.0)
    indus = st.slider("Non-retail Business Acres (INDUS)", 0.0, 30.0, 5.0)
    chas = st.selectbox("Charles River (CHAS)", [0, 1])
    
with col2:
    nox = st.slider("Nitric Oxides (NOX)", 0.0, 1.0, 0.5)
    rm = st.slider("Avg Rooms (RM)", 3.0, 10.0, 6.0)
    age = st.slider("Age of House (AGE)", 0.0, 100.0, 50.0)
    
with col3:
    dis = st.slider("Distance to Employment (DIS)", 0.0, 12.0, 5.0)
    rad = st.slider("Accessibility to Highways (RAD)", 1, 24, 5)
    tax = st.slider("Property Tax Rate (TAX)", 100.0, 700.0, 300.0)
    
with col4:
    ptratio = st.slider("Pupil-Teacher Ratio (PTRATIO)", 10.0, 25.0, 15.0)
    b = st.slider("1000(Bk - 0.63)^2 (B)", 0.0, 400.0, 390.0)
    lstat = st.slider("% Lower Status Population (LSTAT)", 0.0, 40.0, 10.0)

input_data = pd.DataFrame([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]],
                          columns=feat_names)


if st.button("Predict House Price"):
    prediction = model.predict(input_data.values)
    st.success(f"🏡 Predicted House Price: ${prediction[0]*1000:.2f}")
