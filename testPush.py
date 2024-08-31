 output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(data)
    output.seek(0)

    return Response(output.getvalue(), mimetype='text/csv')

npm install papaparse

import React, { useEffect, useState } from 'react';
import Papa from 'papaparse';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto';

function App() {
  const [data, setData] = useState({ labels: [], datasets: [] });

  useEffect(() => {
    fetch('http://localhost:5000/data')
      .then(response => response.text())
      .then(csvData => {
        Papa.parse(csvData, {
          header: true,
          skipEmptyLines: true,
          complete: (results) => {
            const labels = results.data.map(row => row.Column1);
            const values = results.data.map(row => row.Column2);

            setData({
              labels: labels,
              datasets: [{
                label: 'Sample Data',
                data: values,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
              }]
            });
          }
        });
      });
  }, []);

  return (
    <div>
      <h1>Chart Example</h1>
      <Line data={data} />
    </div>
  );
}

export default App;
