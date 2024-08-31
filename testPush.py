import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Step 1: Prepare Data
# Sample DataFrame
df = pd.DataFrame({
    'DATE': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'COUNT': range(100)
})

# Step 2: Feature Engineering
df['Year'] = df['DATE'].dt.year
df['Month'] = df['DATE'].dt.month
df['Day'] = df['DATE'].dt.day
df['DayOfWeek'] = df['DATE'].dt.dayofweek
df['WeekOfYear'] = df['DATE'].dt.isocalendar().week
df['Quarter'] = df['DATE'].dt.quarter
df['IsWeekend'] = (df['DATE'].dt.dayofweek >= 5).astype(int)

# Lag features
df['COUNT_t-1'] = df['COUNT'].shift(1)
df['COUNT_t-2'] = df['COUNT'].shift(2)

# Rolling statistics
df['RollingMean_7'] = df['COUNT'].rolling(window=7).mean()
df['RollingStd_7'] = df['COUNT'].rolling(window=7).std()

# Drop rows with NaN values generated by lagging/rolling operations
df = df.dropna()

# Step 3: Train-Test Split
# Create target variable and features
X = df.drop(columns=['DATE', 'COUNT'])
y = df['COUNT']

# Convert categorical features to numeric if needed
# Here, all features are numeric except the week number; you might need to ensure no categorical data is left
# In this case, the WeekOfYear is already numeric but verify other potential issues

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Step 4: Train the Model
model = XGBRegressor(objective='reg:squarederror', n_estimators=100)
model.fit(X_train, y_train)

# Step 5: Evaluate the Model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Step 6: Predict Future Dates
# Generate future dates
future_dates = pd.date_range(start='2024-04-01', periods=10, freq='D')

# Create DataFrame for future dates with similar feature engineering
future_df = pd.DataFrame({
    'DATE': future_dates
})
future_df['Year'] = future_df['DATE'].dt.year
future_df['Month'] = future_df['DATE'].dt.month
future_df['Day'] = future_df['DATE'].dt.day
future_df['DayOfWeek'] = future_df['DATE'].dt.dayofweek
future_df['WeekOfYear'] = future_df['DATE'].dt.isocalendar().week
future_df['Quarter'] = future_df['DATE'].dt.quarter
future_df['IsWeekend'] = (future_df['DATE'].dt.dayofweek >= 5).astype(int)

# For future dates, lag features and rolling statistics need to be approximated
# (These would normally require the actual future counts for accurate prediction)
# As a workaround, we'll use the last available values
last_available = df.iloc[-1]
future_df['COUNT_t-1'] = last_available['COUNT']
future_df['COUNT_t-2'] = last_available['COUNT']
future_df['RollingMean_7'] = last_available['RollingMean_7']
future_df['RollingStd_7'] = last_available['RollingStd_7']

# Predict future counts
future_X = future_df.drop(columns=['DATE'])
future_predictions = model.predict(future_X)

# Add predictions to future_df
future_df['Predicted_COUNT'] = future_predictions

print(future_df[['DATE', 'Predicted_COUNT']])
