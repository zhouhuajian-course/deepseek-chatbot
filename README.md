# DeepSeek 聊天机器人项目

## 为 DeepSeek Chatbot 准备零件

**项目演示**

输入提示词：

1. Who are you?
2. How to develop a chatbot?

**环境准备**

前端语言使用 HTML CSS JS

后端语言使用 Python [https://www.python.org/](https://www.python.org/)

编辑器使用 VS Code [https://code.visualstudio.com/](https://code.visualstudio.com/)

**项目搭建**

安装 Flask 库 `pip install Flask`

deepseek-chatbot/app.py

```python
from flask import Flask, render_template

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 定义一个路由和视图函数
@app.route('/')
def home():
    return render_template("index.html")


# 运行应用
if __name__ == '__main__':
    app.run(debug=True)
```

deepseek-chatbot/templates/index.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chatbot</title>
  <link rel="stylesheet" href="/static/index.css">
</head>

<body>
  <h1>🤖</h1>
  <script src="/static/index.js"></script>
</body>

</html>
```

deepseek-chatbot/static/index.css

```css
h1 {
  text-align: center;
}
```

deepseek-chatbot/static/index.js

```javascript
console.log(123);
```

## 给 DeepSeek Chatbot 美化界面

deepseek-chatbot/templates/index.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chatbot</title>
  <link rel="stylesheet" href="/static/index.css">
</head>

<body>
  <h1>🤖</h1>

  <div class="chat">
    <div class="chat-content">
      <!-- <div class="user-message">introduce yourself</div>
      <pre
        class="robot-message">Hello! I’m an AI language model created to assist with answering questions, providing information, brainstorming ideas, and helping with various tasks. I don’t have personal experiences or emotions, but I’m here to help you with whatever you need. Feel free to ask me anything—whether it’s about science, history, writing, or just casual conversation. How can I assist you today? 😊</pre>
      <div class="user-message">introduce yourself</div>
      <pre
        class="robot-message">Hello! I’m an AI language model created to assist with answering questions, providing information, brainstorming ideas, and helping with various tasks. I don’t have personal experiences or emotions, but I’m here to help you with whatever you need. Feel free to ask me anything—whether it’s about science, history, writing, or just casual conversation. How can I assist you today? 😊</pre>
      <div class="user-message">introduce yourself</div>
      <pre
        class="robot-message">Hello! I’m an AI language model created to assist with answering questions, providing information, brainstorming ideas, and helping with various tasks. I don’t have personal experiences or emotions, but I’m here to help you with whatever you need. Feel free to ask me anything—whether it’s about science, history, writing, or just casual conversation. How can I assist you today? 😊</pre>
      <div class="user-message">introduce yourself</div>
      <pre
        class="robot-message">Hello! I’m an AI language model created to assist with answering questions, providing information, brainstorming ideas, and helping with various tasks. I don’t have personal experiences or emotions, but I’m here to help you with whatever you need. Feel free to ask me anything—whether it’s about science, history, writing, or just casual conversation. How can I assist you today? 😊</pre> -->

    </div>
    <div class="chat-form">
      <input type="text" id="user-message-ipt">
      <button id="send-btn">Send</button>
    </div>
  </div>

  <script src="/static/index.js"></script>
</body>

</html>
```

deepseek-chatbot/static/index.css

```css
h1 {
  text-align: center;
}


.chat {
  max-width: 600px;
  margin: 0 auto;
  border: 1px solid #ccc;
  background-color: #f9f9f9;
}


.chat-content {
  padding: 20px;
  height: 400px;
  overflow-y: scroll;
}

.chat-content .user-message {
  text-align: right;
}

.chat-content .robot-message {
  white-space: pre-wrap;
}


.chat-form {
  padding: 10px;
  display: flex;
}

.chat-form input {
  flex-grow: 1;
  padding: 5px;
  border: 1px solid #ccc;
  margin-right: 10px;
}

.chat-form button {
  flex-grow: 0;
  padding: 5px 10px;
  border: 1px solid #ccc;
  cursor: pointer;
}
```

deepseek-chatbot/static/index.js

```javascript
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
  }
}

```

## 教 DeepSeek Chatbot 会话补全

会话补全接口

[https://api-docs.deepseek.com/zh-cn/api/create-chat-completion](https://api-docs.deepseek.com/zh-cn/api/create-chat-completion)

错误码

[https://api-docs.deepseek.com/zh-cn/quick_start/error_codes](https://api-docs.deepseek.com/zh-cn/quick_start/error_codes)

模型 & 价格

[https://api-docs.deepseek.com/zh-cn/quick_start/pricing](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)

deepseek-chatbot/static/index.js

```javascript
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
    // const robotMessagePre = document.createElement('pre')
    // robotMessagePre.className = 'robot-message'
    // robotMessagePre.textContent = "I'm a robot!"
    // chatContent.append(robotMessagePre)

    // 服务端接口：http://127.0.0.1/api/chat
    // 请求方法：POST
    // 请求体：{"user_message": "Hi"}
    // 响应体：{"robot_message": "Hello"}

    fetch('/api/chat', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ "user_message": userMessage })
    })
      .then(response => response.json())
      .then(data => {
        const robotMessagePre = document.createElement('pre')
        robotMessagePre.className = 'robot-message'
        robotMessagePre.textContent = data['robot_message']
        chatContent.append(robotMessagePre)
      })
  }
}

```

deepseek-chatbot/app.py

```python
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")



@app.route('/api/chat', methods=['POST'])
def api_chat():
    user_message = request.json.get('user_message')

    url = "https://api.deepseek.com/chat/completions"
    payload = json.dumps({
        "messages": [
            {
                "content": user_message,
                "role": "user"
            }
        ],
        "model": "deepseek-chat",
        "n": 1
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer sk-ca3371d655c3431397022c8cee313788'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    robot_message = response.json()['choices'][0]['message']['content']
    return {"robot_message": robot_message}



if __name__ == '__main__':
    app.run(debug=True, port=80)
```

deepseek-chatbot/test.py

安装 requests 库 `pip install requests`

```python
import requests
import json

url = "https://api.deepseek.com/chat/completions"

payload = json.dumps({
  "messages": [
    {
      "content": "Hi",
      "role": "user"
    }
  ],
  "model": "deepseek-chat",
  "n": 1
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer sk-ca3371d655c3431397022c8cee313788'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.status_code)
print(response.text)
robot_message = response.json()['choices'][0]['message']['content']
print(robot_message)
```

## 学 DeepSeek 流式 API

[Server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) 服务器发送事件

[https://developer.mozilla.org/zh-CN/docs/Web/API/Server-sent_events/Using_server-sent_events](https://developer.mozilla.org/zh-CN/docs/Web/API/Server-sent_events/Using_server-sent_events)

deepseek-chatbot/app.py

```python
from flask import Flask, render_template, request, Response
import requests
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")



@app.route('/api/chat', methods=['POST'])
def api_chat():
    user_message = request.json.get('user_message')

    url = "https://api.deepseek.com/chat/completions"

    payload = json.dumps({
      "messages": [
        # {
        #   "content": "You are a software developer",
        #   "role": "system"
        # },
        {
          "content": user_message,  # Hello! How can I assist you today? 😊
          "role": "user"    # 你好！很高兴见到你。你今天想学些什么中文呢？
        }                   # Hello! How can I assist you today? Are you working on a coding project, or do you have a question about software development? Let me know! 😊
      ],
      "model": "deepseek-chat",
      "n": 1
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer sk-492ec2acc35c4d20b6ab2c9490fcef0d'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    robot_message = response.json()['choices'][0]['message']['content']
    return {"robot_message": robot_message}



@app.route('/api/v2/chat')
def api_v2_chat():
    import time
    def robot_message():
        for chunk in ["I'm ", "a ", "robot"]: 
            # yield chunk
            # yield "data: " + chunk + "\n\n"
            yield "data: " + json.dumps({'chunk': chunk}) + "\n\n"
            time.sleep(1)
        yield "data: [DONE]\n\n"
    
    return Response(robot_message(), content_type="text/event-stream")



if __name__ == '__main__':
    app.run(debug=True, port=80)
```

deepseek-chatbot/static/index.js

```javascript
console.log(123);

window.onload = () => {
  const chatContent = document.querySelector('.chat-content')
  const userMessageIpt = document.querySelector('#user-message-ipt')
  const sendBtn = document.querySelector('#send-btn')

  sendBtn.onclick = () => {
    const userMessage = userMessageIpt.value

    userMessageIpt.value = ''
    sendBtn.disabled = true

    // <div class="user-message">introduce yourself</div>
    const userMessageDiv = document.createElement('div')
    userMessageDiv.className = 'user-message'
    userMessageDiv.textContent = userMessage
    chatContent.append(userMessageDiv)
    // <pre class="robot-message">Hello! I’m an AI language model created to assist with answering questions, providing information, brainstorming ideas, and helping with various tasks. I don’t have personal experiences or emotions, but I’m here to help you with whatever you need. Feel free to ask me anything—whether it’s about science, history, writing, or just casual conversation. How can I assist you today? 😊</pre>
    // const robotMessagePre = document.createElement('pre')
    // robotMessagePre.className = 'robot-message'
    // robotMessagePre.textContent = "I'm a robot!"
    // chatContent.append(robotMessagePre)

    // 服务端接口：http://127.0.0.1/api/chat
    // 请求方法：POST
    // 请求体：{"user_message": "Hi"}
    // 响应体：{"robot_message": "Hello"}

    // fetch('/api/chat', {
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

    const robotMessagePre = document.createElement('pre')
    robotMessagePre.className = 'robot-message'
    // robotMessagePre.textContent = "I'm a robot!"
    chatContent.append(robotMessagePre)
    const eventSource = new EventSource('/api/v2/chat')
    eventSource.onmessage = (event) => {
      console.log(event.data);
      if (event.data == '[DONE]') {
        eventSource.close()
        sendBtn.disabled = false
      } else {
        robotMessagePre.textContent += JSON.parse(event.data)['chunk']
      }
    }
  }
}

```

## 让 DeepSeek Chatbot 像流水般说话

对话补全接口

[https://api-docs.deepseek.com/zh-cn/api/create-chat-completion](https://api-docs.deepseek.com/zh-cn/api/create-chat-completion)

deepseek-chatbot/static/index.js

```javascript
console.log(123);

window.onload = () => {
  const chatContent = document.querySelector('.chat-content')
  const userMessageIpt = document.querySelector('#user-message-ipt')
  const sendBtn = document.querySelector('#send-btn')

  sendBtn.onclick = () => {
    const userMessage = userMessageIpt.value

    userMessageIpt.value = ''
    sendBtn.disabled = true

    // <div class="user-message">introduce yourself</div>
    const userMessageDiv = document.createElement('div')
    userMessageDiv.className = 'user-message'
    userMessageDiv.textContent = userMessage
    chatContent.append(userMessageDiv)
    // <pre class="robot-message">Hello! I’m an AI language model created to assist with answering questions, providing information, brainstorming ideas, and helping with various tasks. I don’t have personal experiences or emotions, but I’m here to help you with whatever you need. Feel free to ask me anything—whether it’s about science, history, writing, or just casual conversation. How can I assist you today? 😊</pre>
    // const robotMessagePre = document.createElement('pre')
    // robotMessagePre.className = 'robot-message'
    // robotMessagePre.textContent = "I'm a robot!"
    // chatContent.append(robotMessagePre)

    // 服务端接口：http://127.0.0.1/api/chat
    // 请求方法：POST
    // 请求体：{"user_message": "Hi"}
    // 响应体：{"robot_message": "Hello"}

    // fetch('/api/chat', {
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

    const robotMessagePre = document.createElement('pre')
    robotMessagePre.className = 'robot-message'
    // robotMessagePre.textContent = "I'm a robot!"
    chatContent.append(robotMessagePre)
    const eventSource = new EventSource('/api/v2/chat?user_message=' + encodeURIComponent(userMessage))
    eventSource.onmessage = (event) => {
      console.log(event.data);
      if (event.data == '[DONE]') {
        eventSource.close()
        sendBtn.disabled = false
      } else {
        robotMessagePre.textContent += JSON.parse(event.data)['chunk']
        chatContent.scrollTop = chatContent.scrollHeight
      }
    }
  }
}

```

deepseek-chatbot/app.py

```python
from flask import Flask, render_template, request, Response
import requests
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")



@app.route('/api/chat', methods=['POST'])
def api_chat():
    user_message = request.json.get('user_message')

    url = "https://api.deepseek.com/chat/completions"

    payload = json.dumps({
      "messages": [
        # {
        #   "content": "You are a software developer",
        #   "role": "system"
        # },
        {
          "content": user_message,  # Hello! How can I assist you today? 😊
          "role": "user"    # 你好！很高兴见到你。你今天想学些什么中文呢？
        }                   # Hello! How can I assist you today? Are you working on a coding project, or do you have a question about software development? Let me know! 😊
      ],
      "model": "deepseek-chat",
      "n": 1
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer sk-492ec2acc35c4d20b6ab2c9490fcef0d'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    robot_message = response.json()['choices'][0]['message']['content']
    return {"robot_message": robot_message}



@app.route('/api/v2/chat')
def api_v2_chat():
    user_message = request.args.get('user_message')
        
    url = "https://api.deepseek.com/chat/completions"

    payload = json.dumps({
      "messages": [
        {
          "content": user_message, 
          "role": "user"    
        }                   
      ],
      "model": "deepseek-chat",
      "n": 1,
      "stream": True
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer sk-492ec2acc35c4d20b6ab2c9490fcef0d'
    }

    response = requests.request("POST", url, headers=headers, data=payload, stream=True)
   
    

    # import time
    def robot_message():
        for line in response.iter_lines():
            if not line:
                continue
            if line == b'data: [DONE]':
                print("DONE")
                yield "data: [DONE]\n\n"
            else:
                chunk = json.loads(line[6:])['choices'][0]['delta']['content']    
                if not chunk:
                    continue
                print(chunk)
                yield "data: " + json.dumps({'chunk': chunk}) + "\n\n"
        # for chunk in ["I'm ", "a ", "robot"]: 
        #     # yield chunk
        #     # yield "data: " + chunk + "\n\n"
        #     yield "data: " + json.dumps({'chunk': chunk}) + "\n\n"
        #     time.sleep(1)
        # yield "data: [DONE]\n\n"

    return Response(robot_message(), content_type="text/event-stream")



if __name__ == '__main__':
    app.run(debug=True, port=80)
```

deepseek-chatbot/test.py

```python
import requests
import json

url = "https://api.deepseek.com/chat/completions"

payload = json.dumps({
    "messages": [
        # {
        #   "content": "You are a software developer",
        #   "role": "system"
        # },
        {
            "content": "Hi",  # Hello! How can I assist you today? 😊
            "role": "user"    # 你好！很高兴见到你。你今天想学些什么中文呢？
        }                   # Hello! How can I assist you today? Are you working on a coding project, or do you have a question about software development? Let me know! 😊
    ],
    "model": "deepseek-chat",
    "n": 1,
    "stream": True
})
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer sk-492ec2acc35c4d20b6ab2c9490fcef0d'
}

response = requests.request("POST", url, headers=headers, data=payload, stream=True)
print(response.status_code)
print(response.headers['Content-Type'])
# print(response.text)
# robot_message = response.json()['choices'][0]['message']['content']

for line in response.iter_lines():
    # print(line)
    if not line:
        continue
    if line == b'data: [DONE]':
        print("DONE")
    else:
        chunk = json.loads(line[6:])['choices'][0]['delta']['content']    
        if not chunk:
            continue
        print(chunk)



"""
data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":"Hello"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":"!"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" How"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" can"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" I"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" assist"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" you"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" today"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":"?"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" 😊"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":""},"logprobs":null,"finish_reason":"stop"}],"usage":{"prompt_tokens":4,"completion_tokens":11,"total_tokens":15,"prompt_tokens_details":{"cached_tokens":0},"prompt_cache_hit_tokens":0,"prompt_cache_miss_tokens":4}}

data: [DONE]


"""
```

deepseek-chatbot/test.json

```json
{
  "id": "2da1725d-8eec-4612-a8da-e76cd896052b",
  "object": "chat.completion.chunk",
  "created": 1742954476,
  "model": "deepseek-chat",
  "system_fingerprint": "fp_3d5141a69a_prod0225",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "Hello"
      },
      "logprobs": null,
      "finish_reason": null
    }
  ]
}
```

