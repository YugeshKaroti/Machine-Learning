import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import streamlit as s
model = pickle.load(open(r"C:\Users\yuges\OneDrive\Desktop\drugs_model.pkl", "rb"))
pipe=pickle.load(open(r"C:\Users\yuges\OneDrive\Desktop\drugs_pipe.pkl","rb"))
Age = s.number_input("Enter the age")
Sex = s.selectbox('Select Gender', ('M', 'F'))
BP = s.selectbox('BP Condition', ('HIGH', 'LOW', 'NORMAL'))
Cholesterol = s.selectbox('Cholesterol', ('HIGH', 'NORMAL'))
Na_to_K = s.number_input("Enter the Na_to_K rate")
query=pd.DataFrame([[Age,Sex,BP,Cholesterol,Na_to_K]],columns=["Age","Sex","BP","Cholesterol","Na_to_K"])
q=pipe.transform(query)
pre = model.predict(q)

if s.button("Submit"):
    if pre == 0:
        s.write("Predicted Drug : Drug A")
    elif pre == 1:
        s.write("Predicted Drug : Drug B")
    elif pre == 2:
        s.write("Predicted Drug : Drug C")
    elif pre == 3:
        s.write("Predicted Drug : Drug X")
    else:
        s.write("Predicted Drug : Drug Y")
else:
    s.write("Click Submit")
