# 🏗️ Concrete Strength Prediction using Machine Learning

## Domain
In Ghana, building collapse incidents are a recurring problem, often resulting in serious casualties. Between 2000 and 2020, approximately 60 people lost their lives and 140 were injured in 20 reported cases of building collapse. Even in major cities, such incidents still occur, with low-quality building materials, particularly concrete, identified as a key contributing factor.

Concrete in Ghana is typically mixed directly on construction sites rather than purchased as ready-mix, primarily due to the high cost of pre-prepared concrete. However, ready-mix concrete generally meets standardized quality parameters, making it more reliable than on-site mixes.

The quality of concrete is often measured through compressive strength tests, which determine the material’s ability to withstand loads. Compressive strength is influenced by the proportions of components in the mix—cement, water, coarse aggregate, fine aggregate, etc.—as well as environmental factors like temperature, humidity, and exposure conditions. This combination of variables makes predicting concrete strength a complex task.


## 1️⃣ Business Understanding
Concrete is one of the most widely used construction materials, and its compressive strength is a critical factor in determining the structural integrity and durability of buildings and infrastructure.
Traditionally, strength is determined through time-consuming laboratory tests that require casting, curing, and testing specimens.
If we can predict concrete strength accurately before production, engineers can:

Optimize mix design

Reduce testing costs and time

Ensure safety and compliance with standards

Minimize material wastage

## 2️⃣ Problem Statement
Given the mix proportions of concrete ingredients and the curing age, we need to predict the compressive strength (in MPa) without destructive testing.

## 3️⃣ Goal
To build a machine learning model that:

Accurately predicts compressive strength

Can be used by engineers in real-time

Is easy to integrate into a web or mobile application for quick predictions

## 4️⃣ Solution Approach
We follow a CRISP-DM (Cross-Industry Standard Process for Data Mining) approach:

Understand the business needs

Prepare and clean the data

Train multiple ML models

Evaluate model performance

Select the best-performing model

Deploy for real-time use

## 5️⃣Understanding the Data
Dataset: UCI Machine Learning Repository – Concrete Compressive Strength Data Set

Features:
| Feature            | Description           | Unit  |
| ------------------ | --------------------- | ----- |
| Cement             | Cement content in mix | kg/m³ |
| Blast Furnace Slag | Slag content          | kg/m³ |
| Fly Ash            | Fly ash content       | kg/m³ |
| Water              | Water content         | kg/m³ |
| Superplasticizer   | Chemical admixture    | kg/m³ |
| Coarse Aggregate   | Gravel/stones         | kg/m³ |
| Fine Aggregate     | Sand                  | kg/m³ |
| Age                | Curing time           | Days  |
| **Target**         | Compressive Strength  | MPa   |

## 6️⃣ Data Preparation
Checked missing values – dataset was complete

Feature scaling – StandardScaler used

Train-test split – 80% training, 20% testing

Exploratory Data Analysis (EDA) – correlation heatmaps, scatter plots, and distribution checks

## 7️⃣ Modelling
Models Tested:

Linear Regression

Random Forest Regressor

Gradient Boosting Regressor

Hyperparameter tuning performed for Random Forest and Gradient Boosting

## 8️⃣ Evaluation
Metrics Used:

R² Score – How much variance is explained by the model

MAE (Mean Absolute Error) – Average error in MPa

RMSE (Root Mean Squared Error) – Penalizes larger errors more
| Model                   | R² Score | MAE | RMSE |
| ----------------------- | -------- | --- | ---- |
| Linear Regression       | 0.61     | 7.2 | 9.4  |
| Random Forest Regressor | 0.92     | 2.8 | 3.5  |
| Gradient Boosting       | 0.91     | 3.0 | 3.6  |
✅ Random Forest Regressor performed best.

## 9️⃣ Conclusion
Random Forest Regressor is recommended for predicting compressive strength due to high accuracy and stability.

Predictions can help in early decision-making for mix designs without waiting for lab results.

Model can be integrated into construction management tools or mobile apps for real-time use.

### 📚 References
Yeh, I-C. (1998). "Modeling of strength of high-performance concrete using artificial neural networks." Cement and Concrete Research, 28(12), 1797–1808.

UCI Machine Learning Repository – Concrete Compressive Strength Data Set

Scikit-learn documentation: https://scikit-learn.org
