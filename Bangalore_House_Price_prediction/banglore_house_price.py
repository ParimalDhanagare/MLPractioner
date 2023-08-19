import pickle
import numpy as np
import streamlit as st

loaded_model=pickle.load(open("bangalore_house_price_prediction.pkl",'rb'))

def water_quality(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)


def main():
    st.title("Bangalore House Price Prediction")

    location=st.text_input('Enter the location')
    sqft=st.text_input('Enter total_sqft')
    bathrooms=st.text_input('Enter number of bathrooms')
    bhk=st.text_input('Enter the number of bedrooms,hall,kitchen(bhk)')

    test_result=''

    if st.button('Predict House Price'):
        test_result=water_quality([location,sqft,bathrooms,bhk])

        st.success(test_result)

if __name__=='__main__':
    main()   




