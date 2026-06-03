# 🎮 Game Completion Time Prediction System

A complete End-to-End Machine Learning project that predicts **game completionist hours** using game metadata, sales statistics, review metrics, platform information, and publisher details.

This project implements a full ML production pipeline including:

* Data Ingestion
* Data Transformation
* Model Training
* Prediction Pipeline
* Flask Deployment
* Logging & Exception Handling
* Modular Project Structure

---

# 📌 Problem Statement

Predict:

```text
how_long_to_beat_completionist_hrs
```

using features such as:

* Platform Information
* Review Scores
* Sales Metrics
* Game Genre
* Publisher Details
* Revenue Information
* Multiplayer Features
* DLC Information
* And more...

---

# 🚀 Features

✅ Modular ML pipeline architecture

✅ Automatic preprocessing pipeline

✅ Numerical + categorical feature handling

✅ Model serialization using Pickle

✅ Custom exception handling

✅ Logging system

✅ Flask Web App Deployment

✅ Production-style folder structure

---

# 📂 Project Structure

```text
MLProject/

│

├── artifacts/

├── logs/

├── data/

│

├── src/

│   ├── components/

│   │   ├── data_ingestion.py

│   │   ├── data_transformation.py

│   │   └── model_trainer.py

│   │

│   ├── pipeline/

│   │   └── predict_pipeline.py

│   │

│   ├── exception.py

│   ├── logger.py

│   └── utils.py

│

├── templates/

│   ├── index.html

│   └── home.html

│

├── app.py

├── requirements.txt

├── setup.py

└── README.md
```

---

# ⚙️ Technologies Used

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* CatBoost
* XGBoost

### Deployment

* Flask
* HTML
* CSS

### Development Tools

* VS Code
* Git
* GitHub

---

# 📊 Input Features

### Numerical Features

* year
* metacritic_score
* user_score
* critic_review_count
* user_review_count
* na_sales_million
* eu_sales_million
* jp_sales_million
* other_sales_million
* global_sales_million
* estimated_revenue_million_usd
* how_long_to_beat_main_hrs
* launch_price_usd

---

### Categorical Features

* platform
* platform_type
* platform_maker
* platform_generation
* genre
* publisher
* developer
* publisher_region
* publisher_tier
* esrb_rating
* is_sequel
* online_multiplayer
* dlc_released
* microtransactions
* loot_boxes
* game_pass_available
* vr_support
* goty_nominated
* goty_won

---

# 🧠 Machine Learning Pipeline

```text
Raw Dataset

↓

Data Ingestion

↓

Train/Test Split

↓

Data Transformation

↓

Feature Engineering

↓

Model Training

↓

Model Serialization

↓

Prediction Pipeline

↓

Flask Web App
```

---

# 🛠 Installation

Clone repository:

```bash
git clone <repository-url>
```

Move into project:

```bash
cd MLProject
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Running Training Pipeline

Run:

```bash
python -m src.components.data_ingestion
```

This automatically:

* Ingests Data
* Transforms Features
* Trains Models
* Saves Artifacts

---

# 🌐 Running Flask Application

Start server:

```bash
python -m app
```

Open:

```text
http://127.0.0.1:5000
```

---

# 📈 Prediction Workflow

```text
User Input

↓

Flask Form

↓

CustomData Class

↓

DataFrame Creation

↓

Preprocessor.pkl

↓

Model.pkl

↓

Predicted Completion Time
```

---

# 📸 Web Application

Landing Page:

* Project Overview
* Start Prediction Button

Prediction Page:

* Enter Game Information
* Predict Completionist Hours

---

# 🔥 Future Improvements

* Docker Deployment

* Cloud Deployment

* Hyperparameter Optimization

* Better UI Components

* Model Monitoring

* API Deployment

---

# 👨‍💻 Author

Rajarshi Mahato

Machine Learning Enthusiast | Data Science | Computer Vision

---

# ⭐ If you like this project

Give it a star on GitHub.
