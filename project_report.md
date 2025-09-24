# Project Report: Simple Linear Regression with CRISP-DM

## 1. Business Understanding
The primary goal of this project is to develop an interactive tool to understand the fundamental relationship between two variables by fitting a linear model. The application is designed to allow users to see in real-time how a linear regression model adapts when its underlying data-generation parameters are modified. This serves as an educational tool for data science concepts.

## 2. Data Understanding
To explore the concepts of linear regression without the need for an external dataset, we generate synthetic data. The data is created based on the linear equation `y = ax + b`, with an adjustable amount of random noise. The user has control over the following parameters:
- **Slope (a):** The coefficient of the independent variable X.
- **Noise:** The standard deviation of the random noise added to the data.
- **Number of points:** The size of the generated dataset.

## 3. Data Preparation
The synthetic data is generated within the application itself. A range of X values is created using `numpy.linspace`, and the corresponding y values are calculated based on the user-defined slope `a`, a fixed intercept `b`, and random noise. The data is then loaded into a pandas DataFrame, which is a suitable structure for training the model.

## 4. Modeling
A simple linear regression model from `scikit-learn` (`sklearn.linear_model.LinearRegression`) is used. The model is trained on the generated (X, y) data points to find the best-fit line that minimizes the residual sum of squares.

## 5. Evaluation
The model's performance is evaluated visually. The application plots:
- The original scattered data points.
- The resulting regression line predicted by the model.

Additionally, the equation of the regression line (`y = mx + c`) is displayed, showing the learned coefficient (slope) and intercept. This allows for a direct comparison between the parameters used to generate the data and the parameters learned by the model.

## 6. Deployment
The model and its interactive controls are deployed as a web application using the Streamlit framework. This provides an accessible and user-friendly interface for interacting with the linear regression model and observing its behavior.