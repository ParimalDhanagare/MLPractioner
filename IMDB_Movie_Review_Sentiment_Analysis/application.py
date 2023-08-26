import pickle
import numpy as np
import streamlit as st

loaded_model=pickle.load(open("IMDB_Movie_Review_Sentiment_Analysis/logistic_regression_model.pkl",'rb'))

def review_sentiment(input_data):
    # input_data_as_numpy_array=np.asarray(input_data)
    # input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data)
    print(prediction)

    if (prediction[0]==1):
        return "The sentiment about the movie is positive, You should watch this movie"
    else:
        return "The sentiment about the movie is negative, You should not watch this movie"

def main():
    st.title("IMDB Movie Review Sentiment App")

    movie_name=st.text_input('Enter movie name',placeholder="Enter movie name")
    movie_review=st.text_input('Enter movie review',placeholder="Enter movie Review")

    test_result=''

    if st.button('Predict movie sentiment'):
        test_result=review_sentiment([movie_name,movie_review])

        st.success(test_result)

if __name__=='__main__':
    main()   




