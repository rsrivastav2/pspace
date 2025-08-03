import React, { useState, useEffect } from 'react';

function MultiDeploymentControl() {
  const [deployments, setDeployments] = useState([]);
  const [selectedDeployments, setSelectedDeployments] = useState([]);

  // Fetch deployments on load
  useEffect(() => {
    fetch('http://localhost:5000/deployments')
      .then(res => res.json())
      .then(data => setDeployments(data.deployments))
      .catch(err => console.error(err));
  }, []);

  // Toggle checkbox selection
  const toggleDeployment = (deployment) => {
    setSelectedDeployments(prev =>
      prev.includes(deployment)
        ? prev.filter(d => d !== deployment)
        : [...prev, deployment]
    );
  };

  // Restart selected deployments
  const handleRestart = () => {
    if (selectedDeployments.length === 0) return;

    selectedDeployments.forEach(dep => {
      fetch('http://localhost:5000/restart-deployment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ deployment: dep, namespace: 'default' })
      })
        .then(res => res.json())
        .then(data =>
          alert(`Deployment: ${dep}\nStatus: ${data.status}\nMessage: ${data.output || data.error}`)
        )
        .catch(err => console.error(`Error restarting ${dep}:`, err));
    });
  };

  return (
    <div>
      <h3>Select Deployments to Restart</h3>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {deployments.map(dep => (
          <li key={dep}>
            <label>
              <input
                type="checkbox"
                value={dep}
                checked={selectedDeployments.includes(dep)}
                onChange={() => toggleDeployment(dep)}
              />
              {dep}
            </label>
          </li>
        ))}
      </ul>
      <button onClick={handleRestart} disabled={selectedDeployments.length === 0}>
        Restart Selected Deployments
      </button>
    </div>
  );
}

export default MultiDeploymentControl;

