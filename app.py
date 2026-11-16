# import pickle
# import pandas as pd
# import streamlit as st

# # Page configuration
# st.set_page_config(page_title='Loan Classification')

# with st.sidebar:
#     st.title('Loan Classification')

# # Load the model
# with open('best_model_pipeline.pkl', 'rb') as file:
#     best_pipeline = pickle.load(file)

# # Load cleaned dataframe
# df = pd.read_csv('cleaned_data.csv')

# # Display dataset in browser=
# st.dataframe(df)

import pickle
import pandas as pd 
import streamlit as st

# page configuration
st.set_page_config(page_title='loan classification')

with st.sidebar:
    st.title('loan classification')
    st.image('photo_2026-11-16_13-35-19.jpg')

# load the model
with open('best_model_pipeline.pkl', 'rb') as file:
    best_pipeline = pickle.load(file)

# load cleaned dataframe
df=pd.read_csv('cleaned_data.csv')
# st.dataframe(df)
# st.write(df)

# user input
col1,col2,col3, col4=st.columns(4, border=True)

with col1:
    person_age= st.slider('age',min_value=18,max_value=100)
    person_income=st.slider('income',min_value=10000,max_value=1000000)
    person_emp_exp=st.slider('employment experience',min_value=0,max_value=100)
    loan_amnt=st.slider('loan amount',min_value=0,max_value=100000)

with col2:
    person_gender=st.radio('gender',options=df['person_gender'].unique())
    loan_intent=st.selectbox('loan intent',options=df['loan_intent'].unique())
    loan_int_rate=st.slider('loan interest rate',min_value=0.0,max_value=20.0)
    loan_percent_income=st.slider('loan percent income',min_value=0.0,max_value=0.99)
    cb_person_cred_hist_length=st.slider('credit history length',min_value=0.0,max_value=30.0)
    credit_score=st.slider('credit score',min_value=0,max_value=850)

with col3:
    person_education=st.selectbox('education',options=df['person_education'].unique())
    person_home_ownership=st.selectbox('home ownership',options=df['person_home_ownership'].unique())

    previous_loan_defaults_on_file=st.selectbox('previous loan defaults on file',options=df['previous_loan_defaults_on_file'].unique())
new_data=pd.DataFrame(new_data,index=[0])

with col4:
    if st.button("Predict Loan Status"):
        prediction= best_pipeline.predict(new_data)[0]
        if prediction == 0 :
            st.error("Loan Rejected")
        else:
            st.success("Loan aprroved")
