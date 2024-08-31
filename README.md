# Task-Final
Final Project: Survey Tool for Income Spending Analysis

Overview
This project includes a Flask web application for collecting user data, storing it in MongoDB, processing it with Python, and visualizing the results in a Jupyter notebook.

Project Structure
 app.py: Flask application for data collection.
 index.html: HTML form for user input.
 data_processing.py: Python class for data processing.
 user_data.csv: CSV file generated from the collected data.
 visualization.ipynb: Jupyter notebook with data visualization.
 README.md: Instructions for deploying and running the project.

 Setup and Installation
1. Clone the repository.
2. Install required Python packages: Flask, pymongo, pandas, matplotlib.
3. Set up MongoDB on your local machine.
4. Run the Flask application using python app.py.
5. Open your web browser and go to https://localhost:5000/ to use the application.

Deployment on AWS
1. Set up an AWS account and create a new Elastic Beanstalk or EC2 instance.
2. Upload your project files and configure the environment.
3. Deploy the Flask application and access it via the provided AWS URL.

Visualization
The data visualization results are stored as PNG files and can be used for presentations.
