from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


"""
@app.route('/api/chat', methods=['POST'])
def api_chat():
    user_message = request.json.get('user_message')
    return {"robot_message": "I received your message. " + user_message}
"""


if __name__ == '__main__':
    app.run(debug=True, port=80)