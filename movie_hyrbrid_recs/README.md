# 🎥 MovieLens Hybrid Recommender System

This project is an end-to-end hybrid recommendation engine built using the [MovieLens 1M dataset](https://grouplens.org/datasets/movielens/1m/). It combines **collaborative filtering** (via matrix factorization with LightFM) and **content-based filtering** (via TF-IDF vectorization of movie genres) to deliver personalized movie suggestions.

[![View Demo on Hugging Face Spaces](https://img.shields.io/badge/🚀_Launch_Demo-Hugging_Face-blue?logo=huggingface)](https://huggingface.co/spaces/your-username/hybrid-movielens-recommender)

## 📊 Features

- ✅ **Hybrid Recommender**: Combines collaborative and content-based scores for stronger personalization
- ✅ **LightFM (WARP loss)** for implicit feedback modeling
- ✅ **TF-IDF Vectorizer** on genres for content similarity
- ✅ **User profile vectors** generated from genre preferences
- ✅ **Interactive Gradio interface** hosted on Hugging Face Spaces

## 🚀 Technologies Used

- Python, Pandas, NumPy
- Scikit-learn, Scipy
- LightFM
- Gradio
- Hugging Face Hub / Spaces

## 🧪 Try It Live

Click the badge above to launch the app in your browser.  
You can select a user ID, adjust the hybrid weight `α`, and switch between:
- Hybrid recommendations
- Collaborative-only
- Content-only

## 🗂️ Dataset

MovieLens 1M ratings and metadata:
- 6,000 users
- 4,000 movies
- 1,000,000+ ratings

## 📂 Repository Structure

