from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Setup MongoDB connection
client = MongoClient('localhost', 27017)
db = client.income_spending_db
collection = db.users

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    age = request.form['age']
    gender = request.form['gender']
    total_income = request.form['total_income']
    expenses = {
        'utilities': request.form.get('utilities', 0),
        'entertainment': request.form.get('entertainment', 0),
        'school_fees': request.form.get('school_fees', 0),
        'shopping': request.form.get('shopping', 0),
        'healthcare': request.form.get('healthcare', 0),
    }

    user_data = {
        'age': int(age),
        'gender': gender,
        'total_income': float(total_income),
        'expenses': {k: float(v) for k, v in expenses.items()}
    }

    collection.insert_one(user_data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
