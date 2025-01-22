import React, { useState } from 'react';

function MyDropdown() {
  // State to store the selected value
  const [selectedValue, setSelectedValue] = useState('');

  // Handle dropdown value change
  const handleChange = (event) => {
    setSelectedValue(event.target.value);
  };

  // Handle form submission and send the selected value to Flask API
  const handleSubmit = async (event) => {
    event.preventDefault();  // Prevent form from reloading the page

    try {
      const response = await fetch('http://localhost:5000/api/endpoint', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ selectedValue: selectedValue }),
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Response from API:', data);
      } else {
        console.error('Error from API:', response.status);
      }
    } catch (error) {
      console.error('Error in sending request:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <select value={selectedValue} onChange={handleChange}>
          <option value="">Select a value</option>
          <option value="value1">Value 1</option>
          <option value="value2">Value 2</option>
          <option value="value3">Value 3</option>
        </select>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default MyDropdown;
