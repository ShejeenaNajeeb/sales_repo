#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("sales_Dataset")

#import dataset
df = pd.read_csv('supermarket_sales.csv')
#First thirty rows
sales = df.head(30)
#Display the table
st.table(sales)
st.header("Visualisation Using Seaborn")
#bar plot
st.subheader("Bar Plot")
sales.plot(kind='bar')
st.pyplot()
#Displot
st.subheader("Displot")
sns.displot(sales['Total'])
st.pyplot()
#joinplot
st.subheader("JointPlot")
sns.jointplot(x='Total',y='Unit price',data=sales,kind='scatter')
st.pyplot()
#pairplot
st.subheader("Pairplot")
sns.pairplot(sales,hue='Payment',palette='rainbow')
st.pyplot()
#Rugplot
st.subheader("Rugplot")
sns.rugplot(sales['gross income'])
st.pyplot()
#Correation
st.subheader("Heatmap")
sns.heatmap(sales.corr(),cmap='coolwarm',annot=True)
st.pyplot()

