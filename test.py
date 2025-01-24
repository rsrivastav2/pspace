import React, { useState, useEffect } from 'react';

const MyComponent = () => {
  // States for dropdowns and API response
  const [firstDropdownValue, setFirstDropdownValue] = useState('');
  const [secondDropdownOptions, setSecondDropdownOptions] = useState([]);
  
  // Handle first dropdown change
  const handleFirstDropdownChange = (event) => {
    setFirstDropdownValue(event.target.value);
  };

  // Call API when first dropdown value changes
  useEffect(() => {
    if (firstDropdownValue) {
      // API call with the selected value
      fetch(`https://your-flask-api.com/endpoint?param=${firstDropdownValue}`)
        .then((response) => response.json())
        .then((data) => {
          // Assuming the response is an array of options for the second dropdown
          setSecondDropdownOptions(data);
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
        });
    }
  }, [firstDropdownValue]); // Only run the effect when firstDropdownValue changes

  return (
    <div>
      <select onChange={handleFirstDropdownChange} value={firstDropdownValue}>
        <option value="">Select Value</option>
        <option value="value1">Value 1</option>
        <option value="value2">Value 2</option>
        <option value="value3">Value 3</option>
        {/* Add more options here */}
      </select>

      <select>
        <option value="">Select Response</option>
        {secondDropdownOptions.map((option, index) => (
          <option key={index} value={option}>{option}</option>
        ))}
      </select>
    </div>
  );
};

export default MyComponent;
