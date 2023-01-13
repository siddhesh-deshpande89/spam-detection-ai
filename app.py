from flask import Flask, jsonify, request
from spam_detection_ai import SpamDetection

app = Flask(__name__)
  
  
@app.route('/detect-spam', methods=['POST'])
def spam_detection():
    data = request.json

    # DO Spam detection ai
    spam_detection = SpamDetection()
    result = spam_detection.is_spam(data['sentence'])

    return jsonify({"is_spam": result})
  
  
if __name__ == '__main__':
    app.run(debug=True)