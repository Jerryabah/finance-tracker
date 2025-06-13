from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Transaction, Category
from forms import RegistrationForm, LoginForm, TransactionForm, CategoryForm
from datetime import datetime, date
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if username or email already exists
        existing_user = User.query.filter(
            (User.username == form.username.data) | 
            (User.email == form.email.data)
        ).first()
        
        if existing_user:
            flash('Username or email already exists. Please choose different ones.', 'error')
            return render_template('register.html', form=form)
        
        # Create new user
        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash('Login successful!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    # Get recent transactions
    recent_transactions = Transaction.query.filter_by(user_id=current_user.id)\
                                         .order_by(Transaction.created_at.desc())\
                                         .limit(5).all()
    
    # Calculate total income and expenses
    total_income = db.session.query(db.func.sum(Transaction.amount))\
                            .filter_by(user_id=current_user.id, transaction_type='income')\
                            .scalar() or 0
    
    total_expenses = db.session.query(db.func.sum(Transaction.amount))\
                              .filter_by(user_id=current_user.id, transaction_type='expense')\
                              .scalar() or 0
    
    balance = total_income - total_expenses
    
    return render_template('dashboard.html', 
                         recent_transactions=recent_transactions,
                         total_income=total_income,
                         total_expenses=total_expenses,
                         balance=balance)

@app.route('/add_transaction', methods=['GET', 'POST'])
@login_required
def add_transaction():
    form = TransactionForm()
    
    # Populate category choices
    categories = Category.query.all()
    form.category_id.choices = [(c.id, c.name) for c in categories]
    
    if form.validate_on_submit():
        transaction = Transaction(
            amount=form.amount.data,
            description=form.description.data,
            transaction_type=form.transaction_type.data,
            category_id=form.category_id.data,
            date=form.date.data,
            user_id=current_user.id
        )
        
        db.session.add(transaction)
        db.session.commit()
        
        flash('Transaction added successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('add_transaction.html', form=form)

@app.route('/transactions')
@login_required
def transactions():
    page = request.args.get('page', 1, type=int)
    transactions = Transaction.query.filter_by(user_id=current_user.id)\
                                  .order_by(Transaction.date.desc())\
                                  .paginate(page=page, per_page=10, error_out=False)
    
    return render_template('transactions.html', transactions=transactions)

def create_default_categories():
    """Create default categories if none exist"""
    if Category.query.count() == 0:
        default_categories = [
            Category(name='Food & Dining', description='Restaurants, groceries, etc.'),
            Category(name='Transportation', description='Gas, public transport, uber, etc.'),
            Category(name='Entertainment', description='Movies, games, hobbies, etc.'),
            Category(name='Shopping', description='Clothes, electronics, etc.'),
            Category(name='Bills & Utilities', description='Rent, electricity, internet, etc.'),
            Category(name='Healthcare', description='Medical expenses, pharmacy, etc.'),
            Category(name='Salary', description='Regular income from work'),
            Category(name='Other Income', description='Freelance, gifts, etc.'),
            Category(name='Other', description='Miscellaneous expenses'),
        ]
        
        for category in default_categories:
            db.session.add(category)
        
        db.session.commit()
        print("Default categories created.")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_default_categories()
    
    app.run(debug=True)