# 💧 Water Potability Prediction

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://water-potability-ml-app-nsecm2rxflegwpbbyegha7.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Machine Learning](https://img.shields.io/badge/ML-CatBoost%20%7C%20RandomForest-green)

A machine learning application that predicts whether water is safe for human consumption based on physicochemical properties. This project integrates environmental assessment principles with computational intelligence to aid in water quality monitoring.

## 🚀 Live Demo
Check out the deployed web application here:
**[👉 Launch Water Potability App](https://water-potability-ml-app-nsecm2rxflegwpbbyegha7.streamlit.app/)**

---

## 📝 Project Overview
Access to safe drinking water is a fundamental human right, yet it is threatened by contaminants ranging from industrial effluents to emerging threats like PFAS. 

This project utilizes the **Water Potability Dataset** to train predictive models. By analyzing factors such as pH, Hardness, and Chloramines, the system classifies water samples as **Potable (1)** or **Not Potable (0)**. The goal is to provide a scalable, automated decision-support tool for water resource management.

## 📊 Dataset
The model is trained on the [Kaggle Water Potability Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability).

**Key Features:**
* **pH:** Acid-base balance of the water.
* **Hardness:** Ca and Mg salts capacity (mg/L).
* **Solids (TDS):** Total dissolved solids (ppm).
* **Chloramines:** Disinfection dosage (ppm).
* **Sulfate:** Dissolved sulfates (mg/L).
* **Conductivity:** Electrical conductivity (μS/cm).
* **Organic Carbon:** Amount of organic carbon (ppm).
* **Trihalomethanes:** Disinfection by-product (μg/L).
* **Turbidity:** Measure of light emitting property.

## ⚙️ Methodology
To ensure robust predictions, the following data processing pipeline was implemented:

1.  **Data Cleaning:** Handling missing values in `pH`, `Sulfate`, and `Trihalomethanes` using **Median Imputation**.
2.  **Class Imbalance Handling:** Applied **SMOTE** (Synthetic Minority Over-sampling Technique) to balance the ratio of Potable vs. Non-Potable samples.
3.  **Scaling:** Features standardized using `StandardScaler`.
4.  **Model Selection:** Evaluated 12 classifiers including Logistic Regression, SVM, and various Ensembles.

## 🏆 Model Performance
Ensemble methods demonstrated the superior performance, capturing the non-linear relationships between chemical features.

| Model | Accuracy | ROC-AUC |
| :--- | :---: | :---: |
| **CatBoost** | **65.0%** | **0.696** |
| Random Forest | 66.2% | 0.690 |
| XGBoost | 63.7% | 0.682 |
| LightGBM | 63.7% | 0.672 |
| Logistic Regression | 49.8% | 0.495 |

*The deployed application utilizes the **CatBoost** model for its superior class-separation ability (ROC-AUC).*

## 💻 Installation & Local Usage

To run this project locally on your machine:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/water-potability-ml.git](https://github.com/your-username/water-potability-ml.git)
    cd water-potability-ml
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app**
    ```bash
    streamlit run app.py
    ```

## 👥 Authors
* **Harsh Vishwakarma** (Roll No. 2022205)
* **Ayan Kumar Singh** (Roll No. 2022122)

How to add this to GitHub:
Go to your GitHub repository.
Click on Add file > Create new file.
Name the file README.md.
Paste the code block above into the editor.
(Optional) Replace your-username in the "Clone the repository" section with your actual GitHub username.
Click Commit changes.
