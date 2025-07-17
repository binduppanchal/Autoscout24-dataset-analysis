import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

st.set_page_config(page_title="Machine Learning Model", page_icon="🧠", layout="wide")

# Load data once and cache it
@st.cache_data
def load_data():
    data = pd.read_csv("autoscout24.csv")
    return data

data = load_data()

# Filtered sample dataset
sample = data[data["make"].isin(["Volkswagen", "Opel", "Ford", "Skoda", "Renault"])]

# Prepare features and target
gear_dummies = pd.get_dummies(sample["gear"], prefix="gear", dtype=int, drop_first= True)

Marken_dummies = pd.get_dummies(sample["make"], prefix="Marke", dtype=int, drop_first= True)

Treibstof_dummies = pd.get_dummies(sample["fuel"], prefix="Treibstof", dtype=int, drop_first= True)

offerType_dummies = pd.get_dummies(sample["offerType"], prefix="offerType", dtype=int, drop_first= True)

sample = pd.concat([sample,gear_dummies, Marken_dummies, Treibstof_dummies, offerType_dummies], axis=1)

sample.dropna(inplace=True)
sample = sample.rename(columns={"Treibstof_Electric/Diesel" : "Treibstof_Electric_Diesel", "Treibstof_Electric/Gasoline" : "Treibstof_Electric_Gasoline", "offerType_Employee's car" : "offerType_Employee_car", "offerType_Pre-registered" : "offerType_Pre_registered"})

X = sample[["mileage", "hp", "gear_Manual", "gear_Semi-automatic", "year", "Marke_Opel",
       "Marke_Renault", "Marke_Skoda", "Marke_Volkswagen", "Treibstof_CNG",
       "Treibstof_Diesel", "Treibstof_Electric", "Treibstof_Electric_Diesel",
       "Treibstof_Electric_Gasoline", "Treibstof_Ethanol",
       "Treibstof_Gasoline", "Treibstof_LPG", "Treibstof_Others",
       "offerType_Employee_car", "offerType_New", "offerType_Pre_registered",
       "offerType_Used"]]

y = sample["price"]

# Train models once and store in session state
if "models" not in st.session_state:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    
    dtr = DecisionTreeRegressor()
    dtr.fit(X_train, y_train)
    
    rfr = RandomForestRegressor()
    rfr.fit(X_train, y_train)
    
    st.session_state.models = {
        "lr": lr,
        "dtr": dtr,
        "rfr": rfr,
        "X_test": X_test,
        "y_test": y_test
    }

models = st.session_state.models

# Rest of your app logic using models["lr"], models["dtr"], models["rfr"], etc.

st.write("Wie teuer war durschnittlich ein Auto von Herstellar X?")
firma = st.selectbox("Welche firma?", ("Volkswagen", "Opel", "Ford", "Skoda", "Renault"))
filtered = sample[sample["make"] == firma]
st.write(f"Die durchschnitliche preis von **{firma}** ist **{filtered['price'].mean():.2f}€**.")



prediction_lr = models["lr"].predict(models["X_test"])
prediction_dtr = models["dtr"].predict(models["X_test"])
prediction_rfr = models["rfr"].predict(models["X_test"])

models_list = ["Linear Regression", "Decision Tree Regression", "Random Forest Regression"]
r2_scores = [r2_score(models["y_test"], prediction_lr), r2_score(models["y_test"], prediction_dtr), r2_score(models["y_test"], prediction_rfr)]
mse_scores = [mean_squared_error(models["y_test"], prediction_lr), mean_squared_error(models["y_test"], prediction_dtr), mean_squared_error(models["y_test"], prediction_rfr)]
mae_scores = [mean_absolute_error(models["y_test"], prediction_lr), mean_absolute_error(models["y_test"], prediction_dtr), mean_absolute_error(models["y_test"], prediction_rfr)]

df2 = pd.DataFrame({
    "Model": models_list,
    "R2 Score": r2_scores,
    "Mean Squared Error": mse_scores,
    "Mean Absolute Error": mae_scores
})
st.subheader("Maß:")
st.dataframe(df2, use_container_width=False)

st.subheader("Vorhersagen")
mileage = st.number_input("Geben Sie den Kilometerstand ein", min_value=10000, step=500)
hp = st.number_input("Geben Sie die PS ein", min_value=1, step=5)
gear = st.selectbox("Type von Gang", ["Automatic", "Manual", "Semi-Automatic"])

gear_Manual = 1 if gear == "Manual" else 0
gear_Semi_Automatic = 1 if gear == "Semi-Automatic" else 0
year = st.selectbox("Geben Sie Jahr ein.", range(2011, 2022))

marke = st.selectbox("Wählen Sie eine Marke", ["Opel", "Renault", "Skoda", "Volkswagen", "Ford"])
Marke_Opel = 1 if marke == "Opel" else 0
Marke_Renault = 1 if marke == "Renault" else 0
Marke_Skoda = 1 if marke == "Skoda" else 0
Marke_Volkswagen = 1 if marke == "Volkswagen" else 0



fuel = st.selectbox("Wählen Sie eine Treibstof", ["CNG", "Diesel", "Electric", "Electric/Diesel", "Electric/Gasoline", "Ethanol", "Gasoline","LPG", "Others", "-/- (Fuel)"])
Treibstof_CNG = 1 if fuel == "CNG" else 0
Treibstof_Diesel = 1 if fuel == "Diesel" else 0
Treibstof_Electric = 1 if fuel == "Electric" else 0
Treibstof_Electric_Diesel = 1 if fuel == "Electric/Diesel" else 0
Treibstof_Electric_Gasoline = 1 if fuel == "Electric/Gasoline" else 0
Treibstof_Ethanol = 1 if fuel == "Ethanol" else 0
Treibstof_Gasoline = 1 if fuel == "Gasoline" else 0
Treibstof_LPG = 1 if fuel == "LPG" else 0
Treibstof_Others = 1 if fuel == "Others" else 0

# "offerType_Employee's car", "offerType_New", "offerType_Pre-registered", "offerType_Used"


offerType = st.selectbox("Wählen Sie ein OfferType", ["Employee's car", "New", "Pre-registered", "Used", "Demonstration"])
offerType_Employee_car = 1 if offerType == "Employee's car" else 0
offerType_New = 1 if offerType == "New" else 0
offerType_Pre_registered = 1 if offerType == "Pre-registered" else 0
offerType_Used = 1 if offerType == "Used" else 0



prediction = models["rfr"].predict([[mileage, hp, gear_Manual, gear_Semi_Automatic, year, Marke_Opel, Marke_Renault, Marke_Skoda, Marke_Volkswagen, Treibstof_CNG, Treibstof_Diesel, Treibstof_Electric, Treibstof_Electric_Diesel, Treibstof_Electric_Gasoline, Treibstof_Ethanol, Treibstof_Gasoline, Treibstof_LPG, Treibstof_Others, offerType_Employee_car, offerType_New, offerType_Pre_registered, offerType_Used]])
st.write(f"Der Preis für dieses Auto beträgt **{prediction[0]:,.4f} €**")
