import React, { useState } from "react";
import axios from "axios";

const ScheduleXApp = () => {
  const [activeTab, setActiveTab] = useState("jobDetails");
  const [jobName, setJobName] = useState("");
  const [dependencies, setDependencies] = useState([]);

  const handleForceStart = async () => {
    try {
      const res = await axios.post("http://localhost:5000/api/force-start", { jobName });
      alert(res.data.message || "Job triggered successfully");
    } catch (err) {
      alert("Error: " + (err.response?.data?.message || err.message));
    }
  };

  const handleFetchDependencies = async () => {
    try {
      const res = await axios.get(`http://localhost:5000/api/dependencies?job=${jobName}`);
      setDependencies(res.data.dependencies || []);
    } catch (err) {
      alert("Error fetching dependencies");
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>ScheduleX</h1>

      <div style={styles.tabBar}>
        <button style={styles.tab(activeTab === "jobDetails")} onClick={() => setActiveTab("jobDetails")}>Job Details</button>
        <button style={styles.tab(activeTab === "forceStart")} onClick={() => setActiveTab("forceStart")}>Force Start</button>
        <button style={styles.tab(activeTab === "jobDependencies")} onClick={() => setActiveTab("jobDependencies")}>Job Dependencies</button>
      </div>

      <div style={styles.content}>
        {activeTab === "jobDetails" && (
          <div>
            <h2>Job Details</h2>
            <p>Display job metadata and status here...</p>
          </div>
        )}

        {activeTab === "forceStart" && (
          <div>
            <h2>Force Start a Job</h2>
            <input
              style={styles.input}
              placeholder="Enter job name"
              value={jobName}
              onChange={(e) => setJobName(e.target.value)}
            />
            <button style={styles.button} onClick={handleForceStart}>Submit</button>
          </div>
        )}

        {activeTab === "jobDependencies" && (
          <div>
            <h2>Fetch Job Dependencies</h2>
            <input
              style={styles.input}
              placeholder="Enter job name"
              value={jobName}
              onChange={(e) => setJobName(e.target.value)}
            />
            <button style={styles.button} onClick={handleFetchDependencies}>Submit</button>

            {dependencies.length > 0 && (
              <div style={styles.dependencies}>
                <h3>Dependencies:</h3>
                <ul>
                  {dependencies.map((dep, idx) => <li key={idx}>{dep}</li>)}
                </ul>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

const styles = {
  container: {
    fontFamily: "Arial, sans-serif",
    maxWidth: "800px",
    margin: "20px auto",
    padding: "20px",
    border: "1px solid #ccc",
    borderRadius: "10px",
  },
  title: {
    textAlign: "center",
    color: "#333",
  },
  tabBar: {
    display: "flex",
    justifyContent: "space-around",
    marginBottom: "20px",
  },
  tab: (isActive) => ({
    padding: "10px 20px",
    cursor: "pointer",
    borderBottom: isActive ? "2px solid blue" : "2px solid transparent",
    backgroundColor: isActive ? "#f0f8ff" : "#fff",
    borderRadius: "6px",
  }),
  content: {
    padding: "20px",
    border: "1px solid #eee",
    borderRadius: "6px",
    backgroundColor: "#fafafa",
  },
  input: {
    padding: "10px",
    width: "100%",
    marginBottom: "10px",
    border: "1px solid #ccc",
    borderRadius: "4px",
  },
  button: {
    padding: "10px 20px",
    backgroundColor: "#007BFF",
    color: "white",
    border: "none",
    borderRadius: "4px",
    cursor: "pointer",
  },
  dependencies: {
    marginTop: "20px",
    backgroundColor: "#f1f1f1",
    padding: "10px",
    borderRadius: "6px",
  },
};

export default ScheduleXApp;
