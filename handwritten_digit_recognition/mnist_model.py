import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# データのロード
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# データの正規化
X_train = X_train / 255.0
X_test = X_test / 255.0

# モデルの構築
model = Sequential([
    Flatten(input_shape=(28, 28)),  # 28x28の画像を1次元に変換
    Dense(128, activation='relu'),  # 隠れ層
    Dense(10, activation='softmax')  # 出力層
])

# モデルのコンパイル
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# モデルのトレーニング
history = model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

# 学習結果の可視化
plt.plot(history.history['accuracy'], label='Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.show()

# モデルの評価
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc}")

# モデルの保存
model.save("mnist_model.h5")
