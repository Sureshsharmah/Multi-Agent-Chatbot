document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
    const sendButton = document.getElementById('send-button');
    
    let messageHistory = [
        {
            role: "assistant",
            content: "Hello! I'm your AI legal assistant. I can help with legal procedures in India, corporate law questions, contract explanations, and intellectual property rights. How can I assist you today?"
        }
    ];
    
    userInput.focus();
    
    chatForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        await handleUserMessage();
    });
    
    userInput.addEventListener('keydown', async function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            await handleUserMessage();
        }
    });
    
    async function handleUserMessage() {
        const message = userInput.value.trim();
        if (!message) return;
        
        addMessage('user', message);
        messageHistory.push({ role: 'user', content: message });
        
        userInput.value = '';
        userInput.disabled = true;
        sendButton.disabled = true;
        
        showTypingIndicator();
        
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: message,
                    history: messageHistory
                })
            });
            
            const data = await response.json();
            removeTypingIndicator();
            
            if (data.error) {
                addMessage('assistant', 'Sorry, I encountered an error processing your request. Please try again.');
            } else {
                addMessage('assistant', cleanResponse(data.response));
                messageHistory.push({ role: 'assistant', content: data.response });
            }
        } catch (error) {
            console.error('Error:', error);
            removeTypingIndicator();
            addMessage('assistant', 'I\'m having trouble connecting to the server. Please check your internet connection and try again.');
        } finally {
            userInput.disabled = false;
            sendButton.disabled = false;
            userInput.focus();
        }
    }
    
    function addMessage(role, content) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}`;
        
        const iconDiv = document.createElement('div');
        iconDiv.className = 'message-icon';
        iconDiv.textContent = role === 'user' ? '👤' : '🤖';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        const paragraphs = content.split('\n\n');
        paragraphs.forEach(para => {
            if (para.trim()) {
                const p = document.createElement('p');
                p.innerHTML = para.replace(/\n/g, '<br>');
                contentDiv.appendChild(p);
            }
        });
        
        messageDiv.appendChild(iconDiv);
        messageDiv.appendChild(contentDiv);
        
        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }
    
    function cleanResponse(text) {
        return text
            .replace(/^#+\s+/gm, '')
            .replace(/^-{3,}/gm, '')
            .replace(/\*\*([^*]+)\*\*/g, '$1')
            .replace(/__([^_]+)__/g, '$1')
            .replace(/^[\*\-]\s+/gm, '')
            .replace(/^>\s+/gm, '')
            .replace(/`([^`]+)`/g, '$1')
            .trim();
    }
    
    function showTypingIndicator() {
        const indicatorDiv = document.createElement('div');
        indicatorDiv.className = 'message assistant';
        indicatorDiv.id = 'typing-indicator';
        
        const iconDiv = document.createElement('div');
        iconDiv.className = 'message-icon';
        iconDiv.textContent = '🤖';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        const typingDiv = document.createElement('div');
        typingDiv.className = 'typing-indicator';
        
        for (let i = 0; i < 3; i++) {
            const dot = document.createElement('div');
            dot.className = 'typing-dot';
            typingDiv.appendChild(dot);
        }
        
        contentDiv.appendChild(typingDiv);
        indicatorDiv.appendChild(iconDiv);
        indicatorDiv.appendChild(contentDiv);
        
        chatMessages.appendChild(indicatorDiv);
        scrollToBottom();
    }
    
    function removeTypingIndicator() {
        const indicator = document.getElementById('typing-indicator');
        if (indicator) {
            indicator.remove();
        }
    }
    
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});