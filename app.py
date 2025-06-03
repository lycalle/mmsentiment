from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
sentiment_pipeline = pipeline("sentiment-analysis", model="indobenchmark/indobert-base-p1")

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    user_message = req['queryResult']['queryText']
    result = sentiment_pipeline(user_message)
    sentiment = result[0]['label']
    response_text = f"Terima kasih! Sentimen anda: {sentiment}."
    return jsonify({'fulfillmentText': response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
