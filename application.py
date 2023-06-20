import pickle
import numpy as np
import streamlit as st

loaded_model=pickle.load(open("C:/Users/parim/OneDrive/Desktop/RandomForestDeployment/RandomForest.pkl",'rb'))

def water_quality(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
        return "Potable Water"
    else:
        return"Non-potable Water"

def main():
    st.title("Water Quality Prediction")

    ph=st.text_input('ph value', 'Enter the value')
    Hardness=st.text_input('Hardness value','Enter the value')
    Solids=st.text_input('Solids','Enter the value')
    Chloramines=st.text_input('Chloramines','Enter the value')
    Sulphate=st.text_input('Sulphate','Enter the value')
    Conductivity=st.text_input('Conductivity','Enter the value')
    Organic_carbon=st.text_input('Organic Carbon Value','Enter the value')
    Trihalomethanes=st.text_input('Trihalomethanes Value','Enter the value')
    Turbidity=st.text_input('Turbidity','Enter the Value')

    test_result=''

    if st.button('Predict Water Quality'):
        test_result=water_quality([ph,Hardness,Solids,Chloramines,Sulphate,
        Conductivity,Organic_carbon,Trihalomethanes,Turbidity])

        st.success(test_result)

if __name__=='__main__':
    main()   




