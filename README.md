# Problem Statement

## Modeling and Forecasting COVID-19 Dynamics in the United States Using Logistic Growth Models

The COVID-19 pandemic has had a profound impact on public health, healthcare infrastructure, and socioeconomic systems worldwide. Understanding the dynamics of infectious disease spread through mathematical and computational modeling is essential for analyzing epidemic trends, evaluating growth patterns, and developing data-driven forecasting approaches.

This project focuses on developing a mathematical and data science framework to analyze and predict the progression of COVID-19 cases in the United States using the **logistic growth model**. The logistic growth model provides a mathematical representation of cumulative growth that initially increases exponentially before gradually slowing as it approaches an estimated upper asymptote, commonly referred to as the carrying capacity.

The primary problem addressed in this project is determining how effectively a logistic growth model can characterize historical COVID-19 case trajectories and forecast cumulative confirmed cases over selected future time intervals. Using historical COVID-19 surveillance data, the project will investigate epidemic growth patterns, estimate model parameters, and evaluate the predictive performance of the mathematical model.

The analysis will incorporate data collection, preprocessing, exploratory data analysis, nonlinear parameter estimation, numerical simulation, and statistical model evaluation. Python and its scientific computing ecosystem will be used for data processing, visualization, and predictive modeling. MATLAB will provide an independent computational environment for implementing the logistic growth equations, performing numerical optimization, and validating model outputs. Jupyter Notebook will serve as the primary interactive research environment for documenting the analytical workflow and communicating results.

Model performance will be evaluated using statistical measures, including Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the coefficient of determination (R²). Chronological training and testing datasets will be used to assess forecasting performance and minimize information leakage.

An additional objective is to investigate the limitations of the classical logistic growth model when applied to a complex, multi-wave epidemic. Changes in transmission dynamics, viral variants, vaccination patterns, public health interventions, testing availability, and reporting practices can influence observed case trajectories and reduce the accuracy of long-term predictions.

Ultimately, this project aims to demonstrate how mathematical modeling, statistical analysis, and computational data science can be integrated to study infectious disease dynamics. The findings will provide insight into the applicability, predictive capabilities, and limitations of logistic growth models in epidemiological forecasting.

## Primary Research Objective

To develop, implement, and evaluate a logistic growth-based computational model for characterizing historical COVID-19 case trajectories and forecasting cumulative confirmed cases in the United States.

## Key Research Questions

1. How effectively can the logistic growth model represent the cumulative progression of reported COVID-19 cases in the United States?
2. What are the estimated growth rate and carrying capacity parameters for selected epidemic waves?
3. How accurately can the model forecast cumulative confirmed cases over 7-day, 14-day, and 30-day prediction horizons?
4. How does forecasting performance change across different epidemic waves?
5. What are the limitations of applying a classical logistic growth model to a multi-wave infectious disease outbreak?
6. How consistent are the estimated model parameters and predictions between Python and MATLAB implementations?

## Expected Outcomes

- A cleaned and structured historical COVID-19 dataset for the United States.
- Exploratory data analysis and visualizations of epidemic growth patterns.
- A mathematically formulated and computationally implemented logistic growth model.
- Estimated logistic growth parameters using nonlinear optimization.
- Short-term cumulative case forecasts.
- Statistical evaluation of model performance.
- Independent Python and MATLAB implementation comparisons.
- A discussion of model assumptions, limitations, and potential improvements.

**Scope:** This project is intended as a retrospective computational and statistical modeling study using reported COVID-19 case data. Predictions are model-based estimates rather than official public health forecasts or measurements of all actual infections.
