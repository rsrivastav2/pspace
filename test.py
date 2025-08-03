const fetchDeployments = async () => {
      try {
        const response = await axios.get('http://localhost:5000/deployments');
        console.log("API response:", response.data);  // ✅ confirm structure
        setDeployments(response.data.deployments);    // ✅ fix this line
      } catch (error) {
        console.error("Failed to load deployments:", error);
      }
    };

    fetchDeployments();
  }, []);

  return (
    <MultiDeploymentControl
      deployments={deployments}
      selectedDeployments={selectedDeployments}
      setSelectedDeployments={setSelectedDeployments}
    />
  );
}

export default App;
✅ Also: Check Your Flask API Response
Make sure the Flask API returns this structure:

json
Copy
Edit
{
  "deployments": ["nginx", "redis"]
}
Not:

json
Copy
Edit
{
  "data": {
    "deployments": [...]
  }
}
If it's nested, you'd use:

js
Copy
Edit
setDeployments(response.data.data.deployments);
Would you like to paste your actual Axios call or Flask response structure? I’ll confirm the exact fix.









Ask ChatGPT

Unlock more with Plus
