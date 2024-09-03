.container {
    display: flex; /* Use flexbox for layout */
    align-items: flex-start; /* Align items to the start of the container */
    padding: 20px; /* Add padding if needed */
}

.chart-container {
    flex: 1; /* Allow the chart container to take up available space */
    max-width: 600px; /* Adjust the maximum width of the chart */
}
.sidebar {
    flex: 0 0 auto; /* Prevent the sidebar from growing */
    margin-right: 20px; /* Add margin to the right of the sidebar */
}

.logo-image {
    width: 150px;  /* Adjust width as needed */
    height: auto;  /* Maintain aspect ratio */
    margin-bottom: 20px; /* Add space below the logo */
}

<div className="container">
            <div className="sidebar">
                <img src={logo} alt="Logo" className="logo-image" />
            </div>
