const socket = new WebSocket("ws://localhost:8000/ws/chat");
let currentMessageElement = null;

// Send a message and display it in the chat box
function sendMessage() {
  const inputField = document.getElementById("user-input");
  const userMessage = inputField.value.trim();

  if (userMessage) {
    // Display user message
    displayMessage(userMessage, "user-message");

    // Clear input field
    inputField.value = "";

    socket.send(userMessage);

    currentMessageElement = null;
  }
}

// Display a message in the chat box
function displayMessage(message, className) {
  const chatBox = document.getElementById("chat-box");
  const messageElement = document.createElement("div");

  messageElement.className = `message ${className}`;
  messageElement.textContent = message;
  chatBox.appendChild(messageElement);

  chatBox.scrollTop = chatBox.scrollHeight;

  return messageElement;
}

socket.onmessage = function (event) {
  const data = event.data;

  if (data.startsWith("event: thread.run.completed")) {
    currentMessageElement = null; // Reset for next message
    return;
  }

  // If this is the first chunk, create a new message element
  if (!currentMessageElement) {
    currentMessageElement = displayMessage("", "dm-message");
  }

  // Append each new chunk to the current message element
  currentMessageElement.textContent += data;
  const chatBox = document.getElementById("chat-box");
  chatBox.scrollTop = chatBox.scrollHeight;
};

socket.onclose = function () {
  currentMessageElement = null; // Reset for the next message
};

document
  .getElementById("user-input")
  .addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      event.preventDefault();
      sendMessage();
    }
  });
