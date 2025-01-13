from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import cv2

# Flask アプリケーションの初期化
app = Flask(__name__)

# アップロードフォルダの設定
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# モデルのロード
model = load_model("models/mnist_model.h5")

@app.route('/')
def index():
    # 初回アクセス時に 'image_url' を空として渡す
    return render_template('index.html', prediction=None, image_url=None)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return redirect(url_for('index'))

    file = request.files['image']
    if file.filename == '':
        return redirect(url_for('index'))

    # ファイルを保存
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # 画像を処理
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28)) / 255.0  # ピクセル値を正規化
    img = np.expand_dims(img, axis=0)  # モデル入力形状に調整

    # モデルで予測
    prediction = model.predict(img)
    predicted_digit = np.argmax(prediction)

    # 'image_url' と 'prediction' をテンプレートに渡す
    return render_template('index.html', prediction=predicted_digit, image_url=file.filename)

# 静的ファイルとしてアップロード画像を提供
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
