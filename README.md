# 手書き数字認識システム

手書きの数字画像をアップロードして、学習済みの機械学習モデルを使用して数字を認識するシステムです。  
Flaskを使用して構築されたバックエンドと、シンプルなインターフェースを持つWebアプリケーションです。

---

## 機能

- **手書き数字の認識**: アップロードされた画像を解析し、数字を認識。
- **ブラウザベースのUI**: ユーザーはブラウザで簡単に操作可能。
- **アップロード画像のプレビュー**: 認識結果とともにアップロードされた画像を表示。

---

## ディレクトリ構造



```
handwritten_digit_recognition/
├── app.py               # Flaskアプリケーション
├── models/
│   └── mnist_model.h5   # 学習済みモデル
├── static/
│   └── styles.css       # CSSスタイルシート
├── templates/
│   └── index.html       # HTMLテンプレート
├── uploads/             # アップロードされた画像（自動生成）
├── requirements.txt     # 必要なPythonライブラリ
└── README.md            # 説明ファイル
```
---

## 必要条件

- **Python**: バージョン 3.7以上  
- **仮想環境**: （推奨）`venv`または`virtualenv`

---

## セットアップ

### 1. リポジトリをクローン

```bash
git clone https://github.com/yourusername/handwritten_digit_recognition.git
cd handwritten_digit_recognition
```

### 2. 仮想環境を作成してアクティブ化 


```bash
python3 -m venv .venv
source .venv/bin/activate  # Windowsの場合は .venv\Scripts\activate
```

### 3. 必要なライブラリをインストール 


```bash
pip install -r requirements.txt
```

### 4. ディレクトリの確認 
 
- `uploads/` フォルダはアプリ起動時に自動生成されます。
 
- モデルファイル（`mnist_model.h5`）が `models/` に存在することを確認してください。


---


## 使用方法 

### 1. アプリケーションを起動 


```bash
python3 app.py
```

### 2. ブラウザでアクセス 
以下のURLにアクセスします:
[http://127.0.0.1:5000](http://127.0.0.1:5000/) 
### 3. 画像をアップロード 

- ページ内の「画像を選択してください」ボタンから画像をアップロード。

- 「認識開始」をクリックすると、認識結果とアップロードした画像が表示されます。


---


## デモ画面 

### ホーム画面 


### 認識結果 



---


## 使用技術 
 
- **バックエンド** : Flask
 
- **機械学習モデル** : TensorFlow
 
- **フロントエンド** : HTML5 / CSS3
 
- **データ処理** : OpenCV, NumPy


---