document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.createElement('div');
    chatContainer.id = 'chatbot-container';
    document.body.appendChild(chatContainer);

    const chatBox = document.createElement('div');
    chatBox.id = 'chatbox';
    chatContainer.appendChild(chatBox);

    const inputField = document.createElement('input');
    inputField.type = 'text';
    inputField.id = 'user-input';
    inputField.placeholder = 'Ask me anything...';
    chatContainer.appendChild(inputField);

    inputField.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            const userMessage = inputField.value;
            inputField.value = '';
            chatBox.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;

            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userMessage })
            })
            .then(response => response.json())
            .then(data => {
                chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
            });
        }
    });
});
