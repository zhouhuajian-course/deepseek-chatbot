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
    return "Hi, I am a robot!"
    # def robot_message():
    #     for str in ["Hi, ", "I am a ", "robot!"]: 
    #         yield str
    # return Response(robot_message())


if __name__ == '__main__':
    app.run(debug=True, port=80)