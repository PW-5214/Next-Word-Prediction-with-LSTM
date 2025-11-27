import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer   ## text to vec
from tensorflow.keras.preprocessing.sequence import pad_sequences  ## to make same size by addding padding
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
import pickle
model = load_model('next_word.h5')

with open('tokenizer.pickle','rb') as handle:
    tokenizer = pickle.load(handle)

def predict_next(model,tokenizer,text,max_seq):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) >= max_seq:
        token_list = token_list[-(max_seq-1):] # Ensure the seq length matches max_seq-1
    token_list = pad_sequences([token_list],maxlen=max_seq-1,padding='pre')
    predicted = model.predict(token_list,verbose=0)
    pred_next = np.argmax(predicted,axis=1)[0]   # High prob
    for word,index in tokenizer.word_index.items():
        if index == pred_next:
            return word
    return None


## Streamlit app
import streamlit as st
st.title( "Next Word Prediction with LSTM")
input_text = st.text_input("Enter the sequence of words","to be or not to be")
if st.button("Predict Next Word"):
    max_seq = model.input_shape[1] + 1
    next_word = predict_next(model,tokenizer,input_text,max_seq)
    st.write(f"Next word:{next_word}")
