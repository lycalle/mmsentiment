app = Flask(name)
sentiment_pipeline = pipeline("sentiment-analysis", model="indobenchmark/indobert-base-p1")

@app.route('/webhook', methods=['POST'])
def webhook():
req = request.get_json()
user_message = req['queryResult']['queryText']
result = sentiment_pipeline(user_message)
sentiment = result[0]['label']
response_text = f"Terima kasih! Sentimen anda: {sentiment}."
return jsonify({'fulfillmentText': response_text})

if name == 'main':
app.run(port=5000)