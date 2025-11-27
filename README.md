# 🧠 Next Word Prediction with LSTM

### 🔗 Live App: [https://next-word-prediction-with-lstm-pnw.streamlit.app/](https://next-word-prediction-with-lstm-pnw.streamlit.app/)

This project demonstrates a **Next Word Prediction** system built using a **Long Short-Term Memory (LSTM)** neural network. The model is trained on text data to understand context and predict the most probable next word. A **Streamlit web app** is provided for real-time predictions.

---

## 🚀 Features

* ✔️ Tokenization of text data
* ✔️ Automatic sequence generation for training
* ✔️ LSTM-based deep learning model
* ✔️ Next-word prediction using temperature sampling
* ✔️ Streamlit interface for real-time prediction
* ✔️ Trained tokenizer + saved model for reusability

---

## 📂 Project Structure

```
├── app.py                 # Streamlit web app
├── model.h5               # Trained LSTM model
├── tokenizer.pkl          # Saved Keras tokenizer
├── dataset.txt            # Training corpus
└── README.md              # Documentation
```

---

## 🧩 How It Works

### 1️⃣ Data Preparation

* Raw text is cleaned and split into lines.
* Each line is converted to integer sequences using a tokenizer.
* Input sequences are generated like:

```
I love deep learning
→ ["I", "I love", "I love deep", "I love deep learning"]
```

### 2️⃣ Training Data

```python
x , y = input_seq[:,:-1], input_seq[:,-1]
```

* `x` → all words except last
* `y` → last word (label for prediction)

### 3️⃣ Model Architecture

```
Embedding → LSTM → Dense (Softmax)
```

### 4️⃣ Prediction

* User enters a seed text
* Model predicts next word
* Word appended → prediction continues

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repo

```
git clone https://github.com/yourusername/next-word-lstm.git
cd next-word-lstm
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run Locally

```
streamlit run app.py
```

---

## 🌐 Live Hosted App

Click below to try the model:

👉 **[https://next-word-prediction-with-lstm-pnw.streamlit.app/](https://next-word-prediction-with-lstm-pnw.streamlit.app/)**

---

## 📊 Model Summary

* **Embedding Dimension**: 100
* **LSTM Units**: 150
* **Optimizer**: Adam
* **Loss Function**: Categorical Crossentropy
* **Accuracy Achieved**: ~90% (depends on dataset)

---

## 📦 Requirements

```
tensorflow
streamlit
numpy
pickle
keras
```

---

## 🤝 Contribution

Pull requests are welcome! Improve UI, model accuracy, or add NLP features such as:

* Beam search
* Bi-LSTM
* GRU model
* Transformer-based next-word prediction


## ❤️ Author

**Prathmesh Wavhal**
Feel free to connect or ask queries!
