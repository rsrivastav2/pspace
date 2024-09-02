.watermark-image {
    position: absolute; /* Absolute positioning to overlay the watermark */
    top: 50%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /* Center the watermark */
    width: 300px; /* Adjust size as needed */
    height: auto; /* Maintain aspect ratio */
    opacity: 0.2; /* Light transparency */
    pointer-events: none; /* Allow clicks to pass through the watermark */
    z-index: 999; /* Ensure the watermark is above other content */
}
<div className="watermark-container">
            <img src={watermark} alt="Watermark" className="watermark-image" />
