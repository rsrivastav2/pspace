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


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LeakyReLU, PReLU, ELU, Dropout
from tensorflow.keras.optimizers import Adam

# Sample Data Creation
np.random.seed(42)
data_size = 1000
X = np.random.rand(data_size, 10)  # 10 features
y = np.random.randint(2, size=data_size)  # Binary classification

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the Model
model = Sequential([
    Dense(128, input_dim=X_train_scaled.shape[1]),
    LeakyReLU(alpha=0.01),  # Using Leaky ReLU
    Dropout(0.5),
    
    Dense(64),
    PReLU(),  # Using PReLU
    Dropout(0.5),
    
    Dense(32),
    ELU(alpha=1.0),  # Using ELU
    Dropout(0.5),
    
    Dense(1, activation='sigmoid')  # Output layer for binary classification
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
