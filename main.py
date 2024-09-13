# Importing Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load the Dataset
def load_data():
    HouseDF = pd.read_csv('USA_Housing.csv')
    return HouseDF

# Define Features and Target
def prepare_features_target(HouseDF):
    X = HouseDF[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                 'Avg. Area Number of Bedrooms', 'Area Population']]
    y = HouseDF['Price']
    return X, y

# Train the model
def train_model(X_train, y_train):
    lm = LinearRegression()
    lm.fit(X_train, y_train)
    return lm

# Save the model
def save_model(model, model_path):
    joblib.dump(model, model_path)
    print("Model saved successfully!")

# Load the model
def load_model(model_path):
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

# Main function to prepare data, train, and save model
def prepare_and_save_model():
    HouseDF = load_data()
    X, y = prepare_features_target(HouseDF)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

    model = train_model(X_train, y_train)
    save_model(model, 'models/linear_regression_model.pkl')

# Run the main function if this script is executed
if __name__ == "__main__":
    prepare_and_save_model()
