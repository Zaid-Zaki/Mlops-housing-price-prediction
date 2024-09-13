# House Price Prediction with MLOps

This project implements a house price prediction model as a Flask web service, following modern MLOps best practices. Users can input house-related features and receive predictions from the trained machine learning model. The project also incorporates CI/CD using GitHub Actions and multi-environment testing, with deployment on Vercel.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training and API](#model-training-and-api)
- [Evaluation Metrics](#evaluation-metrics)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project involves creating a machine learning model for predicting house prices using input features like average area income, house age, number of rooms, etc. The project follows MLOps practices and includes continuous integration and deployment pipelines.

## Project Structure


## Technologies Used

- **Flask**: Web framework for building the API.
- **scikit-learn**: For training the machine learning model.
- **Pandas**: Data manipulation and preparation.
- **Numpy**: Numerical computing.
- **Vercel**: For deployment.
- **GitHub Actions**: For CI/CD pipelines.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-repo/house-price-prediction.git
    ```
2. Change into the project directory:
    ```bash
    cd house-price-prediction
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask app:
    ```bash
    python app.py
    ```
2. Access the application at `http://localhost:5000`.

3. Enter values for features like average area income, house age, number of rooms, etc. The model will return the predicted house price along with evaluation metrics like MAE, MSE, and RMSE.

## Model Training and API

- **Data**: The dataset used is a house price dataset.
- **Model**: The machine learning model is a linear regression model trained using `scikit-learn`.
- **API Endpoint**: The API exposes a `/predict` route that accepts POST requests with house-related features, and returns a prediction.

## Evaluation Metrics

The model's performance is evaluated using:
- **MAE (Mean Absolute Error)**
- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Squared Error)**

## Deployment

The application is deployed on Vercel. Follow the steps below for CI/CD using GitHub Actions:
1. Push to GitHub triggers the CI pipeline.
2. Automatic testing and linting are performed.
3. After passing tests, the app is deployed to Vercel in three environments: `dev`, `stage`, and `prod`.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
