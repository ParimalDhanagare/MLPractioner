import pickle
import numpy as np
import streamlit as st

loaded_model=pickle.load(open("Bangalore_House_Price_prediction/bangalore_house_price_prediction.pkl",'rb'))

def predict_price(location,sqft,bath,bhk):
    loc_index = np.where(x.columns==location)[0]
    
    x1 = np.zeros(len(x.columns))
    x1[0] = sqft
    x1[1] = bath
    x1[2] = bhk
    if loc_index.size >= 0:
        x1[loc_index] = 1
    return lr_clf.predict([x1])[0]


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




