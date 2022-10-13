import numpy as np 
import pickle            # for loading the saved model 
import streamlit as st   # for creating the web page

loaded_model = pickle.load(open("C:/Users/91788/Downloads/Big_Mart/Big_mart.sav", 'rb'))

def Big_mart(input_data):
    

    #changing input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=object)

    #reshape the array as we are predicting for one instance 
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
   # print(prediction)

    return prediction

            
def main():
    
    
    # giving a title
    st.title('Big mart Price Predict')  
    
    # image_file = st.file_uploader('Upload a file')
    # st.image(image_file)
    # st.download_button('Download file', image_file) 
    
    # getting the input data from the user
    weight = st.text_input('Item_Weight') 
    Fat = st.text_input('Item_Fat_Content 0-> Low Fat 1-> Regular')
    MRP = st.text_input('Item_MRP')
    size = st.text_input('Outlet_Size 0-> Small 1->Medium 2->High')
   
   

    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction

    if st.button('Outlet_Sales :'):
        diagnosis = Big_mart([weight, Fat, MRP, size])
    
    st.success(diagnosis)


if __name__ == '__main__': 
    main()