import streamlit as st
import joblib
import pandas as pd
data = joblib.load(r"C:\Users\nairuti\Downloads\all_models.pkl")
targets = [
    "debt_focus",
    "emergency_fund_status",
    "investment_advice",
    "car_recommendation"
]
models = data["models"]
feature_cols = data["feature_cols"]
targets = data["targets"]
st.title("Personal Financial Advisor")
st.write(
    "Get personalized recommendations based on your financial and travel situation."
)
income = st.number_input(
    "Monthly Income",
    min_value=0.0
)
monthly_expenses = st.number_input(
    "Monthly Expenses",
    min_value=0.0
)

distance_to_college_work = st.number_input(
    "Distance to College/Work",
    min_value=0.0
)

travel_time_by_bus = st.number_input(
    "Travel Time by Bus (minutes)",
    min_value=0.0
)

transport_cost = st.number_input(
    "Monthly Transport Cost",
    min_value=0.0
)

bus_frequency = st.number_input(
    "Bus Frequency",
    min_value=0.0
)

family_size = st.number_input(
    "Family Size",
    min_value=1
)

current_vehicle = st.selectbox(
    "Current Vehicle",
    [
        "No vehicle",
        "Bike",
        "Car"
    ]
)

loan_payment = st.number_input(
    "Monthly Loan Payment",
    min_value=0.0
)

savings = st.number_input(
    "Current Savings",
    min_value=0.0
)
if st.button("Get Recommendations"):

    input_data = pd.DataFrame({
        "income": [income],
        "monthly_expenses": [monthly_expenses],
        "distance_to_college_work": [distance_to_college_work],
        "travel_time_by_bus": [travel_time_by_bus],
        "transport_cost": [transport_cost],
        "bus_frequency": [bus_frequency],
        "family_size": [family_size],
        "current_vehicle": [current_vehicle],
        "loan_payment": [loan_payment],
        "savings": [savings]
    })

    predictions = {}

    for target in targets:
        predictions[target] = models[target].predict(input_data)[0]

    st.subheader("Your Personalized Recommendations")

    st.write(
        "Debt Focus:",
        predictions["debt_focus"]
    )

    st.write(
        "Emergency Fund:",
        predictions["emergency_fund_status"]
    )

    st.write(
        "Investment Advice:",
        predictions["investment_advice"]
    )

    st.write(
        "Car Recommendation:",
        predictions["car_recommendation"]
    )