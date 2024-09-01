const [responseText, setResponseText] = useState('');

  useEffect(() => {
    // Replace with your API URL
    fetch('http://localhost:5000/data')
      .then(response => response.text()) // Get the response text
      .then(text => setResponseText(text)) // Save it to state
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h1>Response Text</h1>
      <pre>{responseText}</pre> {/* Use <pre> to preserve formatting */}
    </div>
  );
}


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Load the data
data = pd.read_csv('path/to/your/data.csv')

# Convert date-related features to numeric if they aren't already
data['date'] = pd.to_datetime(data[['year', 'month', 'date']])
data['day_of_week'] = data['date'].dt.dayofweek
data['day_of_year'] = data['date'].dt.dayofyear

# Drop columns that are no longer needed
data.drop(columns=['date'], inplace=True)  # Remove 'date' column if not needed

# Define features and target
X = data[['month', 'year', 'day_of_week', 'day_of_year']]
y = data['count']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize/Scale features
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the neural network model
model = Sequential([
    Dense(64, input_dim=X_train_scaled.shape[1], activation='relu'),
    Dense(32, activation='relu'),
    Dense(1)  # Output layer for regression
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# Train the model
history = model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=1)

# Evaluate the model
loss = model.evaluate(X_test_scaled, y_test, verbose=1)
print(f'Test Loss: {loss}')

# Predict with the model (optional)
predictions = model.predict(X_test_scaled)
