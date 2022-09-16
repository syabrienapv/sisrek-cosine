from unicodedata import name
from main import app
import os
from flask import Flask, request, redirect, render_template
from main.prediksi import top_item
# from main.prediksi_knn import knn_models

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def test_form():
    text = request.form['text']
    rekomendasi = top_item(text)
    # processed_text = text.upper()
    # print(processed_text)
    return render_template('index.html', teks=rekomendasi) 