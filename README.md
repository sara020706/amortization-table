# amortization table 

# AmortizePro - Loan Amortization Calculator

**AmortizePro** is a modern, visually appealing loan amortization calculator built with **Django** and **Tailwind CSS**. It allows users to input loan details, calculate monthly payments, total interest, total payment, and view a full amortization schedule in a beautifully styled interface.

---

## Features

- **Loan Calculation**: Calculates monthly payment, total payment, and total interest based on loan amount, interest rate, and term.  
- **Amortization Schedule**: Generates a detailed table showing month-by-month principal, interest, and remaining balance.  
- **Responsive Design**: Works perfectly on mobile, tablet, and desktop devices.  
- **Tailwind Styling**: Gradient backgrounds, cards, shadows, and animations for a modern UI.  
- **Error Handling**: Validates user input and provides clear error messages.  

---

## Tech Stack

- **Backend**: Django 5.2  
- **Frontend**: HTML, Tailwind CSS  
- **Language**: Python 3.13  
- **Deployment**: Local development server (can be deployed on any WSGI-compatible server)

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/amortizepro.git
   cd amortizepro
Create and activate a virtual environment


python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies


pip install -r requirements.txt
Apply migrations


python manage.py migrate
Run the development server


python manage.py runserver

Open in browser


http://127.0.0.1:8000/
Usage
Enter Loan Amount, Annual Interest Rate, and Loan Term (Years).

Click Calculate.

View Monthly Payment, Total Payment, Total Interest, and the Amortization Schedule.

Use the Back to Calculator button to perform a new calculation.

Project Structure

amortizepro/
│
├─ loan_app/
│   ├─ templates/
│   │   └─ loan_app/
│   │       ├─ index.html
│   │       └─ results.html
│   ├─ views.py
│   ├─ urls.py
│   └─ ...
│
├─ loan_calc/
│   └─ settings.py
│
├─ manage.py
└─ README.md
Contributing
Contributions are welcome!

Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature/your-feature)

Open a Pull Request

License
This project is licensed under the MIT License.

Contact
GitHub: sara020706

Email: ps2601296@gmail.com