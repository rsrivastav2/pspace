import React, { useEffect, useState } from 'react';

function Dropdown() {
    const [options, setOptions] = useState([]);
    
    // Fetch data when the component mounts
    useEffect(() => {
        fetch('http://localhost:5000/api/data')
            .then((response) => response.json())
            .then((data) => {
                setOptions(data); // Store the API response in state
            })
            .catch((error) => {
                console.error('Error fetching data:', error);
            });
    }, []);

    return (
        <select>
            {options.map((option) => (
                <option key={option.id} value={option.id}>
                    {option.name}
                </option>
            ))}
        </select>
    );
}

export default Dropdown;
