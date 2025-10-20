import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pickle

# 1️⃣ Load dataset
data = pd.read_csv(r"C:\Users\aravi\OneDrive\Documents\Diabetes_prediction\data\diabetes.csv")

# 2️⃣ Split features and target
X = data.drop("Outcome", axis=1)  # All columns except 'Outcome'
y = data["Outcome"]               # 'Outcome' column is the label

# 3️⃣ Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5️⃣ Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# 6️⃣ Save the model and scaler
pickle.dump(model, open("model/diabetes_model.pkl", "wb"))
pickle.dump(scaler, open("model/scaler.pkl", "wb"))

print("✅ Model trained and saved successfully!")
