data = {
    'DATE': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'COUNT': np.random.randint(0, 100, size=100)
}
df = pd.DataFrame(data)

# Convert DATE to datetime
df['DATE'] = pd.to_datetime(df['DATE'])

# Create features from DATE
df['YEAR'] = df['DATE'].dt.year
df['MONTH'] = df['DATE'].dt.month
df['DAY'] = df['DATE'].dt.day
df['DAY_OF_WEEK'] = df['DATE'].dt.dayofweek

# Feature engineering - lag features
df['COUNT_LAG1'] = df['COUNT'].shift(1)
df['COUNT_LAG2'] = df['COUNT'].shift(2)
df['COUNT_LAG3'] = df['COUNT'].shift(3)

# Drop rows with NaN values (result of shifting)
df = df.dropna()

# Define features and target
X = df[['YEAR', 'MONTH', 'DAY', 'DAY_OF_WEEK', 'COUNT_LAG1', 'COUNT_LAG2', 'COUNT_LAG3']]
y = df['COUNT']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
