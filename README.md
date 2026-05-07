# 📊 Population vs Sample Stats Simulator

A simple web application built with Python (Flask) that generates a random population(with mean near 50, variance of 10) and takes a random sample based on user input to compare their statistical properties (Mean and Variance). It also visualizes the distribution using Matplotlib.

## 🚀 Live DemoYou can view the live app here: https://sampling-visualisor.onrender.com

## ✨ Features
Dynamic Data Generation: Generates a random normal distribution based on user-defined population size.\
Random Sampling: Extracts a subset of data from the population for comparison.\
Statistical Analysis: Automatically calculates the Mean and Variance for both the population and the sample.\
Data Visualization: Displays a normalized histogram comparing the density of both datasets.\
Responsive Design: Clean, simple UI for both desktop and mobile.\

## 🛠️ Tech Stack
Backend: Python with FlaskData Science Libraries: NumPy for calculations, Matplotlib for plotting.\
Frontend: HTML5 & CSS3\
Deployment: Render (using Gunicorn)\

## 📦 Local Installation & Setup
Clone the repository:
```
git clone https://github.com/dilmilsoach/Sampling-Visualisor
```

Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Run the application:
```
python app.py
```

The app will be available at http://127.0.0.1:5000.

## 📝 Usage
Enter a Population Size (e.g., 5000).\
Enter a Sample Size (e.g., 500).\
Click Calculate & Plot.\
The app will display the calculated Mean and Variance alongside a distribution chart.\

## Created by @dilmilsoach
