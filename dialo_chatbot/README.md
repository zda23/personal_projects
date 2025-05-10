# 💬 DialoGPT Chatbot

[![Live Demo](https://img.shields.io/badge/🚀%20Launch-DialoGPT%20Chatbot-blue?style=for-the-badge)](https://huggingface.co/spaces/<your-username>/dialo-chatbot)

This project is a lightweight, open-domain conversational chatbot powered by [Microsoft's DialoGPT-small](https://huggingface.co/microsoft/DialoGPT-small) and built with [Gradio](https://gradio.app/) for an interactive web interface.

It allows users to carry on natural language conversations with a transformer-based AI in a browser — no backend server required.

---

## 🚀 Features

- 🔁 Maintains context across multiple dialogue turns  
- 🤖 Powered by Hugging Face Transformers (DialoGPT-small)  
- 🧠 Stateless function for stable deployment on Hugging Face Spaces  
- ⚡ Easily deployable with a single Python script  
- 🌐 Live web interface via Gradio  

---

## 🛠 How to Run Locally

```bash
pip install transformers torch gradio
python app.py
