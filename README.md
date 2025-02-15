# Combined-Cycle-Power-Plant
In this project, we aim to build a model to predict the electrical energy output of a Combined Cycle Power Plant. This plant utilizes gas turbines, steam turbines, and heat recovery steam generators to produce power. We will use a dataset containing 9568 hourly average ambient environmental readings from sensors at the power plant for our model.

1. Modeling Approach
Type of Modeling Task: For predicting the electrical energy output of a Combined Cycle Power Plant, we need a regression approach since the target variable (PE) is continuous.
Features to Use: 
•	Temperature (T)
•	Ambient Pressure (AP)
•	Relative Humidity (RH)
•	Exhaust Vacuum (V).
 
Possible Algorithms: 
•	Linear Regression
•	Random Forest Regressor
Output Metrics:
•	Mean Absolute Error (MAE)
•	Mean Squared Error (MSE)
•	R-squared (R²)
2. Model Building
For building the model, I used below strategy 
•	Data Split: Training and Testing sets (80/20 split)
•	Validation Strategy: Cross-validation
•	Models Compared: Linear Regression, Random Forest Regressor
3. Model Evaluation
Cross-validation result indicates as Random Forest Regressor is performing better compared to Linear Regression
==> Linear Regression CV MAE: 3.631877866079249
==> Random Forest Regressor CV MAE: 2.477296928053348

Evaluation Metric: 
To determine the performance of the model, I used MAE, MSE, R-squared output metrics. Metrics are calculated on training set and got the below results
==> Final Model MAE: 2.329609195402295
==> Final Model MSE: 10.537997861180706
==> Final Model R-squared: 0.9636693399560956
 
4. Model Interpretation
The model explains 96% of the variance in the data (R-squared = 0.96).
