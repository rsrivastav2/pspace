import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'recharts';

const App = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/predict')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the data!', error);
      });
  }, []);

  return (
    <div>
      <h1>Future Predictions</h1>
      <BarChart width={600} height={300} data={data}>
        <XAxis dataKey="DATE" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="PREDICTED_COUNT" fill="#8884d8" />
      </BarChart>
    </div>
  );
};

export default App;
