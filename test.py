import React, { useState, useEffect } from 'react';

function DropdownExample() {
  const [deployments, setDeployments] = useState([]); // List of deployments for the first dropdown
  const [firstDropdownValue, setFirstDropdownValue] = useState(''); // Selected value from the first dropdown
  const [secondDropdownOptions, setSecondDropdownOptions] = useState([]); // Options for the second dropdown

  // Fetch the list of deployments when the component mounts
  useEffect(() => {
    const fetchDeployments = async () => {
      try {
        const response = await fetch('http://localhost:5000/get-deployments');
        const data = await response.json();
        setDeployments(data); // Set the deployments for the first dropdown
      } catch (error) {
        console.error("Error fetching deployments:", error);
      }
    };

    fetchDeployments();
  }, []); // Empty dependency array means this runs once when the component mounts

  // Fetch the second dropdown options based on the selected deployment
  const fetchSecondDropdownOptions = async (firstValue) => {
    try {
      const response = await fetch(`http://localhost:5000/get-deployment-details?deployment_name=${firstValue}`);
      const data = await response.json();

      // Ensure that the response is an array before setting it
      if (Array.isArray(data)) {
        setSecondDropdownOptions(data); // Set the second dropdown options
      } else {
        setSecondDropdownOptions([]); // If it's not an array, set an empty array
      }
    } catch (error) {
      console.error("Error fetching second dropdown options:", error);
      setSecondDropdownOptions([]); // Handle error case by setting an empty array
    }
  };

  const handleFirstDropdownChange = (e) => {
    const selectedValue = e.target.value;
    setFirstDropdownValue(selectedValue);
    fetchSecondDropdownOptions(selectedValue); // Fetch second dropdown options based on the first dropdown value
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
        {Array.isArray(secondDropdownOptions) && secondDropdownOptions.length > 0 ? (
          secondDropdownOptions.map((option, index) => (
            <option key={index} value={option}>
              {option}
            </option>
          ))
        ) : (
          <option value="">No options available</option> // Display if no options
        )}
      </select>
    </div>
  );
}

export default DropdownExample;
