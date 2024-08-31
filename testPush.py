npm install chart.js react-chartjs-2

// src/BarChart.js
import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

// Register chart components
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const BarChart = () => {
  const [chartData, setChartData] = useState({ labels: [], datasets: [] });

  useEffect(() => {
    fetch('http://localhost:5000/api/data')
      .then(response => response.json())
      .then(data => {
        setChartData({
          labels: data.labels,
          datasets: [
            {
              label: 'My Data',
              data: data.values,
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1
            }
          ]
        });
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h2>Bar Chart</h2>
      <Bar
        data={chartData}
        options={{
          responsive: true,
          plugins: {
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Bar Chart Example',
            },
          },
        }}
      />
    </div>
  );
};

export default BarChart;




/ src/App.js
import React from 'react';
import './App.css';
import BarChart from './BarChart';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Dashboard</h1>
        <BarChart />
      </header>
    </div>
  );
}

export default App;
