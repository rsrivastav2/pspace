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
