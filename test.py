import React, { useState, useEffect } from 'react';

function DropdownExample() {
  const [deployments, setDeployments] = useState([]); // List of deployment names
  const [firstDropdownValue, setFirstDropdownValue] = useState(''); // Selected deployment
  const [secondDropdownOptions, setSecondDropdownOptions] = useState([]); // Options for the second dropdown

  // Fetch deployment names from Flask API when the component mounts
  useEffect(() => {
    const fetchDeployments = async () => {
      try {
        const response = await fetch('http://localhost:5000/get-deployments');
        const data = await response.json();
        setDeployments(data); // Set the deployment names in the first dropdown
      } catch (error) {
        console.error("Error fetching deployments:", error);
      }
    };

    fetchDeployments();
  }, []); // Empty array to run this once when the component loads

  // Fetch second dropdown options based on the selected deployment name
  const fetchSecondDropdownOptions = async (selectedDeployment) => {
    try {
      const response = await fetch(`http://localhost:5000/get-deployment-details?deployment_name=${selectedDeployment}`);
      const data = await response.json();
      setSecondDropdownOptions(data); // Set the second dropdown options
    } catch (error) {
      console.error("Error fetching second dropdown options:", error);
      setSecondDropdownOptions([]); // Set to empty if there's an error
    }
  };

  // Handle first dropdown selection change
  const handleFirstDropdownChange = (e) => {
    const selectedValue = e.target.value;
    setFirstDropdownValue(selectedValue); // Set selected deployment in state
    fetchSecondDropdownOptions(selectedValue); // Fetch second dropdown options based on the selection
  };

  return (
    <div>
      {/* First dropdown (deployments) */}
      <select value={firstDropdownValue} onChange={handleFirstDropdownChange}>
        <option value="">Select a deployment</option>
        {deployments.map((deployment, index) => (
          <option key={index} value={deployment}>
            {deployment}
          </option>
        ))}
      </select>

      {/* Second dropdown (dynamic options) */}
      <select>
        <option value="">Select an option</option>
        {secondDropdownOptions.length > 0 ? (
          secondDropdownOptions.map((option, index) => (
            <option key={index} value={option}>
              {option}
            </option>
          ))
        ) : (
          <option value="">No options available</option>
        )}
      </select>
    </div>
  );
}

export default DropdownExample;
