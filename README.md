This my movie recommendation system which i have created using Python, API integration, NLP,content based filtering algorithms and created similarity scores and interactive Streamlit web app for real_time recommendations.
# 🎬 Movie Recommendation System

A Python‑based movie recommendation engine that suggests films similar to a user‑selected title using content-based filtering techniques.

---

## Table of Contents

- [Features](#features)  
- [Technologies](#technologies)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [How It Works](#how-it-works) 
- [Author](#author)  

---

## Features

- 🚀 Quickly recommends movies based on similarity  
- Scalable and easy to extend to other recommendation methodologies  
- Clean, modular Python codebase  

## Technologies

- Python 3.x  
- pandas, NumPy  
- scikit‑learn (TF-IDF, cosine similarity)  
- Streamlit (optional for GUI)

## Project Structure
movie_recommendation/ ├── movie_recommendor.py 
Core recommendation engine ├── movies.csv  # Dataset of movies (title, plot, genres)
requirements.txt  
README.md  

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ojas45shinde/movie_recommendation.git
   cd movie_recommendation
2. **Install dependencies**

     pip install -r requirements.txt



## How It Works

**1. Preprocessing:**

Load movies.csv including plot descriptions.
Clean and vectorize text using TF‑IDF.

**2. Similarity Calculation:**

Compute cosine similarity matrix across all movie plot features.

**3. Recommendation Logic:**

Given an input title, fetch its vector.
Sort other titles by descending similarity (excluding the input).
Return the top N recommendations.  



## AUTHOR : OJAS SHINDE 
