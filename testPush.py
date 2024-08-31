const [responseText, setResponseText] = useState('');

  useEffect(() => {
    // Replace with your API URL
    fetch('http://localhost:5000/data')
      .then(response => response.text()) // Get the response text
      .then(text => setResponseText(text)) // Save it to state
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h1>Response Text</h1>
      <pre>{responseText}</pre> {/* Use <pre> to preserve formatting */}
    </div>
  );
}
