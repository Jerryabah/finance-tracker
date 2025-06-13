# Finance Tracker

A simple and secure personal finance tracking web application built with Flask.

📸 Screenshots

![01  Before Logging in](https://github.com/user-attachments/assets/7eb6158f-39b6-4d59-b176-89a3ea4fef50)
Welcome Page and secure login system with password hashing

![02  Dashboard](https://github.com/user-attachments/assets/5ba63f59-56eb-4ccb-988f-73a328a54a89)
Dashboard with easy-to-use form for adding income and expenses

![03  Dashboard with Transactions](https://github.com/user-attachments/assets/48993055-3800-47d1-b4f6-b593a2773d53)
Dashboard with updated financial balances at a glance.

![04  Recent Transactions](https://github.com/user-attachments/assets/2a57ca89-c138-423d-bb7d-093bd71b5eb4)
Complete transaction history with filtering and categorization



#Screenshots


## Features

- User registration and login system
- Add and view financial transactions
- Categorize income and expenses
- Dashboard with financial overview
- Responsive Bootstrap design
- Secure password hashing and CSRF protection

## Technologies Used

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login with password hashing
- **Forms**: Flask-WTF with validation
- **Frontend**: Bootstrap 5, HTML5, CSS3

## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jerryabah/finance-tracker.git
   cd finance-tracker
   ```

2. **Create virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000` OR `http://127.0.0.1:5000/`

## Usage

1. Register a new account or login with existing credentials
2. Add transactions by clicking "Add Transaction"
3. View your dashboard to see financial overview
4. Browse all transactions in the transactions page

## Project Structure

```
finance_tracker/
├── app.py              # Main Flask application
├── models.py           # Database models
├── forms.py            # WTForms for user input
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # Custom CSS styles
└── templates/         # HTML templates
    ├── base.html
    ├── index.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── add_transaction.html
    └── transactions.html
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Contact

Project Link: [https://github.com/Jerryabah/finance-tracker](https://github.com/Jerryabah/finance-tracker)
