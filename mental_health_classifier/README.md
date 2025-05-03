# 🧠 Mental Health Tweet Classifier

This project uses **Natural Language Processing (NLP)** to classify mental health-related tweets into specific mental health conditions such as *Anxiety*, *Depression*, *Stress*, *Suicidal Ideation*, and more. It includes a deployable Gradio web app and a full ML pipeline from preprocessing through model training and evaluation.

## 🚀 Live Demo
[![View on Hugging Face](https://img.shields.io/badge/Launch%20App-Hugging%20Face-blue)](https://huggingface.co/spaces/zda23/mental_health_classifier)

## 📌 Project Highlights

- **TF-IDF + Logistic Regression Pipeline:** Chosen for its strong performance and interpretability.
- **Custom Label Encoding:** Multi-class classification problem with 7 target classes.
- **Model Evaluation:** Includes precision, recall, F1-score, and confusion matrix heatmap.
- **Gradio UI:** Clean, user-friendly interface for live model interaction.
- **Hosted on Hugging Face Spaces:** Easily accessible, lightweight deployment without requiring local setup.

## 🛠️ Technologies Used

- Python
- scikit-learn
- pandas, numpy
- matplotlib, seaborn
- Gradio
- Hugging Face Spaces
- joblib (for model serialization)

## 🧩 Folder Structure

mental_health_classifier/ ├── app.py # Gradio interface script ├── logistic_model.joblib # Trained logistic regression model ├── tfidf_vectorizer.joblib # Saved TF-IDF vectorizer ├── requirements.txt # Dependencies for Hugging Face Spaces ├── README.md # This file

Copy
Edit

## 📈 Skills Demonstrated

✅ End-to-end model deployment  
✅ Handling multi-class text classification  
✅ Model interpretability and reproducibility  
✅ Practical experience with Hugging Face and Gradio  
✅ Clean, modular code ready for production and further research

---
