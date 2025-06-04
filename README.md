# 📊 Student Math Score Predictor

A simple machine learning web app to predict students' math scores based on reading and writing scores and other demographic features. Built with **Jupyter Notebook**, **Scikit-learn**, and deployed using **Streamlit**.

## 🔍 Features Used
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

## 🚀 How to Run Locally

1. Clone or download this repository.

2. (Optional but recommended) Create and activate a virtual environment:

```bash
# If using conda:
conda create -n student_predictor python=3.10
conda activate student_predictor

# Or with venv:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

## 🗂️ Files
- `Project_jstudio_draft3.ipynb`: Model training and experimentation
- `final_model.pkl`: Trained regression model
- `app.py`: Streamlit app for predictions
- `requirements.txt`: Python dependencies

## 📌 Built With
- Python
- Scikit-learn
- Pandas
- Streamlit