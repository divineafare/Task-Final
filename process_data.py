import csv
from pymongo import MongoClient

class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses

def get_users_from_db():
    client = MongoClient('localhost', 27017)
    db = client.income_spending_db
    collection = db.users

    users = []
    for user_data in collection.find():
        user = User(
            age=user_data['age'],
            gender=user_data['gender'],
            total_income=user_data['total_income'],
            expenses=user_data['expenses']
        )
        users.append(user)
    return users

def save_users_to_csv(users, filename='users.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Age', 'Gender', 'Total Income', 'Utilities', 'Entertainment', 'School Fees', 'Shopping', 'Healthcare']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for user in users:
            writer.writerow({
                'Age': user.age,
                'Gender': user.gender,
                'Total Income': user.total_income,
                'Utilities': user.expenses['utilities'],
                'Entertainment': user.expenses['entertainment'],
                'School Fees': user.expenses['school_fees'],
                'Shopping': user.expenses['shopping'],
                'Healthcare': user.expenses['healthcare'],
            })

if __name__ == '__main__':
    users = get_users_from_db()
    save_users_to_csv(users)
