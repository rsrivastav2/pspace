return (
        <div className="chart-container">
            <h1 className="chart-title">Bar Chart with Dates</h1>
            <BarChart width={600} height={300} data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis 
                    dataKey="date" 
                    tickFormatter={(tick) => new Date(tick).toLocaleDateString()} 
                />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="count" fill="#8884d8">
                    <LabelList dataKey="count" position="top" />
                </Bar>
            </BarChart>
        </div>
