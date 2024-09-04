.chart-container {
    position: absolute; /* Use absolute positioning */
    top: 20px; /* Distance from the top */
    right: 20px; /* Distance from the right */
    width: 800px; /* Fixed width for the chart */
    height: 400px; /* Fixed height for the chart */
    background: #fff; /* Optional: background color */
    border: 1px solid #ddd; /* Optional: border for visual clarity */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Optional: shadow for better visibility */
    padding: 20px; /* Optional: padding around the chart */
    box-sizing: border-box; /* Include padding and border in the element’s total width and height */
}

.chart-title {
    margin-bottom: 20px;
    font-size: 2rem;
    color: #333;
}
2. Update the React Component
Ensure your React component uses the updated CSS classes. The chart container should have the .chart-container class, and you can optionally include a .chart-title for the title.

Example React Component
jsx
Copy code
import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import axios from 'axios';
import './App.css'; // Import your CSS file if you have custom styles

const TrendLineChart = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/api/trend')  // Adjust the URL if needed
            .then(response => {
                setData(response.data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []);

    return (
        <div className="chart-container">
            <h1 className="chart-title">Trend Line Chart</h1>
            <LineChart width={800} height={400} data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="index" label={{ value: 'Index', position: 'bottom' }} />
                <YAxis label={{ value: 'Values', angle: -90, position: 'left' }} />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="ytest" stroke="#8884d8" dot={false} name="Actual Values" />
                <Line type="monotone" dataKey="ypred" stroke="#82ca9d" dot={false} name="Predicted Values" />
            </LineChart>
        </div>
    );
};

export default TrendLineChart;
3. Ensure the Parent Container is Positioned
For the .chart-container to be positioned absolutely within your React application, the parent container or <body> needs to have a relative position:

Example CSS for Parent Container
css
Copy code
/* App.css or index.css */

body, html {
    margin: 0;
    padding: 0;
    height: 100%;
}

#root {
    position: relative; /* Ensure the root element is relatively positioned */
    height: 100%;
}
Summary
Update CSS: Use absolute positioning for .chart-container to place it in the top right corner.
Update React Component: Ensure the React component uses the correct CSS classes.
Check Parent Container: Make sure the parent container (#root or <body>) is relatively positioned so that the absolute positioning of the chart works as expected.
By following these steps, you should be able to position the line chart in the top right corner of your React application. If you need any further customization or have additional questions, feel free to ask!





