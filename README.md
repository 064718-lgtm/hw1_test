# Interactive Simple Linear Regression Application

This project is an interactive web application built with Streamlit that demonstrates the principles of simple linear regression. It serves as an educational tool to visualize how a regression model is affected by changes in the underlying data.

The application follows the Cross-Industry Standard Process for Data Mining (CRISP-DM) methodology.

## Features

- **Interactive Controls:** Modify the parameters of the data generation process in real-time using sidebar sliders.
    - **Slope (a):** Control the slope of the underlying linear relationship.
    - **Noise:** Adjust the amount of random noise added to the data points.
    - **Number of Points:** Change the size of the dataset.
- **Real-time Visualization:** The scatter plot and regression line are updated instantly as you change the parameters.
- **Model Evaluation:** The calculated regression equation (y = mx + c) is displayed, allowing you to compare the model's learned parameters to the actual parameters used for data generation.

## Methodology (CRISP-DM)

The project structure and workflow are based on the CRISP-DM framework:

1.  **Business Understanding:** To create an educational tool for understanding linear regression.
2.  **Data Understanding:** Using synthetically generated data that the user can control.
3.  **Data Preparation:** Generating and formatting the data on the fly.
4.  **Modeling:** Applying `scikit-learn`'s `LinearRegression` model.
5.  **Evaluation:** Visually inspecting the model's fit and its equation.
6.  **Deployment:** Deploying the interactive model as a Streamlit web app.

## Setup and Usage

1.  **Prerequisites:** Ensure you have Python 3.6+ installed.

2.  **Clone the repository (optional):**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    streamlit run linear_regression_app/app.py
    ```

Once running, open the provided local URL in your web browser to start using the application.
