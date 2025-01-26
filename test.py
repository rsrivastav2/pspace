import React, { useState, useEffect } from 'react';

function DropdownExample() {
  const [deployments, setDeployments] = useState([]);
  const [firstDropdownValue, setFirstDropdownValue] = useState('');
  const [secondDropdownOptions, setSecondDropdownOptions] = useState([]);

  // Fetch the AKS deployment names when the component loads
  useEffect(() => {
    const fetchDeployments = async () => {
      try {
        const response = await fetch('http://localhost:5000/get-deployments');
        const data = await response.json();
        setDeployments(data); // Update the deployments list
      } catch (error) {
        console.error("Error fetching deployments:", error);
      }
    };

    fetchDeployments();
  }, []);

  // Fetch the second dropdown options when the first dropdown value changes
  const fetchSecondDropdownOptions = async (firstValue) => {
    try {
      const response = await fetch(`http://localhost:5000/get-dropdown-options?first_value=${firstValue}`);
      const data = await response.json();
      setSecondDropdownOptions(data); // Update the second dropdown options
    } catch (error) {
      console.error("Error fetching dropdown options:", error);
    }
  };

  const handleFirstDropdownChange = (e) => {
    const selectedValue = e.target.value;
    setFirstDropdownValue(selectedValue);
    fetchSecondDropdownOptions(selectedValue); // Fetch second dropdown options based on first dropdown selection
  };

  return (
    <div>
      <select value={firstDropdownValue} onChange={handleFirstDropdownChange}>
        <option value="">Select a deployment</option>
        {deployments.map((deployment, index) => (
          <option key={index} value={deployment}>
            {deployment}
          </option>
        ))}
      </select>

      <select>
        <option value="">Select an option</option>
        {secondDropdownOptions.map((option, index) => (
          <option key={index} value={option}>
            {option}
          </option>
        ))}
      </select>
    </div>
  );
}

export default DropdownExample;
