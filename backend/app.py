import openai
import os
import random
import requests

from flask import Flask, request, jsonify

app = Flask(__name__)

# expect OPENAI_API_KEY and PORT (default 5007) to be set in env

openai.api_key = os.environ.get('OPENAI_API_KEY')
port = int(os.environ.get('PORT', 5007))

# load words from words.txt and store in memory
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
