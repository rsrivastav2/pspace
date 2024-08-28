# Generate future dates
future_dates = pd.date_range(start='2024-04-01', periods=30, freq='D')
future_df = pd.DataFrame({'DATE': future_dates})

# Create features for future dates
future_df['YEAR'] = future_df['DATE'].dt.year
future_df['MONTH'] = future_df['DATE'].dt.month
future_df['DAY'] = future_df['DATE'].dt.day
future_df['DAY_OF_WEEK'] = future_df['DATE'].dt.dayofweek

# To create lag features for future data, you need to append past data to the future DataFrame
# to simulate the lag behavior. Here, I append the most recent data from the original dataset.
last_known_data = df[['COUNT_LAG1', 'COUNT_LAG2', 'COUNT_LAG3']].iloc[-1]
for i in range(3):
    future_df[f'COUNT_LAG{i+1}'] = np.nan

# Initialize lag values for future data
future_df.iloc[0, -3:] = last_known_data.values

# Fill in lag values by shifting them from the known historical data
for i in range(1, len(future_df)):
    future_df.loc[i, 'COUNT_LAG1'] = future_df.loc[i-1, 'COUNT'] if i > 0 else np.nan
    future_df.loc[i, 'COUNT_LAG2'] = future_df.loc[i-2, 'COUNT'] if i > 1 else np.nan
    future_df.loc[i, 'COUNT_LAG3'] = future_df.loc[i-3, 'COUNT'] if i > 2 else np.nan

# Fill lag values by predicting the counts
for i in range(3):
    future_df[f'COUNT_LAG{i+1}'] = future_df[f'COUNT_LAG{i+1}'].fillna(0)

# Predict counts for future dates
X_future = future_df[['YEAR', 'MONTH', 'DAY', 'DAY_OF_WEEK', 'COUNT_LAG1', 'COUNT_LAG2', 'COUNT_LAG3']]
future_df['PREDICTED_COUNT'] = model.predict(X_future)

# Display the future dates with predicted counts
print(future_df[['DATE', 'PREDICTED_COUNT']])
