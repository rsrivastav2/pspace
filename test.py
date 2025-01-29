const handleButtonClick = async () => {
    if (!firstDropdownValue || !secondDropdownValue) {
      alert("Please select values from both dropdowns.");
      return;
    }

    try {
      const response = await fetch(
        `http://localhost:5000/api-endpoint/${firstDropdownValue}/${secondDropdownValue}`,
        {
          method: "GET", // or "POST" depending on your API
        }
      );
      const data = await response.json();
      console.log("API Response:", data);
    } catch (error) {
      console.error("Error while calling API:", error);
    }
  };
