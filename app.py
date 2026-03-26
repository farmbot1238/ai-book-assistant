from flask import Flask, request, jsonify, render_template
import os
import google.generativeai as genai

app = Flask(__name__)

# إعداد مفتاح API من متغير البيئة
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question', '')
    response = model.generate_content(user_question)
    return jsonify({'answer': response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)