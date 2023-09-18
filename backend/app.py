import os
import openai
import random
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_API_KEY')
port = int(os.environ.get('PORT', 5007))

words = [word for word in open('words.txt', 'r').read().split('\n') if len(word) > 0]

@app.route('/api', methods=['GET'])
def get_dad_joke():
    """ Returns a dad joke from ChatGPT API"""

    # pick a random word from words
    word = random.choice(words)

    # make a request to ChatGPT API
    prompt = f'Tell me an original dad joke about {word}'

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = [{"role": "user", "content": prompt}],
    )

    return jsonify({
        "word": word,
        "joke": response['choices'][0]['message']['content']
    })

if __name__ == '__main__':
    app.run(debug=True, port=port)


