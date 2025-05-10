# 📊 Real-Time Sentiment Dashboard

[![Live Demo](https://img.shields.io/badge/🚀%20Launch-Dashboard-blue?style=for-the-badge)](https://huggingface.co/spaces/<your-username>/realtime-sentiment-dashboard)

A clean and interactive real-time sentiment analysis dashboard built with [Gradio](https://gradio.app/) and powered by [Hugging Face Transformers](https://huggingface.co/transformers/). This app simulates streaming tweet-like inputs and classifies their sentiment using a fine-tuned `DistilBERT` model trained on the SST-2 dataset.

---

## ✨ Features

- ⚡ Live sentiment predictions from randomly sampled “tweets”
- 📈 Displays sentiment label and confidence score
- 🔁 Manual refresh to simulate a stream of data
- 🎨 Lightweight Gradio UI ready for Hugging Face Spaces

---

## 🚀 How to Use

Click the **🔁 Refresh** button in the app to generate 10 new random tweet predictions.

Each entry includes:
- 📝 The tweet text
- 🟥 / 🟩 Sentiment (positive or negative)
- 🎯 Confidence score

---

## 🧪 Run Locally

```bash
pip install gradio transformers torch
python app.py
