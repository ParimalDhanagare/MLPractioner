import pickle
import numpy as np
import streamlit as st

loaded_model=pickle.load(open("Bangalore_House_Price_prediction/bangalore_house_price_prediction.pkl",'rb'))

def predict_price(location,sqft,bathrooms,bhk):
    # input_data_as_numpy_array=np.asarray(input_data)
    # input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(location,sqft,bathrooms,bhk)
    print(prediction)


def main():
    st.title("Bangalore House Price Prediction")

    location=st.text_input('Enter the location')
    sqft=st.text_input('Enter total_sqft')
    bathrooms=st.text_input('Enter number of bathrooms')
    bhk=st.text_input('Enter the number of bedrooms,hall,kitchen(bhk)')

    test_result=''

    if st.button('Predict House Price'):
        test_result=predict_price(location,sqft,bathrooms,bhk)

        st.success(test_result)

if __name__=='__main__':
    main()   




