import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import axios from 'axios';

const MyBarChart = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/api/data')  // Adjust URL if necessary
            .then(response => {
                console.log('Data fetched from API:', response.data);  // Log the data
                if (Array.isArray(response.data)) {
                    setData(response.data);
                } else {
                    console.error('Expected data to be an array.');
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []);

    return (
        <div>
            <h1>Bar Chart</h1>
            <BarChart width={600} height={300} data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="count" fill="#8884d8" />
            </BarChart>
        </div>
    );
};

export default MyBarChart;
