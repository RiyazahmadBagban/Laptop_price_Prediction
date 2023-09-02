# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 08:47:19 2022

@author: Admin
"""

#pip install sreamlit

import streamlit as st
import pandas as pd
import pickle


st.title('Laptop Price Prediction')



st.sidebar.header('User Input Parameters')



def user_input_features():
    CO = st.sidebar.selectbox('Company',('Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI','Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer','Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG'))
    TN = st.sidebar.selectbox('TypeName',('Ultrabook', 'Notebook', 'Netbook', 'Gaming', '2 in 1 Convertible','Workstation'))
    Ram = st.sidebar.selectbox('Ram',(8, 16,  4,  2, 12,  6, 32, 24, 64))
    
    Wt = st.slider("Weight",min_value=0.69,max_value=4.7,step=0.1)
    Pr = st.slider("Price",min_value=0.619565,max_value=12.691441,step=0.1)
    
    TS = st.sidebar.selectbox('TouchScreen',(0,1))    
    Ips = st.sidebar.selectbox('Ips',(0,1))
    
    Ppi = st.slider("Ppi",min_value=90.0,max_value=360.0,step=0.1)
    
    CB = st.sidebar.selectbox('Cpu_brand',('Intel Core i5', 'Intel Core i7', 'AMD Processor', 'Intel Core i3','Other Intel Processor'))
    HDD = st.sidebar.selectbox('HDD',(0, 32, 128, 500, 1000, 2000))    
    SSD = st.sidebar.selectbox('SSD',(0, 8, 16, 32, 64, 128, 180, 240, 256, 512, 768, 1000, 1024))    
    GB = st.sidebar.selectbox('Gpu_brand',('Intel', 'AMD', 'Nvidia'))
    Os = st.sidebar.selectbox('Os',('Mac', 'Others', 'Windows'))
    
    SZ = st.sidebar.number_input('ScreenSize',min_value=130,max_value=1250,step=1)   
    SC = st.sidebar.number_input('StorageCapacity',min_value=450,max_value=2550,step=1)
     
    
    data= {'Company': CO,
           'TypeName': TN,
           'Ram': Ram,
            'Weight': Wt,
            'Price': Pr,
            'TouchScreen': TS,
            'Ips': Ips,
            'Ppi': Ppi,
            'Cpu_brand': CB,
            'HDD': HDD,
            'SSD': SSD,
            'Gpu_brand': GB,
            'Os': Os,
            'ScreenSize': SZ,
            'StorageCapacity': SC}
    
    

    features = pd.DataFrame(data,index = [0])
    return features 
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)



with open(file="final_model.sav",mode="rb") as f1:
    model = pickle.load(f1)
    
    
prediction = model.predict(df)
#prediction_proba = clf.predict_proba(df)

st.subheader('Predicted Result')
#st.write('Yes' if prediction_proba[0][1] > 0.5 else 'No')

#st.subheader('Prediction Probability')
st.write(prediction[0])
















