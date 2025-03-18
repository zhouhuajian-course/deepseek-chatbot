from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


"""
@app.route('/api/v1/chat/send', methods=['POST'])
def api_v1_chat_send():
    user_message = request.json.get('user_message', '').strip()  
    if not user_message:
        abort(400)
      
    # url = "https://api.deepseek.com/chat/completions"
    # payload = json.dumps({
    #   "messages": [
    #     {
    #       "content": user_message,
    #       "role": "user"
    #     }
    #   ],
    #   "model": "deepseek-chat",
    # })
    # headers = {
    #   'Content-Type': 'application/json',
    #   'Accept': 'application/json',
    #   'Authorization': 'Bearer sk-05c6f9a1625543299f1dd5850b2f6d7c'
    # }
    # deepseek_response = requests.request("POST", url, headers=headers, data=payload)
    # robot_message = deepseek_response.json()['choices'][0]['message']['content']
    # return {"robot_message": robot_message}

    return {"robot_message": "I'm a chatbot!"}
"""


if __name__ == '__main__':
    app.run(debug=True, port=80)