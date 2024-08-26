document.getElementById('sendBtn').addEventListener('click', function() {
  const userInput = document.getElementById('userInput').value;
  if (userInput.trim() !== '') {
      appendMessage('User', userInput);
      fetchAIResponse(userInput);
      document.getElementById('userInput').value = '';
  }
});

function appendMessage(sender, message) {
  const chatbox = document.getElementById('chatbox');
  chatbox.innerHTML += `<p><strong>${sender}:</strong> ${message}</p>`;
  chatbox.scrollTop = chatbox.scrollHeight;
}

async function fetchAIResponse(query) {
  try {
      const response = await fetch('/chat', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ message: query })
      });

      const data = await response.json();
      const aiResponse = data.response;
      appendMessage('AI', aiResponse);
  } catch (error) {
      console.error('Error fetching AI response:', error);
      appendMessage('AI', 'Sorry, I encountered an error while processing your request.');
  }
}
