from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# The chatbot's response logic
def get_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Greetings!"],
        "how are you": ["I'm just a bot, but I'm doing fine!", from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

def get_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Greetings!"],
        "how are you": ["I'm just a bot, but I'm doing fine!", "Doing great, thanks for asking!", "I'm here to help you!"],
        "what is your name": ["I’m your friendly chatbot.", "You can call me AI.", "My creators didn't name me, but I’m here to help!"],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
    }

    user_input = user_input.lower()

    for keyword in responses:
        if keyword in user_input:
            return random.choice(responses[keyword])

    return "I'm sorry, I don't understand that."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

