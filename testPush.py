from flask import Flask, jsonify
import pandas as pd
import numpy as np
import xgboost as xgb

app = Flask(__name__)

# Load your pre-trained model
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100)
model.load_model('xgboost_model.json')  # Adjust path as needed

@app.route('/predict', methods=['GET'])
def predict():
    # Generate future dates
    future_dates = pd.date_range(start='2024-04-01', periods=30, freq='D')
    future_df = pd.DataFrame({'DATE': future_dates})

    # Create features for future dates
    future_df['YEAR'] = future_df['DATE'].dt.year
    future_df['MONTH'] = future_df['DATE'].dt.month
    future_df['DAY'] = future_df['DATE'].dt.day
    future_df['DAY_OF_WEEK'] = future_df['DATE'].dt.dayofweek

    # For simplicity, use static lag values
    future_df['COUNT_LAG1'] = np.nan
    future_df['COUNT_LAG2'] = np.nan
    future_df['COUNT_LAG3'] = np.nan
    future_df.loc[0, ['COUNT_LAG1', 'COUNT_LAG2', 'COUNT_LAG3']] = [0, 0, 0]  # Initial lags

    # Predict counts for future dates
    X_future = future_df[['YEAR', 'MONTH', 'DAY', 'DAY_OF_WEEK', 'COUNT_LAG1', 'COUNT_LAG2', 'COUNT_LAG3']]
    future_df['PREDICTED_COUNT'] = model.predict(X_future)

    # Prepare response
    result = future_df[['DATE', 'PREDICTED_COUNT']].to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
