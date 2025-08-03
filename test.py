import React from 'react';

function MultiDeploymentControl({ deployments, selectedDeployments, setSelectedDeployments }) {
  const toggleDeployment = (dep) => {
    setSelectedDeployments(prev =>
      prev.includes(dep) ? prev.filter(d => d !== dep) : [...prev, dep]
    );
  };

  const handleRestart = () => {
    if (selectedDeployments.length === 0) return;

    selectedDeployments.forEach(dep => {
      fetch('http://localhost:5000/restart-deployment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ deployment: dep, namespace: 'default' })
      })
        .then(res => res.json())
        .then(data => {
          alert(`Deployment: ${dep}\nStatus: ${data.status}`);
        })
        .catch(err => console.error(`Error restarting ${dep}:`, err));
    });
  };

  return (
    <div>
      <h3>Select Deployments to Restart</h3>
      {deployments?.length === 0 ? (
        <p>Loading deployments...</p>
      ) : (
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {deployments.map(dep => (
            <li key={dep}>
              <label>
                <input
                  type="checkbox"
                  checked={selectedDeployments.includes(dep)}
                  onChange={() => toggleDeployment(dep)}
                />
                {dep}
              </label>
            </li>
          ))}
        </ul>
      )}
      <button onClick={handleRestart} disabled={selectedDeployments.length === 0}>
        Restart Selected Deployments
      </button>
    </div>
  );
}

export default MultiDeploymentControl;
