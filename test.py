.chatbot-container {
  border: 1px solid #ccc;
  width: 400px;
  height: 500px;
  display: flex;
  flex-direction: column;
  font-family: sans-serif;
  background-color: #f9f9f9;
}

.chat-window {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
}

.message {
  margin: 8px 0;
  padding: 10px;
  border-radius: 10px;
  max-width: 80%;
}

.message.user {
  background-color: #d0f0fd;
  align-self: flex-end;
}

.message.bot {
  background-color: #e2e2e2;
  align-self: flex-start;
}

.input-area {
  display: flex;
  border-top: 1px solid #ccc;
}

.input-area input {
  flex: 1;
  padding: 10px;
  border: none;
  outline: none;
}

.input-area button {
  padding: 10px 20px;
  border: none;
  background: #007bff;
  color: white;
  cursor: pointer;
}
