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

print(df.head())
