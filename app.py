from datetime import date
from flask import Flask, redirect, render_template, request
from pathlib import Path

from database import db
from models import Expense, Income


app = Flask(__name__)
app.secret_key = 'dev'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///budget.db"

db.init_app(app)

@app.route('/')
def home():
    month_input = request.args.get('month')
    if month_input:
        year, month = map(int, month_input.split('-'))
        selected_month = date(year, month, 1)
    else:
        selected_month = date.today().replace(day=1)

    incomes = db.session.execute(
        db.select(Income)
        .where(Income.month == selected_month)
        .order_by(Income.month.desc())
    ).scalars().all()

    expenses = db.session.execute(
        db.select(Expense)
        .where(Expense.month == selected_month)
        .order_by(Expense.category, Expense.name)
    ).scalars().all()

    total_income = sum(income.amount_grosze for income in incomes)
    total_expenses = sum(expense.amount_grosze for expense in expenses)

    remaining = total_income - total_expenses

    return render_template(
        'index.html',
         incomes=incomes,
         expenses=expenses,
         total_income=total_income,
         total_expenses=total_expenses,
         remaining=remaining,
         selected_month=selected_month)

@app.route('/income/add', methods=['GET', 'POST'])
def add_income():
    if request.method == 'POST':
        month_input = request.form['month']
        name = request.form['name']
        amount_input = request.form['amount']

        year, month = map(int, month_input.split('-'))
        month_date = date(year, month, 1)
        amount_grosze = round(float(amount_input)*100)

        income = Income(
            month = month_date,
            name = name,
            amount_grosze = amount_grosze,
        )

        db.session.add(income)
        db.session.commit()
  
    return render_template('add_income.html')


@app.route('/income/manage')
def manage_income():
    month_input = request.args.get('month')

    if month_input:
        year, month = map(int, month_input.split('-'))
        selected_month = date(year, month, 1)
    else:
        selected_month = date.today().replace(day=1)

    incomes = db.session.execute(
        db.select(Income)
        .where(Income.month == selected_month)
        .order_by(Income.name)
    ).scalars().all()

    return render_template(
        'manage_income.html',
        incomes=incomes,
        selected_month=selected_month,
    )

@app.route('/income/edit/<int:income_id>', methods=['GET', 'POST'])
def edit_income(income_id):
    income = db.get_or_404(Income, income_id)

    if request.method == 'POST':
        month_input = request.form['month']
        name = request.form['name']
        amount_input = request.form['amount']

        year, month = map(int, month_input.split('-'))

        income.month = date(year, month, 1)
        income.name = name
        income.amount_grosze = round(float(amount_input)*100)

        db.session.commit()

    return render_template('edit_income.html', income=income)

@app.route('/income/delete/<int:income_id>', methods=['POST'])
def delete_income(income_id):
    income = db.get_or_404(Income, income_id)
    month = income.month

    db.session.delete(income)
    db.session.commit()

    return redirect(f'/income/manage?month={month.strftime("%Y-%m")}')

@app.route('/expense/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        month_input = request.form['month']
        name = request.form['name']
        category = request.form['category']
        amount_input = request.form['amount']

        year, month = map(int, month_input.split('-'))
        month_date = date(year, month, 1)
        amount_grosze = round(float(amount_input)*100)

        expense = Expense(
            month = month_date,
            name = name,
            category = category,
            amount_grosze = amount_grosze,
        )

        db.session.add(expense)
        db.session.commit()
  
    return render_template('add_expense.html')

@app.route('/expense/manage')
def manage_expenses():
    month_input = request.args.get('month')

    if month_input:
        year, month = map(int, month_input.split('-'))
        selected_month = date(year, month, 1)
    else:
        selected_month = date.today().replace(day=1)

    expenses = db.session.execute(
        db.select(Expense)
        .where(Expense.month == selected_month)
        .order_by(Expense.category, Expense.name)
    ).scalars().all()

    return render_template(
        'manage_expenses.html',
        expenses=expenses,
        selected_month=selected_month,
    )

@app.route('/expense/edit/<int:expense_id>', methods=['GET', 'POST'])
def edit_expense(expense_id):
    expense = db.get_or_404(Expense, expense_id)

    if request.method == 'POST':
        month_input = request.form['month']
        name = request.form['name']
        category = request.form['category']
        amount_input = request.form['amount']

        year,month = map(int, month_input.split('-'))

        expense.month = date(year, month, 1)
        expense.name = name
        expense.category = category
        expense.amount_grosze = round(float(amount_input) * 100)

        db.session.commit()

    return render_template('edit_expense.html', expense=expense)

@app.route('/expense/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    expense = db.get_or_404(Expense, expense_id)
    month = expense.month

    db.session.delete(expense)
    db.session.commit()

    return redirect(f'/expense/manage?month={month.strftime("%Y-%m")}')

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)