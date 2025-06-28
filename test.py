import React from "react";
import { PieChart, Pie, Cell } from "recharts";

const JobDetails = () => {
  const cpuUsage = 30.5;
  const memoryUsage = 221;
  const cpuData = [
    { name: "Used", value: cpuUsage },
    { name: "Free", value: 100 - cpuUsage },
  ];
  const memData = [
    { name: "Used", value: memoryUsage },
    { name: "Free", value: 1000 - memoryUsage },
  ];

  const cardStyle = {
    border: "1px solid #ccc",
    borderRadius: "10px",
    padding: "20px",
    marginBottom: "20px",
  };

  const sectionTitle = {
    fontWeight: "bold",
    marginBottom: "10px",
    textAlign: "center",
  };

  const pieContainer = {
    display: "flex",
    justifyContent: "center",
    marginTop: "10px",
  };

  const buttonStyle = {
    marginTop: "10px",
    padding: "10px 20px",
    borderRadius: "6px",
    border: "1px solid #ccc",
    cursor: "pointer",
  };

  return (
    <div style={{ padding: "20px" }}>
      <div style={{ backgroundColor: "#FEF3C7", color: "#92400E", padding: "10px", borderRadius: "10px", marginBottom: "20px" }}>
        ⚠️ Error: Job Aborted: Manually aborted by user: admin
      </div>

      <div style={cardStyle}>
        <div style={{ display: "flex", justifyContent: "space-between" }}>
          <div>
            <div><strong>JOB ID:</strong> jino6d5h202</div>
            <div><strong>EVENT NAME:</strong> Test Event 2</div>
            <div><strong>EVENT TIMING:</strong> Disabled</div>
            <div><strong>CATEGORY NAME:</strong> Test Cat</div>
            <div><strong>PLUGIN NAME:</strong> Test Plugin</div>
            <div><strong>EVENT TARGET:</strong> joeretina.local</div>
          </div>
          <div>
            <div><strong>JOB SOURCE:</strong> Manual (admin)</div>
            <div><strong>SERVER HOSTNAME:</strong> joeretina.local</div>
            <div><strong>PROCESS ID:</strong> 32457</div>
            <div><strong>JOB STARTED:</strong> Apr 30, 2016 11:07 PM</div>
            <div><strong>JOB COMPLETED:</strong> Apr 30, 2016 11:07 PM</div>
            <div><strong>ELAPSED TIME:</strong> 20 seconds</div>
            <button style={buttonStyle}>Run Again</button>
          </div>
        </div>
      </div>

      <div style={{ display: "flex", gap: "20px", marginBottom: "20px" }}>
        <div style={cardStyle}>
          <div style={sectionTitle}>Performance Metrics</div>
          <div style={pieContainer}>
            <PieChart width={100} height={100}>
              <Pie
                data={[{ name: "total", value: 100 }]}
                cx="50%"
                cy="50%"
                innerRadius={30}
                outerRadius={50}
                fill="#0000FF"
                dataKey="value"
              />
            </PieChart>
          </div>
        </div>

        <div style={cardStyle}>
          <div style={sectionTitle}>CPU Usage</div>
          <div style={pieContainer}>
            <PieChart width={100} height={100}>
              <Pie
                data={cpuData}
                cx="50%"
                cy="50%"
                innerRadius={30}
                outerRadius={50}
                dataKey="value"
              >
                <Cell fill="#006400" />
                <Cell fill="#DDDDDD" />
              </Pie>
            </PieChart>
          </div>
          <div style={{ textAlign: "center", marginTop: "10px" }}>{cpuUsage}% Average</div>
        </div>

        <div style={cardStyle}>
          <div style={sectionTitle}>Memory Usage</div>
          <div style={pieContainer}>
            <PieChart width={100} height={100}>
              <Pie
                data={memData}
                cx="50%"
                cy="50%"
                innerRadius={30}
                outerRadius={50}
                dataKey="value"
              >
                <Cell fill="#006400" />
                <Cell fill="#DDDDDD" />
              </Pie>
            </PieChart>
          </div>
          <div style={{ textAlign: "center", marginTop: "10px" }}>{memoryUsage} MB Average</div>
        </div>
      </div>

      <div style={cardStyle}>
        <div style={sectionTitle}>Job Event Log</div>
        <pre style={{ backgroundColor: "#F3F4F6", padding: "10px", borderRadius: "6px", overflowX: "auto" }}>
# Job ID: jino6d5h202
# Event Title: Test Event 2
# Hostname: joeretina.local
# Date/Time: 2016/04/30 23:07:06 (GMT-7)
Printed this with console.warn, should go to stderr...
        </pre>
        <div style={{ display: "flex", gap: "10px", marginTop: "10px" }}>
          <button style={buttonStyle}>Download Log</button>
          <button style={buttonStyle}>View Full Log</button>
        </div>
      </div>
    </div>
  );
};

export default JobDetails;
