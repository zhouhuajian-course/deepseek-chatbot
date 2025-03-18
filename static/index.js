console.log(123);

window.onload = () => {
  const chatContent = document.querySelector('.chat-content')
  const userMessageIpt = document.querySelector('#user-message-ipt')
  const sendBtn = document.querySelector('#send-btn')

  sendBtn.onclick = () => {
    const userMessage = userMessageIpt.value
    // <div class="user-message">introduce yourself</div>
    const userMessageDiv = document.createElement('div')
    userMessageDiv.className = 'user-message'
    userMessageDiv.textContent = userMessage
    chatContent.append(userMessageDiv)
    // <pre class="robot-message">Hello! I’m an AI language model created to assist with answering questions, providing information, brainstorming ideas, and helping with various tasks. I don’t have personal experiences or emotions, but I’m here to help you with whatever you need. Feel free to ask me anything—whether it’s about science, history, writing, or just casual conversation. How can I assist you today? 😊</pre>
    const robotMessagePre = document.createElement('pre')
    robotMessagePre.className = 'robot-message'
    robotMessagePre.textContent = "I'm a robot!"
    chatContent.append(robotMessagePre)

    /*
    POST http://127.0.0.1/api/v1/chat/send 
    
    {"user_message":"hi"}

    {"robot_message": "Hello! How can I assist you today? 😊"}
    */
    // fetch('/api/v1/chat/send', {
    //   method: "POST",
    //   headers: { "Content-Type": "application/json" },
    //   body: JSON.stringify({ "user_message": userMessage })
    // })
    //   .then(response => response.json())
    //   .then(data => {
    //     const robotMessagePre = document.createElement('pre')
    //     robotMessagePre.className = 'robot-message'
    //     robotMessagePre.textContent = data['robot_message']
    //     chatContent.append(robotMessagePre)
    //   })

  }
}
