import React, { useState, useEffect } from 'react';

function Dropdowns() {
    const [firstDropdownValue, setFirstDropdownValue] = useState('');
    const [secondDropdownOptions, setSecondDropdownOptions] = useState([]);
    
    // Handle change in first dropdown
    const handleFirstDropdownChange = (event) => {
        const selectedValue = event.target.value;
        setFirstDropdownValue(selectedValue);
        
        // Fetch data only if a valid value is selected
        if (selectedValue) {
            fetchData(selectedValue);  // Fetch data based on the selected value
        } else {
            setSecondDropdownOptions([]); // Clear the second dropdown if no value is selected
        }
    };

    // Fetch data for the second dropdown based on the selected value from the first dropdown
    const fetchData = (selectedValue) => {
        fetch(`http://localhost:5000/api/data?selected=${selectedValue}`)
            .then((response) => response.json())
            .then((data) => {
                setSecondDropdownOptions(data); // Populate second dropdown with API data
            })
            .catch((error) => {
                console.error('Error fetching data:', error);
                setSecondDropdownOptions([]); // Clear second dropdown in case of error
            });
    };

    return (
        <div>
            {/* First Dropdown */}
            <select onChange={handleFirstDropdownChange} value={firstDropdownValue}>
                <option value="">Select an option</option>
                <option value="option1">Option 1</option>
                <option value="option2">Option 2</option>
                {/* Add more options here if needed */}
            </select>

            {/* Second Dropdown */}
            <select>
                <option value="">Select result</option>
                {secondDropdownOptions.length > 0 ? (
                    secondDropdownOptions.map((option) => (
                        <option key={option.id} value={option.id}>
                            {option.name}
                        </option>
                    ))
                ) : (
                    <option value="">No results</option>
                )}
            </select>
        </div>
    );
}

export default Dropdowns;
