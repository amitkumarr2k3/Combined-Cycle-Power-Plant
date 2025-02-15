import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

# Load the dataset
df = pd.read_csv('CCPP_data.csv')

# Display the first few rows of the dataframe
print(df.head())

# Define features and target variable
X = df[['AT', 'V', 'AP', 'RH']]
y = df['PE']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
model_lr = LinearRegression()
model_rf = RandomForestRegressor(random_state=42)

# Cross-validation for Linear Regression
cv_scores_lr = cross_val_score(model_lr, X_train, y_train, cv=5, scoring='neg_mean_absolute_error')
print(f"Linear Regression CV MAE: {-cv_scores_lr.mean()}")

# Cross-validation for Random Forest Regressor
cv_scores_rf = cross_val_score(model_rf, X_train, y_train, cv=5, scoring='neg_mean_absolute_error')
print(f"Random Forest Regressor CV MAE: {-cv_scores_rf.mean()}")

# Train the final model
model_rf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model_rf.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Final Model MAE: {mae}")
print(f"Final Model MSE: {mse}")
print(f"Final Model R-squared: {r2}")