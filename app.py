from flask import Flask, request, render_template, jsonify
import requests
import os

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/Falconsai/nsfw_image_detection"
headers = {"Authorization": "Bearer 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"}

def query(file):
    data = file.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def get_highest_score_label(response_json):
    highest_score_label = max(response_json, key=lambda x: x['score'])
    return highest_score_label

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file:
            result = query(file)
            highest_score_label = get_highest_score_label(result)
            # Guardar la imagen temporalmente
            file_path = os.path.join('static', 'uploads', file.filename)
            file.seek(0)  # Reset the file pointer to the beginning
            file.save(file_path)
            return jsonify({
                "label": highest_score_label['label'],
                "score": highest_score_label['score'],
                "file_path": file_path
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    os.makedirs(os.path.join('static', 'uploads'), exist_ok=True)
    app.run(debug=True)
