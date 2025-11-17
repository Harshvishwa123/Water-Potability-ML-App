Water Potability Classification with Machine Learning

A machine learning project to predict water potability based on physicochemical properties, deployed as an interactive web application using Streamlit.

🚀 Live Demo

You can try the live application here:
https://water-potability-ml-app-nsecm2rxflegwpbbyegha7.streamlit.app/

📋 Overview

Access to potable water is a fundamental human right, yet it is increasingly threatened by a complex array of anthropogenic contaminants. This project validates the use of machine learning as a robust, scalable tool for automated potability prediction, offering a crucial decision-support system for water resource management.

The application takes 9 key water quality parameters as input and uses a pre-trained machine learning model to classify the water as "Potable" (Safe to drink) or "Not Potable" (Unsafe).

📊 Dataset

This project uses the Water Potability dataset available on Kaggle.

Source: Kaggle Water Potability Dataset

Features: The dataset includes 9 independent variables:

ph

Hardness

Solids (Total Dissolved Solids)

Chloramines

Sulfate

Conductivity

Organic_carbon

Trihalomethanes

Turbidity

Target: Potability (1 = Potable, 0 = Not Potable)

⚙️ Methodology

The machine learning workflow involved several key stages:

Data Preprocessing:

Imputation: Missing values (in ph, Sulfate, Trihalomethanes) were filled using the median strategy to avoid sensitivity to outliers.

Class Imbalance: The target variable was imbalanced (approx. 61% Not Potable vs. 39% Potable). This was handled by applying the SMOTE (Synthetic Minority Over-sampling Technique) to the training data.

Scaling: All features were standardized using StandardScaler.

Model Training & Evaluation:

Twelve different classification models were trained and evaluated using 5-fold stratified cross-validation.

Ensemble methods (CatBoost, LightGBM, Random Forest) significantly outperformed linear and simple probabilistic models, confirming the non-linear complexity of the problem.

The final model deployed in the Streamlit app is based on the best-performing classifier, CatBoost, which achieved the highest ROC-AUC score (0.696).

🖥️ How to Use the App

Navigate to the live Streamlit app.

Use the sliders in the sidebar to input the values for each of the 9 water quality features.

Click the "Predict Potability" button.

The application will display the prediction ("Potable" or "Not Potable") along with a confidence score.

Local Installation

To run this project on your local machine:

Clone the repository:

git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME


Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


Install the dependencies:
(You will need to create a requirements.txt file based on your project)

pip install -r requirements.txt


A typical requirements.txt might look like this:

streamlit
pandas
numpy
scikit-learn
catboost
lightgbm
imblearn 


Run the Streamlit app:

streamlit run app.py


📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
