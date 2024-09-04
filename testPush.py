import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, Scatter, ScatterChart } from 'recharts';
import axios from 'axios';

const TrendChart = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/api/trend')
            .then(response => setData(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Trend Line Chart</h1>
            <ScatterChart width={600} height={400}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="ytest" name="Actual Values" />
                <YAxis dataKey="ypred" name="Predicted Values" />
                <Tooltip />
                <Legend />
                <Scatter name="Data" data={data} fill="#8884d8" />
                <Line type="monotone" dataKey="ytest" stroke="#ff7300" />
            </ScatterChart>
        </div>
    );
};

export default TrendChart;
