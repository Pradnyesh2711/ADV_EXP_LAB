import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset
data = pd.read_csv('heart.csv')

# Sidebar filters
st.sidebar.header('Filter Options')
age_filter = st.sidebar.slider('Age Range', int(data['age'].min()), int(data['age'].max()), (40, 60))
sex_filter = st.sidebar.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')

filtered_data = data[(data['age'] >= age_filter[0]) & (data['age'] <= age_filter[1]) & (data['sex'] == sex_filter)]

# Title
st.title("Heart Disease Dashboard")

# Line and Area charts
st.subheader("Heart Rate Over Age")
line_chart = px.line(filtered_data, x='age', y='thalach', title='Heart Rate Over Age')
st.plotly_chart(line_chart)

st.subheader("Cholesterol Levels Over Age (Area Chart)")
area_chart = px.area(filtered_data, x='age', y='chol', title='Cholesterol Levels Over Age')
st.plotly_chart(area_chart)

# Box and Violin plots
st.subheader("Box and Violin Plots for Cholesterol Levels")
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

sns.boxplot(data=filtered_data, y='chol', ax=ax[0])
ax[0].set_title('Box Plot - Cholesterol')

sns.violinplot(data=filtered_data, y='chol', ax=ax[1])
ax[1].set_title('Violin Plot - Cholesterol')

st.pyplot(fig)

# Scatter plot with regression line
st.subheader("Regression Plot - Cholesterol vs Age")
fig, ax = plt.subplots(figsize=(6, 4))
sns.regplot(data=filtered_data, x='age', y='chol', ax=ax)
ax.set_title('Cholesterol vs Age (with Regression Line)')
st.pyplot(fig)

# 3D scatter plot
st.subheader("3D Plot of Age, Cholesterol, and Heart Rate")
fig = px.scatter_3d(filtered_data, x='age', y='chol', z='thalach', color='target', title='3D Plot of Age, Cholesterol, and Heart Rate')
st.plotly_chart(fig)

# Pie chart for Heart Disease target
st.subheader("Pie Chart - Heart Disease Distribution")
pie_chart = px.pie(filtered_data, names='target', title='Heart Disease Presence (0 = No, 1 = Yes)')
st.plotly_chart(pie_chart)

# Treemap for categorical variables
st.subheader("Treemap of Chest Pain Types")
treemap = px.treemap(filtered_data, path=['cp'], title='Treemap of Chest Pain Types')
st.plotly_chart(treemap)

# Conclusion and insights
st.subheader("Key Observations:")
st.write("""
- The line and area charts reveal the variation in heart rate and cholesterol levels across different age groups.
- The box and violin plots show the distribution and spread of cholesterol levels.
- The regression plot indicates a potential relationship between age and cholesterol levels.
- The 3D scatter plot visualizes the interplay between age, cholesterol, and heart rate, with colors showing heart disease presence.
- The pie chart illustrates the distribution of individuals with and without heart disease.
""")
