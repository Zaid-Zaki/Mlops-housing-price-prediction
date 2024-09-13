# Importing Libraries
import os
import pandas as pd
import numpy as np
from flask import Flask, request, render_template
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_absolute_error, mean_squared_error
import main 

app_flask = Flask(__name__)

# Load the dataset and train/test split using functions from main.py
HouseDF = main.load_data()
X, y = main.prepare_features_target(HouseDF)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

model_path = 'models/linear_regression_model.pkl'

model = main.load_model(model_path)
if model is None:
    model = main.train_model(X_train, y_train)
    main.save_model(model, model_path)
    print("Model trained and saved successfully!")

# Calculate evaluation metrics using the test set
y_pred = model.predict(X_test)
MAE = mean_absolute_error(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)

@app_flask.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs
        avg_area_income = float(request.form['avg_area_income'])
        avg_area_house_age = float(request.form['avg_area_house_age'])
        avg_area_rooms = float(request.form['avg_area_rooms'])
        avg_area_bedrooms = float(request.form['avg_area_bedrooms'])
        area_population = float(request.form['area_population'])

        # Make prediction
        features = pd.DataFrame([[avg_area_income, avg_area_house_age, avg_area_rooms,
                                  avg_area_bedrooms, area_population]],
                                columns=['Avg. Area Income', 'Avg. Area House Age',
                                         'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms',
                                         'Area Population'])
        prediction = model.predict(features)[0]

        return render_template('index.html', prediction=prediction, MAE=MAE, MSE=MSE, RMSE=RMSE,
                               avg_area_income=avg_area_income, avg_area_house_age=avg_area_house_age,
                               avg_area_rooms=avg_area_rooms, avg_area_bedrooms=avg_area_bedrooms,
                               area_population=area_population)

    return render_template('index.html', MAE=MAE, MSE=MSE, RMSE=RMSE)

if __name__ == '__main__':
    app_flask.run(debug=True)
