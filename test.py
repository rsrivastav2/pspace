/* styles.css */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  text-align: center;
}

.header {
  font-size: 2rem;
  margin-bottom: 20px;
}

.button {
  padding: 10px 20px;
  font-size: 1.2rem;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.button:hover {
  background-color: #0056b3;
}

@media (max-width: 768px) {
  .header {
    font-size: 1.5rem;
  }

  .button {
    font-size: 1rem;
  }
}
