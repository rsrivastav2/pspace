npm install axios react-router-dom chart.js recharts @mui/material @emotion/react @emotion/styled

import React, { useEffect, useState } from 'react';
import { fetchData } from './api';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { Container, Typography, Paper } from '@mui/material';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const loadData = async () => {
      try {
        const result = await fetchData();
        setData(result);
      } catch (error) {
        console.error("Failed to fetch data", error);
      }
    };

    loadData();
  }, []);

  return (
    <Container>
      <Typography variant="h4" gutterBottom>Dashboard</Typography>
      <Paper style={{ padding: '20px', marginTop: '20px' }}>
        <Typography variant="h6">Sample Line Chart</Typography>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="value" stroke="#8884d8" />
          </LineChart>
        </ResponsiveContainer>
      </Paper>
    </Container>
  );
}

export default App;


/* src/App.css */
.Container {
  padding: 20px;
}

.Paper {
  padding: 20px;
  margin-top: 20px;
}

import './App.css';


// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './Dashboard';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        {/* Add more routes here */}
      </Routes>
    </Router>
  );
}
