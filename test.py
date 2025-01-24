import React, { useState, useEffect } from "react";

const MyComponent = () => {
  const [firstDropdownValue, setFirstDropdownValue] = useState(""); // State for first dropdown
  const [secondDropdownData, setSecondDropdownData] = useState([]); // State for second dropdown options
  const [loading, setLoading] = useState(false); // Loading state

  // API call to fetch data for second dropdown
  const fetchSecondDropdownData = async (value) => {
    setLoading(true);
    try {
      // Replace with your API URL and pass the selected value as a query parameter or in the request body
      const response = await fetch(`https://api.example.com/data?filter=${value}`);
      const data = await response.json();
      setSecondDropdownData(data); // Assuming the response is an array of options
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false);
    }
  };

  // Handle change event for the first dropdown
  const handleFirstDropdownChange = (event) => {
    const selectedValue = event.target.value;
    setFirstDropdownValue(selectedValue);
    fetchSecondDropdownData(selectedValue); // Fetch new data based on selected value
  };

  return (
    <div>
      <label htmlFor="first-dropdown">First Dropdown:</label>
      <select id="first-dropdown" value={firstDropdownValue} onChange={handleFirstDropdownChange}>
        <option value="">Select an option</option>
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
        {/* Add more options as needed */}
      </select>

      {loading && <p>Loading...</p>}

      <label htmlFor="second-dropdown">Second Dropdown:</label>
      <select id="second-dropdown">
        <option value="">Select an option</option>
        {secondDropdownData.length > 0 ? (
          secondDropdownData.map((item, index) => (
            <option key={index} value={item.id}> {/* Assuming 'id' is the value you want to send */}
              {item.name} {/* Assuming 'name' is the display text */}
            </option>
          ))
        ) : (
          <option value="">No data available</option>
        )}
      </select>
    </div>
  );
};

export default MyComponent;
