import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import altair as alt

st.title("Simple Linear Regression with CRISP-DM")

st.sidebar.header("CRISP-DM Steps")
st.sidebar.markdown("""
1. **Business Understanding:** The goal is to understand the relationship between two variables by fitting a linear model. This app allows you to see how the model changes with different parameters.
2. **Data Understanding:** We generate synthetic data to explore the concepts of linear regression. You can control the data generation process.
3. **Data Preparation:** The data is generated and prepared for modeling.
4. **Modeling:** A simple linear regression model is trained on the generated data.
5. **Evaluation:** The model is evaluated by visualizing the regression line and its equation.
6. **Deployment:** This Streamlit app is the deployment of the model.
""")


st.sidebar.header("Parameters")
# Allow user to modify a in ax+b, noise, number of points
a = st.sidebar.slider("Slope (a)", -10.0, 10.0, 2.5, 0.1)
noise = st.sidebar.slider("Noise", 0.0, 10.0, 2.0, 0.1)
num_points = st.sidebar.slider("Number of points", 50, 500, 200, 10)
b = 5 # let's keep b constant for simplicity

# Data Generation
X = np.linspace(-10, 10, num_points)
y = a * X + b + np.random.normal(0, noise, num_points)
df = pd.DataFrame({"X": X, "y": y})

# Modeling
model = LinearRegression()
model.fit(df[["X"]], df["y"])
y_pred = model.predict(df[["X"]])
df["y_pred"] = y_pred


# Evaluation
st.header("Data and Regression Model")

chart = alt.Chart(df).mark_circle(size=60).encode(
    x='X',
    y='y',
    tooltip=['X', 'y']
).interactive()

regression_line = alt.Chart(df).mark_line(color='red').encode(
    x='X',
    y='y_pred'
)

st.altair_chart(chart + regression_line, use_container_width=True)

st.write(f"Regression Equation: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}")
