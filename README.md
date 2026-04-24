# Insurance Premium Prediction

## Problem Statement

Insurance companies determine premium costs based on various demographic and medical factors. The objective of this project is to build a predictive system that estimates insurance premiums using features such as age, medical history, and lifestyle indicators. This helps in understanding key drivers of insurance pricing and enables data-driven decision-making.

---

## Target Metric

The performance of the model is evaluated using:

* **R² Score (Coefficient of Determination)** – to measure how well the model explains variance in premium prices
* **RMSE (Root Mean Squared Error)** – to measure prediction error

---

## Approach

### 1. Exploratory Data Analysis (EDA)

* Analyzed distributions of all variables
* Identified relationships between features and premium price
* Detected outliers using statistical methods
* Observed strong correlation between age and premium

---

### 2. Hypothesis Testing

* Performed statistical tests to validate assumptions:

  * T-tests for binary variables (e.g., diabetes, chronic diseases)
  * Kruskal-Wallis test for non-parametric comparisons
  * Levene’s test for variance equality
* Found that factors like chronic diseases, transplants, and surgeries significantly affect premiums

---

### 3. Feature Engineering

* Created **BMI** feature using height and weight
* Encoded categorical variables into numerical format
* Prepared dataset for machine learning models

---

### 4. Model Building

Implemented and compared multiple models:

* Linear Regression (baseline)
* Random Forest Regressor
* XGBoost Regressor

---

### 5. Model Evaluation & Tuning

* Evaluated models using RMSE and R²
* Performed **hyperparameter tuning (GridSearchCV)** for Random Forest
* Compared training and testing performance to detect overfitting

---

## Final Model Performance

**Best Model: Random Forest (Hyeper-parameter Tuned)**

* **Train R²:** ~0.906
* **Test R²:** ~0.902
* **RMSE:** ~2100

The model shows strong generalization with minimal overfitting.

---

## Key Insights

* **Age is the most significant factor** influencing insurance premiums
* Medical conditions such as **chronic diseases and transplants** significantly increase premiums
* **Number of surgeries**, while statistically significant, has lower predictive importance in the model
* Features like **BMI, allergies, and height** have minimal impact
* Demonstrated the difference between **statistical significance and predictive importance**

---

## Deployment

The model was deployed using a **Streamlit web application**, allowing users to:

* Input personal and medical details
* Get **real-time premium predictions**
* View an estimated prediction range

---

## 🔗 Project Links

*  **Live App:** https://insurance-premium-predictor-dqwfltsxcljyb7tx7eh6rx.streamlit.app/
*  **Tableau Dashboard:** https://public.tableau.com/views/InsuranceCompanyDashbaord/Demographics?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
*  **Loom Video Link:** https://www.loom.com/share/9d450ed0056e4eb1b6f05933783a5544
*  **The Medium Blog Post** https://medium.com/@sajivjose174/eda-and-price-prediction-for-insurance-cost-dataset-using-regression-models-31e55bf02592?postPublishedType=repub
*  **Analysis Notebook:** Insurance_Cost_Prediction_Analysis.ipynb

---

## Conclusion

This project successfully combines statistical analysis and machine learning to predict insurance premiums. It highlights how different analytical approaches can provide complementary insights, and demonstrates the practical application of machine learning through a deployed web application.


