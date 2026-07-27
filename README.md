# 💼 Personal Financial Advisor

A machine learning-powered financial recommendation system that provides personalized guidance on debt management, emergency funds, investments, and vehicle decisions based on an individual's financial situation and transportation needs.

---

## 💡 Why I Built This

As a finance and investment enthusiast, I have always preferred investing in assets rather than spending money on depreciating assets.

Recently, I bought a gold chain with the thought that if I ever needed money in the future, I could sell it and recover most of its value. However, after going out recently, I realized something important: sometimes, a depreciating asset can be more useful than an asset that preserves its monetary value.

A vehicle may depreciate over time, but it can provide mobility, convenience, safety, and accessibility when you actually need it.

> [!IMPORTANT]
> ### 💭 A Financial Realization
>
> **You cannot travel in a mutual fund.**
>
> **You cannot shelter under an SIP when it rains.**
>
> **You cannot drive an investment to college, work, or the hospital.**
>
> Sometimes, a depreciating asset is not a bad financial decision —
> it may simply be the price of **convenience, mobility, safety, and necessity**.

This realization inspired me to build a financial advisor that looks at financial decisions more holistically instead of blindly recommending investments or avoiding all liabilities.

---

## 🚀 Live Demo

👉 Try it out here: 🌐 **[Streamlit App](YOUR_STREAMLIT_APP_LINK)**

---

## 📊 Project Overview

The project uses machine learning models to provide personalized financial recommendations based on a user's financial and lifestyle information.

The system includes:

✅ **Debt Focus Prediction:** Determines whether debt management should be a major financial priority.

💰 **Emergency Fund Recommendation:** Evaluates the user's savings and financial situation to provide emergency fund guidance.

📈 **Investment Advice:** Provides personalized investment-related recommendations based on the user's financial profile.

🚗 **Car Recommendation:** Considers transportation needs, travel distance, travel time, transportation costs, family size, and current vehicle ownership.

🤖 **Multi-Target Machine Learning:** Uses separate trained models for different financial recommendation targets.

---

## 🧠 Machine Learning Models

The project uses machine learning pipelines for multiple prediction tasks.

### Random Forest Classifier

Random Forest models are used to predict:

- Debt Focus
- Emergency Fund Status
- Investment Advice
- Car Recommendation

Each model includes preprocessing for numerical and categorical features.

---

## 🧠 Technologies Used

### Language

- Python

### Libraries

- pandas
- scikit-learn
- joblib

### Machine Learning

- RandomForestClassifier
- OneHotEncoder
- ColumnTransformer
- Pipeline

### Frontend & Deployment

- Streamlit

### Model Persistence

- Joblib

---

## 📥 Input Features

The application uses the following information:

- Monthly Income
- Monthly Expenses
- Distance to College/Work
- Travel Time by Bus
- Monthly Transport Cost
- Bus Frequency
- Family Size
- Current Vehicle
- Monthly Loan Payment
- Current Savings

---

## 📤 Predictions

Based on the user's inputs, the system predicts:

| Prediction | Description |
|---|---|
| 💳 Debt Focus | Whether debt management should be prioritized |
| 🛟 Emergency Fund Status | Recommendation regarding emergency savings |
| 📈 Investment Advice | Personalized investment-related recommendation |
| 🚗 Car Recommendation | Whether a vehicle may be financially and practically suitable |

---

## 📁 Files

| File | Description |
|---|---|
| `app.py` | Main Streamlit application |
| `all_models(1).pkl` | Saved machine learning models and feature information |
| `requirements.txt` | Python dependencies required to run the project |
| `README.md` | Project overview and documentation |
| `.gitignore` | Files excluded from version control |

---

## 🔄 How It Works

```text
User Financial & Lifestyle Information
                ↓
        Data Preprocessing
                ↓
        Feature Transformation
                ↓
        Multiple ML Models
                ↓
 ┌──────────────┬──────────────┬──────────────┬──────────────┐
 │ Debt Focus   │ Emergency    │ Investment   │ Car          │
 │ Prediction   │ Fund Status   │ Advice       │ Recommendation│
 └──────────────┴──────────────┴──────────────┴──────────────┘
                ↓
       Personalized Recommendations
