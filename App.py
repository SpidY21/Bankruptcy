import streamlit as st
import numpy as np
import pickle

model = pickle.load((open("C:/Users/Yash/Desktop/ExcelR Project/P357/App/model.sav", 'rb')))


def bankruptcy(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0] == 1:
        return 'Bankruptcy'
    else:
        return 'Non-Bankruptcy'


def main():
    st.title('Bankruptcy Prevention')

    options = [0, 0.5, 1]

    industrial_risk = st.selectbox('Industrial Risks :-', options)
    industrial_risk = float(industrial_risk)
    management_risk = st.selectbox('Management Risks :-', options)
    management_risk = float(management_risk)
    financial_risk = st.selectbox('Financial Risks :-', options)
    financial_risk = float(financial_risk)
    credibility = st.selectbox('Credibility :-', options)
    credibility = float(credibility)
    competitiveness = st.selectbox('Competitiveness :-', options)
    competitiveness = float(competitiveness)
    operation_risk = st.selectbox('Operation Risk :-', options)
    operation_risk = float(operation_risk)

    input_var = [industrial_risk, management_risk, financial_risk, credibility, competitiveness, operation_risk]

    diagnosis = ''
    if st.button('Predict'):
        diagnosis = bankruptcy(input_var)

    st.success(diagnosis)


if __name__ == '__main__':
    main()
